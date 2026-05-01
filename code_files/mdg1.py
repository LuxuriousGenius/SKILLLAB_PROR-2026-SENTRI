import smbus2
import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
import datetime

# ------------------ MPU6050 सेटअप ------------------
MPU_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

bus = smbus2.SMBus(1)
bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)

def read_raw_data(addr):
    high = bus.read_byte_data(MPU_ADDR, addr)
    low = bus.read_byte_data(MPU_ADDR, addr + 1)
    value = (high << 8) | low
    if value > 32768:
        value -= 65536
    return value

# ------------------ DHT11 सेटअप ------------------
dht = adafruit_dht.DHT11(board.D4)

# ------------------ Gas Sensor सेटअप ------------------
GAS_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# ------------------ Startup Info ------------------
print("=" * 40)
print(" SAFEDRIVE SENTINEL: GAS MONITORING ")
print("=" * 40)
print(f"Initializing Gas Sensor on GPIO {GAS_PIN}...")
print("Wait ~30 seconds for gas sensor warmup...")
time.sleep(5)  # increase to 30 in real use

# ------------------ MAIN LOOP ------------------
try:
    while True:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        # ---- MPU6050 ----
        acc_x = read_raw_data(ACCEL_XOUT_H)
        acc_y = read_raw_data(ACCEL_XOUT_H + 2)
        acc_z = read_raw_data(ACCEL_XOUT_H + 4)

        Ax = acc_x / 16384.0
        Ay = acc_y / 16384.0
        Az = acc_z / 16384.0

        # ---- DHT11 ----
        try:
            temperature = dht.temperature
            humidity = dht.humidity
        except RuntimeError:
            temperature = None
            humidity = None

        # ---- Gas Sensor ----
        gas_state = GPIO.input(GAS_PIN)

        # ---- OUTPUT ----
        print("\n" + "-" * 40)
        print(f"[{timestamp}] SENSOR DATA")

        # DHT Output
        if temperature is not None and humidity is not None:
            print(f"Temperature: {temperature}°C | Humidity: {humidity}%")
        else:
            print("DHT11 read failed")

        # MPU Output
        print(f"Acceleration -> Ax: {Ax:.2f}g Ay: {Ay:.2f}g Az: {Az:.2f}g")

        # Gas Output
        if gas_state == GPIO.LOW:
            print(" ALERT: Gas/Smoke Detected! [DANGER]")
        else:
            print(" Air Quality: Normal [SAFE]")

        time.sleep(2)

# ------------------ CLEAN EXIT ------------------
except KeyboardInterrupt:
    print("\nStopping Monitor...")

finally:
    print("Cleaning up GPIO and sensors...")
    dht.exit()          # IMPORTANT
    GPIO.cleanup()
    print("System safely shut down.")
