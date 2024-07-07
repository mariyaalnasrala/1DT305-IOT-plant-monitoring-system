import time
import ubinascii
import machine
from mqtt import MQTTClient
from machine import ADC, Pin

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "your_aio_user"
AIO_KEY = "your_aio_key"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()
AIO_SOIL_FEED = "your_aio_soil_feed"
AIO_LIGHTS_FEED = "your_aio_lights_feed"


# Variables
RANDOMS_INTERVAL = 900000  # milliseconds
last_random_sent_ticks = 0

# Sensor setup
soil_sensor = ADC(Pin(27))  # Soil Moisture Sensor
light_sensor = ADC(Pin(26))  # Light Sensor

# Calibration values
moist_wet = 13347  # Value for wet soil
moist_dry = 42986  # Value for dry soil


# Callback function for responding to messages from Adafruit IO
def sub_cb(topic, msg):
    print((topic, msg))


# Functions to collect and send data
def send_data():
    global last_random_sent_ticks
    if (time.ticks_ms() - last_random_sent_ticks) < RANDOMS_INTERVAL:
        return  # Too soon since last one sent

    moist, light = measure_data()
    try:
        client.publish(topic=AIO_SOIL_FEED, msg=str(moist))
        client.publish(topic=AIO_LIGHTS_FEED, msg=str(light))
        print("Data sent to Adafruit IO")
    except Exception as e:
        print("client.publish() - FAILED:", str(e))
    finally:
        last_random_sent_ticks = time.ticks_ms()


def measure_data():
    moisture_raw = soil_sensor.read_u16()
    light_raw = light_sensor.read_u16()

    # Convert raw moisture value to percentage
    moisture = max(0, min(100, (moist_dry - moisture_raw) * 100 / (moist_dry - moist_wet)))

    # Convert raw light value to percentage
    light = max(0, min(100, light_raw * 100 / 65535))

    # Adjust the moisture and light values based on the ranges
    # Range: 20-80%
    moisture = max(0, min(100, (moisture - 20) * 100 / 60))
    # Range: 40-80%
    light = max(0, min(100, (light - 40) * 100 / 40))

    print("\nSoil moisture is {}% \nLight intensity is {}%\n".format(moisture, light))
    return moisture, light


# Connect to Adafruit IO using MQTT
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
client.set_callback(sub_cb)
client.connect()
client.subscribe(AIO_LIGHTS_FEED)
print("Connected to %s, subscribed to %s and %s topics" % (AIO_SERVER, AIO_SOIL_FEED, AIO_LIGHTS_FEED))

try:
    while True:
        client.check_msg()
        send_data()
        time.sleep(900)
except Exception as e:
    print("An error occurred:", str(e))
finally:
    client.disconnect()
    client = None
    print("Disconnected from Adafruit IO.")
