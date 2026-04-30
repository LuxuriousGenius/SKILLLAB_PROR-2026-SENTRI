import smbus
import time
import math
import tkinter as tk

# =========================
# MPU6050 SETUP
# =========================
MPU = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

bus = smbus.SMBus(1)
bus.write_byte_data(MPU, PWR_MGMT_1, 0)

g = 9.80665
alpha = 0.98

# =========================
# READ FUNCTIONS
# =========================
def read_raw(addr):
    high = bus.read_byte_data(MPU, addr)
    low  = bus.read_byte_data(MPU, addr+1)
    val = (high << 8) | low
    if val > 32767:
        val -= 65536
    return val

def get_accel():
    ax = read_raw(ACCEL_XOUT_H) / 16384.0
    ay = read_raw(ACCEL_XOUT_H + 2) / 16384.0
    az = read_raw(ACCEL_XOUT_H + 4) / 16384.0
    return ax, ay, az

def get_gyro():
    gx = read_raw(GYRO_XOUT_H) / 131.0
    gy = read_raw(GYRO_XOUT_H + 2) / 131.0
    gz = read_raw(GYRO_XOUT_H + 4) / 131.0
    return gx, gy, gz

def get_angles(ax, ay, az):
    pitch = math.degrees(math.atan2(ay, math.sqrt(ax*ax + az*az)))
    roll  = math.degrees(math.atan2(-ax, az))
    return pitch, roll

def normalize(angle):
    while angle > 180:
        angle -= 360
    while angle < -180:
        angle += 360
    return angle

# =========================
# 🔥 CALIBRATION (YOUR LOGIC)
# =========================
print("Keep sensor STILL for calibration...")
time.sleep(2)

pitch_sum = 0
roll_sum = 0
samples = 200

for _ in range(samples):
    ax, ay, az = get_accel()
    p, r = get_angles(ax, ay, az)
    pitch_sum += p
    roll_sum  += r
    time.sleep(0.01)

pitch_offset = pitch_sum / samples
roll_offset  = roll_sum / samples

print(f"Offsets → Pitch: {pitch_offset:.2f}, Roll: {roll_offset:.2f}")

# Gyro calibration for yaw
print("Calibrating gyro (stay still)...")
time.sleep(2)

gz_sum = 0
for _ in range(500):
    _, _, gz = get_gyro()
    gz_sum += gz
    time.sleep(0.002)

gz_offset = gz_sum / 500

print("Calibration complete. Starting GUI...")

# =========================
# STATE VARIABLES
# =========================
pitch = 0
roll = 0
yaw = 0
prev = time.time()

# =========================
# GUI SETUP
# =========================
root = tk.Tk()
root.title("MPU6050 Dashboard")
root.geometry("400x350")

labels = {}

def make_label(name, row):
    tk.Label(root, text=name, font=("Arial", 12)).grid(row=row, column=0, sticky="w")
    val = tk.Label(root, text="0", font=("Arial", 12, "bold"))
    val.grid(row=row, column=1, sticky="w")
    labels[name] = val

fields = [
    "Ax (m/s²)", "Ay (m/s²)", "Az (m/s²)",
    "Pitch (deg)", "Roll (deg)", "Yaw (deg)"
]

for i, f in enumerate(fields):
    make_label(f, i)

# =========================
# UPDATE LOOP
# =========================
def update():
    global pitch, roll, yaw, prev

    now = time.time()
    dt = now - prev
    prev = now

    # ACCEL
    ax_g, ay_g, az_g = get_accel()

    # Convert to m/s²
    ax = ax_g * g
    ay = ay_g * g
    az = az_g * g

    # ANGLES FROM ACCEL
    pitch_raw, roll_raw = get_angles(ax_g, ay_g, az_g)

    # APPLY CALIBRATION OFFSET
    pitch_corr = normalize(pitch_raw - pitch_offset)
    roll_corr  = normalize(roll_raw  - roll_offset)

    # GYRO YAW
    _, _, gz = get_gyro()
    gz -= gz_offset
    yaw += gz * dt
    yaw = normalize(yaw)

    # UPDATE GUI
    labels["Ax (m/s²)"].config(text=f"{ax:.2f}")
    labels["Ay (m/s²)"].config(text=f"{ay:.2f}")
    labels["Az (m/s²)"].config(text=f"{az:.2f}")

    labels["Pitch (deg)"].config(text=f"{pitch_corr:.2f}")
    labels["Roll (deg)"].config(text=f"{roll_corr:.2f}")
    labels["Yaw (deg)"].config(text=f"{yaw:.2f}")

    root.after(50, update)

# START
update()
root.mainloop()
