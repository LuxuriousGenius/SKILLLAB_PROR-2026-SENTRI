from flask import Flask, jsonify, render_template, request
import smbus2
import board
import adafruit_dht
import RPi.GPIO as GPIO
import datetime
import time

app = Flask(__name__)

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

dht_sensor = adafruit_dht.DHT11(board.D4)

GAS_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

THRESHOLDS = {
    "accel_x": 4.5,
    "accel_y": 2.5,
    "temp": 32.0,
    "humidity": 65.0
}

def get_live_data():
    timestamp_log = datetime.datetime.now().strftime("%I:%M:%S %p")

    try:
        ax = read_raw_data(ACCEL_XOUT_H) / 16384.0
        ay = read_raw_data(ACCEL_XOUT_H + 2) / 16384.0
        az = read_raw_data(ACCEL_XOUT_H + 4) / 16384.0
    except:
        ax, ay, az = 0.0, 0.0, 0.0

    try:
        temp = dht_sensor.temperature
        hum = dht_sensor.humidity
    except RuntimeError:
        temp, hum = 0.0, 0.0

    gas_state = GPIO.input(GAS_PIN)
    smoke_status = "DANGER" if gas_state == GPIO.LOW else "SAFE"

    risk_level = 5
    if abs(ax) > THRESHOLDS["accel_x"] or abs(ay) > THRESHOLDS["accel_y"]:
        risk_level = 98

    print(f"[{timestamp_log}] LIVE -> AccelX: {ax:.2f}g | Temp: {temp}°C | Smoke: {smoke_status}")

    return {
        "accel_x": round(ax, 2),
        "accel_y": round(ay, 2),
        "temp": temp or 0.0,
        "humidity": hum or 0.0,
        "smoke_status": smoke_status,
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
        "thr-hum": "humidity"
    }
    for html_id, key in mapping.items():
        if html_id in data and data[html_id] != "":
            THRESHOLDS[key] = float(data[html_id])
    return jsonify({"status": "success", "updated": THRESHOLDS})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        dht_sensor.exit()
        GPIO.cleanup()
