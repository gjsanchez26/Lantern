import network
import time
import socket
import http_client


# setup as a station
def connectWifi(SSID = 'LANTERN', PASS ='electric'):
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.connect(SSID, auth=(network.WLAN.WPA2, PASS))
    while not wlan.isconnected():
        time.sleep_ms(50)
    print(wlan.ifconfig())

def do_connect(SSID = 'LANTERN', PASS ='electric'):
    wlan = network.WLAN(mode=network.WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        if net.ssid == SSID:
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec,PASS ), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print('WLAN connection succeeded!')
            break

#connectWifi()
do_connect()
#http_get('http://micropython.org/ks/test.html')

#r = http_client.post('https://api-test.hunt-r.tech/thingworx/availability/shifts', json={"time_zone": "America/CostaRica","start_date": 0,"end_date": 2})
#r = http_client.post('https://iot.lantern.tech/api/v1/sg1Ul5mQZxBCSndtqVuY/telemetry',json={"Device": "4D5490","Temperature": 25,"Humidity": 50})
r2 = http_client.post('https://iot.lantern.tech/api/v1/sg1Ul5mQZxBCSndtqVuY/telemetry',json={"Device": "4D5490","Temperature": 30,"Humidity": 75})


#print(r.json())
'''
r = http_client.get('http://micropython.org/ks/test.html')
r.raise_for_status()
print(r.status_code)
print(r.text)  # r.content for raw bytes
'''
