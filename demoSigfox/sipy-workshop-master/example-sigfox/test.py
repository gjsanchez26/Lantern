from network import WLAN
from network import Sigfox
import socket
import binascii

sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send some bytes


wlan = WLAN(mode = WLAN.STA)
list = []
nets = wlan.scan()
for net in nets:
    if "sipy" not in net.ssid:
        print(net.ssid)
        list.append(net.bssid)

print(binascii.hexlify(bytes(list[0])))
print(binascii.hexlify(bytes(list[1])))

print('\n\n** 3-Axis Accelerometer (LIS2HH12)')
print('Acceleration', li.acceleration())
print('Roll', li.roll())
print('Pitch', li.pitch())

print('Light', lt.light())
print('Humidity', si.humidity())
print('Temperature', si.temperature())
mpPress = MPL3115A2(py,mode=PRESSURE)
print('Pressure (hPa)', mpPress.pressure()/100)
mpAlt = MPL3115A2(py,mode=ALTITUDE)
print('Altitude', mpAlt.altitude())
print('Temperature', mpAlt.temperature())

#print (str(list[0]) + list[1])

#s.send(bytes(list[0]+list[1]))
