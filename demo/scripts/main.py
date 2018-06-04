from network import Sigfox
import socket
import time
import pycom
import binascii
pycom.heartbeat(False)
time.sleep(5)


# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

print('I am device ',  binascii.hexlify(sigfox.mac()) )

msg_str = "0"
sigfox.reset()
s.send(msg_str)
pycom.rgbled(0xFFFFFF)
time.sleep(20)

pycom.rgbled(0x0)


# send some bytes
