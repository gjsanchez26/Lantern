import  time
from    machine  import  I2C
import  PCF8591
import  binascii

i2c         = I2C(0, I2C.MASTER, baudrate=100000)
adcModule   = PCF8591.PCF8591(i2c, addr=i2c.scan()[0])  # Initializate module with library
sample      = 0


while True:
    dataread = adcModule.read(PCF8591.ACHNNL0)          # read from A0
    time.sleep(1)                                       # sample time
    print("Sample "+str(sample))                        #
    print(dataread)                                     # print read data
    sample+=1

''' TEST WITH NO LIBRARY
while True:
    dataread = i2c.readfrom(0x48, 1)                    # receive 1 bytes from slave
    time.sleep(1)                                       # sample time
    print("Sample "+str(sample))
    test = int(binascii.hexlify(dataread),16)           #
    print(str(test))                                    # print read data
    sample+=1
'''
