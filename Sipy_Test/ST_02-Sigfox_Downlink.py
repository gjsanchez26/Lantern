from    network   import Sigfox
import  socket
import  binascii

sigfoxDevice     = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)      # init Sigfox for RCZ4 (Costa Rica/Americas)
sigfoxSocket     = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW) # create a Sigfox socket
deviceID         = binascii.hexlify(sigfoxDevice.id())              # get device ID
devicePAC        = binascii.hexlify(sigfoxDevice.pac())             # get device PAC

sigfoxSocket.setblocking(True)                                      # make the socket blocking
sigfoxSocket.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)      # #Uplink + Downlink : Send then receive a reply


print("Device %s is asking for downlink" % deviceID)

outputMessage    = sigfoxSocket.send(bytes([0x0F]))                 # send some bytes as an uplink message (mandatory)
inputMessage     = sigfoxSocket.recv(8)                             # reveive the dowlink message

print("Downlink response is %s" % binascii.hexlify(inputMessage))
