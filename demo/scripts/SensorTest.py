import socket
import time
import binascii
import pycom

from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2, ALTITUDE, PRESSURE
from network import Sigfox

py      = Pysense()
si      = SI7006A20(py)
lt      = LTR329ALS01(py)
li      = LIS2HH12(py)
mp      = MPL3115A2(py,mode=ALTITUDE)
mpPress = MPL3115A2(py,mode=PRESSURE)

# Disable heartbeat LED
pycom.heartbeat(False)



def getPressure():
    print('Pressure (hPa)', mpPress.pressure()/100)
    return int(mpPress.pressure()/100)

def getAltitude():
    altitude=mp.altitude()
    print("Altitude raw data")
    print(altitude)
    print(".......")
    return int(altitude)

def getHumidity():
    humidity=si.humidity()
    print("Humidity raw data")
    print(humidity)
    print(".......")
    return int(humidity)

def getTemp():
    temperature=si.temperature()
    print("Temp raw data")
    print(temperature)
    print(".......")
    return int(temperature)


sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# print Sigfox Device ID
print("ID: ", binascii.hexlify(sigfox.id()))
# print Sigfox PAC number
print("PAC: ", binascii.hexlify(sigfox.pac()))

 # make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
msgNumber = 0
print("Start...")
while True:
    temperature = getTemp()
    humidity    = getHumidity()
    #altitude    = getAltitude()
    #pressure    = getPressure()
    s.send(bytes([temperature - 10, humidity]))
    print("Successfully send data to Sigfox...")
    print("Sample number" + str(msgNumber))
    msgNumber = msgNumber+1
    time.sleep(120)
