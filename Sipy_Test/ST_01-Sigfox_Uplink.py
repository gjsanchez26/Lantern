from    network   import Sigfox
import  socket
import  binascii

sigfoxDevice     = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)      # init Sigfox for RCZ4 (Costa Rica/Americas)
sigfoxSocket     = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW) # create a Sigfox socket
deviceID         = binascii.hexlify(sigfoxDevice.id())              # get device ID
devicePAC        = binascii.hexlify(sigfoxDevice.pac())             # get device PAC

sigfoxSocket.setblocking(True)                                      # make the socket blocking
sigfoxSocket.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)      # configure it as uplink only
#
#send some bytes

print("Device is ready to send message")

sigfoxSocket.send(bytces([0x48, 0x65, 0x6C,  0x6C, 0x6F, 0x20, 0x50, 0x79, 0x63, 0x6F, 0x6D, 0x21]))

print("Device %s have sent a message" % deviceID)
