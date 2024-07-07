import keys
import network
from time import sleep


def connect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.active(True)
        wlan.config(pm=0xa11140)
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)
        print('Waiting for connection...', end='')
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip


def disconnect():
    wlan = network.WLAN(network.STA_IF)
    wlan.disconnect()
    wlan.active(False)
    print("Disconnected from WiFi")
