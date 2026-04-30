from gpiozero import Device
from gpiozero.pins.lgpio import LGPIOFactory
import time

# Use lgpio backend
Device.pin_factory = LGPIOFactory()

from gpiozero import DHT11

sensor = DHT11(17)   # GPIO17

while True:
    try:
        temp = sensor.temperature
        hum = sensor.humidity

        if temp is not None and hum is not None:
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {hum}%")
            print("----------------------")
        else:
            print("Retrying...")

    except Exception as e:
        print("Error:", e)

    time.sleep(2)