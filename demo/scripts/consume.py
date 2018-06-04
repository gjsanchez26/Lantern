from network import Sigfox
import socket
import binascii
import pycom
import time
from pysense import Pysense
from LTR329ALS01 import LTR329ALS01

pycom.heartbeat(False)

sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

print('I am device ',  binascii.hexlify(sigfox.id()), binascii.hexlify(sigfox.pac()) )


 # send some bytes
s.send("Hello World")

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)


py = Pysense()
lt = LTR329ALS01(py)


print("Hello World Ligth")

tuple           = (20,10)
index           = 0
pricePerTime    = 10
firstAdvice     = 500
secondAdvice    = 1000
thirdAdvice     = 1500

while True:

    sample = lt.light()
    time.sleep(0.2)
    if ( sample > tuple):
        print("light ON")
        index = index+1
        price = index*pricePerTime
        msg = 'daily consumption: ' + str(price)
        print (msg)
        if(price == firstAdvice):
            print("You have consume 1000 colones")
            s.send("500")
        if(price == secondAdvice):
            print("You have consume 2000 colones be carefull")
            s.send("1000")
            pycom.rgbled(0xFFFFF)
        if(price == thirdAdvice):
            print("You have consume 3000 colones Are you crazy?")
            s.send("1500")
            pycom.rgbled(0x000000)
    else:
        print("light OFF")
      # Red
