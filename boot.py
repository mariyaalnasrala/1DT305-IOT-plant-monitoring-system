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


def http_get(url='http://detectportal.firefox.com/'):
    import socket
    import time
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /{} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(path, host), 'utf8'))
    time.sleep(1)
    rec_bytes = s.recv(10000)
    print(rec_bytes)
    s.close()


try:
    ip = connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

try:
    http_get()
except (Exception, KeyboardInterrupt) as err:
    print("No Internet", err)
