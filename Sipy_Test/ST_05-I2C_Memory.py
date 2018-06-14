import  time
from    machine  import  I2C
import  PCF8591
import  binascii

i2c         = I2C(0, I2C.MASTER, baudrate=100000)
adcModule   = PCF8591.PCF8591(i2c, addr=i2c.scan()[0])  # Initializate module with library
sample      = 0


while True:
        dataread = i2c.readfrom_mem(0x42, 0x10, 2)          # read 2 bytes from slave 0x42, slave memory 0x10)
    time.sleep(1)                                       # sample time
    print("Sample "+str(sample))
    test = int(binascii.hexlify(dataread),16)           #
    print(str(test))                                    # print read data
    sample+=1
