import  time
from    machine  import  I2C
import    PCF8591



i2c = I2C(0, I2C.MASTER, baudrate=100000)
adcModule = PCF8591.PCF8591(i2c, addr=i2c.scan()[0])
sample = 0
while True:
    dataread = adcModule.read(PCF8591.ACHNNL0)
    time.sleep(1)
    print("Sample "+str(sample))
    print(dataread)
    sample+=1



#i2c.writeto(0x70, 'hello') # send 5 bytes to slave with address 0x42
#i2c.readfrom(0x42, 5) # receive 5 bytes from slave
#i2c.readfrom_mem(0x42, 0x10, 2) # read 2 bytes from slave 0x42, slave memory 0x10
#i2c.writeto_mem(0x42, 0x10, 'xy') # write 2 bytes to slave 0x42, slave memory 0x10
