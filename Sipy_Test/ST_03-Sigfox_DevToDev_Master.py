from    network import Sigfox
import  socket
import  time
import  pycom
import  binascii

pycom.heartbeat(False)

sigfoxDevice = Sigfox(mode=Sigfox.FSK, frequency=920800000)         #Set transmision frequency
sigfoxSocket = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)     # create a Sigfox socket

deviceID         = binascii.hexlify(sigfoxDevice.id())              # get device ID
devicePAC        = binascii.hexlify(sigfoxDevice.pac())             # get device PAC

sigfoxSocket.setblocking(True)

num = 0

while True:
  #sigfoxSocket.send(deviceID)

  print("Message ID: " + str(num) + " receiving from " + str(sigfoxSocket.recv(64)))
  time.sleep(1)
  num = num + 1
