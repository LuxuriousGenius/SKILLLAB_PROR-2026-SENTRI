import smbus
import time

# MPU6050 Registers
MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

bus = smbus.SMBus(1)

# Wake up MPU6050
bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

# === YOUR CALIBRATION VALUES ===
offsetX = 230.97
offsetY = 93.73
offsetZ = 1305.91

scaleX = 16260.07
scaleY = 16303.46
scaleZ = 16572.61

g_to_ms2 = 9.80665

def read_raw(addr):
    high = bus.read_byte_data(MPU6050_ADDR, addr)
    low = bus.read_byte_data(MPU6050_ADDR, addr + 1)
    val = (high << 8) | low
    if val > 32767:
        val -= 65536
    return val

def read_accel():
    raw_x = read_raw(ACCEL_XOUT_H)
    raw_y = read_raw(ACCEL_XOUT_H + 2)
    raw_z = read_raw(ACCEL_XOUT_H + 4)

    # Apply calibration
    ax = (raw_x - offsetX) / scaleX
    ay = (raw_y - offsetY) / scaleY
    az = (raw_z - offsetZ) / scaleZ

    # Convert to m/s²
    ax *= g_to_ms2
    ay *= g_to_ms2
    az *= g_to_ms2

    return ax, ay, az

# Loop
while True:
    ax, ay, az = read_accel()

    print(f"X: {ax:.3f} m/s² | Y: {ay:.3f} m/s² | Z: {az:.3f} m/s²")

    time.sleep(0.2)
