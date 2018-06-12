from network import Sigfox
import socket
import time
import pycom

pycom.heartbeat(False)

sigfox = Sigfox(mode=Sigfox.FSK, frequency=920800000)
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)

num = 0

while True:
  s.send('Device-1')
  time.sleep(10)
  print("Message ID: " + str(num) + " receiving from " + str(s.recv(64)))
  num = num + 1
