from   network import WLAN
import time
import socket
import http_client

ssid        = "LANTERN"
password    = "electric"
wlan        = WLAN(mode=WLAN.STA)
temperature = 100
humidity    = 100
status      = False

# setup as a station
def connectWifi(SSID=ssid,PASS=password):
    wlan.connect(SSID, auth=(WLAN.WPA2, PASS))
    while not wlan.isconnected():
        time.sleep_ms(50)
    print(wlan.ifconfig())


def wlanPost(URL,JSON):
    response = http_client.post(URL,json=JSON)
    print("POST response: " + str(response.status_code))
    return response

def wlanGet(URL):
    r = http_client.get(URL)
    r.raise_for_status()
    print("GET response: " + str(r.status_code))
    #print(r.text)

def do_connect(SSID = 'LANTERN', PASS ='electric'):
    sta_if = WLAN(mode=WLAN.STA)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID,PASS)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


connectWifi()

while True:
    #wlanGet('http://micropython.org/ks/test.html')
    wlanPost('https://iot.lantern.tech/api/v1/sg1Ul5mQZxBCSndtqVuY/telemetry', {"Device": "4D5490","Temperature": temperature,"Humidity": humidity})
    time.sleep(20)
    temperature += 3
    humidity += 5
