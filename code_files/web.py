from flask import Flask, jsonify, render_template, request
import smbus2
import board
import adafruit_dht
import RPi.GPIO as GPIO
import datetime
import time

app = Flask(__name__)

# --- Hardware Setup ---
MPU_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
bus = smbus2.SMBus(1)
bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)

dht_sensor = adafruit_dht.DHT11(board.D4)

GAS_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# --- State Management ---
THRESHOLDS = {
    "accel_x": 4.5,
    "accel_y": 2.5,
    "accel_z": 3.0,
    "temp": 32.0,
    "humidity": 65.0,
    "aqi": 50.0  # Kept for UI compatibility
}

def read_raw_data(addr):
    try:
        high = bus.read_byte_data(MPU_ADDR, addr)
        low = bus.read_byte_data(MPU_ADDR, addr + 1)
        value = (high << 8) | low
        return value - 65536 if value > 32768 else value
    except:
        return 0

def get_live_data():
    ts = datetime.datetime.now().strftime("%I:%M:%S %p")

    # 1. Acceleration
    ax = read_raw_data(ACCEL_XOUT_H) / 16384.0
    ay = read_raw_data(ACCEL_XOUT_H + 2) / 16384.0
    az = read_raw_data(ACCEL_XOUT_H + 4) / 16384.0

    # 2. Temperature & Humidity (DHT11 is sensitive to timing)
    try:
        temp = dht_sensor.temperature
        hum = dht_sensor.humidity
    except (RuntimeError, Exception):
        temp, hum = 0.0, 0.0

    # 3. Gas Sensor (Digital State)
    gas_state = GPIO.input(GAS_PIN)
    # Convert digital LOW (smoke detected) to a high AQI number for the UI scale
    aqi_sim = 95.0 if gas_state == GPIO.LOW else 15.0

    # 4. Logic for Risk
    risk_level = 5
    if abs(ax) > THRESHOLDS["accel_x"] or abs(ay) > THRESHOLDS["accel_y"]:
        risk_level = 98

    return {
        "timestamp": ts,
        "accel_x": round(ax, 2),
        "accel_y": round(ay, 2),
        "accel_z": round(az, 2),
        "temp": temp or 0.0,
        "humidity": hum or 0.0,
        "aqi": aqi_sim,
        "risk": risk_level,
        "thresholds": THRESHOLDS
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_sensor_data():
    return jsonify(get_live_data())

@app.route('/api/thresholds', methods=['POST'])
def update_thresholds():
    global THRESHOLDS
    data = request.json
    mapping = {
        "thr-accel-x": "accel_x",
        "thr-accel-y": "accel_y",
        "thr-temp": "temp",
        "thr-humidity": "humidity",
        "thr-aqi": "aqi"
    }
    for html_id, key in mapping.items():
        if html_id in data and data[html_id] != "":
            THRESHOLDS[key] = float(data[html_id])
    return jsonify({"status": "success"})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    finally:
        dht_sensor.exit()
        GPIO.cleanup()
