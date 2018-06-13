import network
import time
import socket
import usocket
import http_client


# setup as a station
def connectWifi(SSID = 'LANTERN', PASS ='electric'):
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.connect(SSID, auth=(network.WLAN.WPA2, PASS))
    while not wlan.isconnected():
        time.sleep_ms(50)
    print(wlan.ifconfig())

def do_connect(SSID = 'LANTERN', PASS ='electric'):
    sta_if = network.WLAN(mode=network.WLAN.STA)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID,PASS)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo('www.lantern.tech', 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

connectWifi()
#do_connect()
#http_get('http://micropython.org/ks/test.html')

r = http_client.get('http://micropython.org/ks/test.html')
r.raise_for_status()
print(r.status_code)
print(r.text)  # r.content for raw bytes


r = http_client.post('https://api-test.hunt-r.tech/thingworx/availability/shifts', json={"time_zone": "America/CostaRica","start_date": 0,"end_date": 2})
print(r.json())
