import smbus
import time
bus=smbus.SMBus(1)
address=0x12
data=""
value=""

while True:
    value=bus.read_i2c_block_data(address,0)
    for i in range(0,len(value)):
        data+=chr(value[i]);
    print data
    time.sleep(1);
