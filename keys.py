
import ubinascii
import machine

# Wireless network
WIFI_SSID = "your_wifi_ssid"
WIFI_PASS = "your_wifi_password"

# Adafruit IO (AIO) configuration.
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "your_aio_user"
AIO_KEY = "your_aio_key"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()
# Convert to string
AIO_SOIL_FEED = "your_user/feeds/soil"
AIO_LIGHTS_FEED = "your_user/feeds/sunlight"
AIO_RANDOMS_FEED = "your_user/feeds"

