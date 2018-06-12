from network import Sigfox
import socket
import binascii

# init Sigfox for RCZ1 (Europe)
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

# send some bytes
#s.send("PuraVida")
