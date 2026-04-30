import smbus
import time
import math

# MPU6050 registers
MPU = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

bus = smbus.SMBus(1)
bus.write_byte_data(MPU, PWR_MGMT_1, 0)

SAMPLES = 5000
g = 9.80665

# -------------------------
# LOW LEVEL READ
# -------------------------
def read_raw(addr):
    high = bus.read_byte_data(MPU, addr)
    low = bus.read_byte_data(MPU, addr+1)
    val = (high << 8) | low
    if val > 32767:
        val -= 65536
    return val

def read_accel_raw():
    return (
        read_raw(ACCEL_XOUT_H),
        read_raw(ACCEL_XOUT_H+2),
        read_raw(ACCEL_XOUT_H+4)
    )

def read_gyro_raw():
    return (
        read_raw(GYRO_XOUT_H),
        read_raw(GYRO_XOUT_H+2),
        read_raw(GYRO_XOUT_H+4)
    )

# -------------------------
# COLLECT SAMPLES
# -------------------------
def collect_accel():
    sx = sy = sz = 0
    for _ in range(SAMPLES):
        x,y,z = read_accel_raw()
        sx += x; sy += y; sz += z
        time.sleep(0.001)
    return sx/SAMPLES, sy/SAMPLES, sz/SAMPLES

# -------------------------
# ACCEL CALIBRATION
# -------------------------
orientations = [
    ("+X","X UP"),
    ("-X","X DOWN"),
    ("+Y","Y UP"),
    ("-Y","Y DOWN"),
    ("+Z","Z UP (flat)"),
    ("-Z","Z DOWN")
]

meas = {}

for key, text in orientations:
    print("\nPlace:", text)
    if input("Press y: ") != 'y':
        exit()
    meas[key] = collect_accel()

def calc(axis, p, n):
    pos = meas[p][axis]
    neg = meas[n][axis]
    offset = (pos + neg)/2
    scale  = (pos - neg)/2
    return offset, scale

offX, scX = calc(0,"+X","-X")
offY, scY = calc(1,"+Y","-Y")
offZ, scZ = calc(2,"+Z","-Z")

print("\nOffsets:", offX, offY, offZ)
print("Scales :", scX, scY, scZ)

# -------------------------
# GYRO CALIBRATION
# -------------------------
print("\nKeep sensor STILL for gyro calibration...")
time.sleep(2)

gx_off = gy_off = gz_off = 0
for _ in range(2000):
    gx,gy,gz = read_gyro_raw()
    gx_off += gx
    gy_off += gy
    gz_off += gz

gx_off /= 2000
gy_off /= 2000
gz_off /= 2000

print("Gyro offsets:", gx_off, gy_off, gz_off)

# -------------------------
# REFERENCE ZERO
# -------------------------
print("\nPlace sensor in DEFAULT position (flat)")
input("Press y: ")

pitch0 = roll0 = 0
for _ in range(1000):
    x,y,z = read_accel_raw()
    ax = (x-offX)/scX
    ay = (y-offY)/scY
    az = (z-offZ)/scZ

    pitch0 += math.degrees(math.atan2(ay, az))
    roll0  += math.degrees(math.atan2(-ax, math.sqrt(ay*ay+az*az)))

pitch0 /= 1000
roll0  /= 1000

print("Reference:", pitch0, roll0)

# -------------------------
# MAIN LOOP
# -------------------------
pitch = roll = yaw = 0
alpha = 0.98
prev = time.time()

while True:
    now = time.time()
    dt = now - prev
    prev = now

    # read accel
    x,y,z = read_accel_raw()
    ax = (x-offX)/scX
    ay = (y-offY)/scY
    az = (z-offZ)/scZ

    # read gyro
    gx,gy,gz = read_gyro_raw()
    gx = (gx - gx_off)/131
    gy = (gy - gy_off)/131
    gz = (gz - gz_off)/131

    # accel angles
    acc_pitch = math.degrees(math.atan2(ay, az))
    acc_roll  = math.degrees(math.atan2(-ax, math.sqrt(ay*ay+az*az)))

    # complementary filter
    pitch = alpha*(pitch + gx*dt) + (1-alpha)*acc_pitch
    roll  = alpha*(roll  + gy*dt) + (1-alpha)*acc_roll
    yaw   += gz * dt

    # apply zero reference
    pitch -= pitch0
    roll  -= roll0

    print(f"PITCH:{pitch:.2f}  ROLL:{roll:.2f}  YAW:{yaw:.2f}")

    time.sleep(0.05)