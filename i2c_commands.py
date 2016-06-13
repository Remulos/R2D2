import smbus
import time
bus=smbus.SMBus(1)

#initialize variables
pin = "" #holds the pin number 0-13 or A0-A3
pinType = "" #hol,ds the pin type: INPUT, OUTPUT, INPUT_PULLUP
mode = "" #holds the pinmode: HIGH, LOW, PWM
pwmValue = "" #h,olds the pwmValue
pwm = "" #holds the pwmValue in 3 digits
val = "" #holds, a String to be converted into ASCII
cmd = "" #holds the first byte of the message for the arduino
message = "" #,holds the second - seventh byte of the message for the arduino
valCmd = 88 #holds the command as ASCII value 88 = "X"
valMessage = [88,88,88,88,88,88] #holds the message as ASCII values
address = "" #holds the slave address


#this routine sends a setPin command to the arduino to make a pin INPUT, OUTPUT or INPUT_PULLUP

def setPin(address, pin, pinType):
        cmd = "S"
        message = pinString(pin)+pinType[0]+"000"
        sendMessage(address, cmd, message)

def writePin(address, pin, mode):
        cmd = "W"
        message = pinString(pin)+mode[0]+ "000"
        sendMessage(address, cmd, message)

def analogWritePin(address, pin, pwmValue):
        cmd = "A"
        message = pinString(pin)+"X"+pwmString(pwmValue)
        sendMessage(address, cmd, message)

#this sends a reset command to the arduino

def pinReset(address):
        setPin(address,"00","Output")
        setPin(address,"01","Output")
        setPin(address,"02","Output")
        setPin(address,"03","Output")
        setPin(address,"04","Output")
        setPin(address,"05","Output")
        setPin(address,"06","Output")
        setPin(address,"07","Output")
        setPin(address,"08","Output")
        setPin(address,"09","Output")
        setPin(address,"10","Output")
        setPin(address,"11","Output")
        setPin(address,"12","Output")
        setPin(address,"13","Output")
        setPin(address,"A0","Output")
        setPin(address,"A1","Output")
        setPin(address,"A2","Output")
        setPin(address,"A3","Output")


#this routine converts Strings to ASCII code

def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal



#this routine actually transmits the command
#sleep is required in order to prevent a request overload on the arduino

def sendMessage(address, cmd, message):
        cmd = cmd.upper()
        message = message.upper()
        valCmd = ord(cmd)
        valMessage = StringToBytes(message)
        print("Message: " + cmd + message + " send to address " + str(address))
        bus.write_i2c_block_data(address, valCmd, valMessage)
        time.sleep(0.03)



#this routine sends a request to the Arduino to provide a 30 byte status update, return all 30 bytes

def getStatus (address):
        status=""
        for i in range(0,30):
                status += chr(bus.read_byte(address))
                time.sleep(0.05);
        #time.sleep(0.01)
        return status
                


#this routine sends a request to the Arduino to provide a 30 byte status update, return the value of a single pin

def pinValue(address, pin):
                status = ""
                
                for i in range(0,30):
                        status += chr(bus.read_byte(address))
                        time.sleep(0.05);
                pinvalues = {   '0':status[0],
                                '1':status[1], 
                                '2':status[2], 
                                '3':status[3], 
                                '4':status[4], 
                                '5':status[5], 
                                '6':status[6], 
                                '7':status[7], 
                                '8':status[8], 
                                '9':status[9], 
                                '10':status[10], 
                                '11':status[11], 
                                '12':status[12], 
                                '13':status[13],
                                'A0':int(status[14]+status[15]+status[16]+status[17])-1000,
                                'A1':int(status[18]+status[19]+status[20]+status[21])-1000,
                                'A2':int(status[22]+status[23]+status[24]+status[25])-1000,
                                'A3':int(status[26]+status[27]+status[28]+status[29])-1000}
                time.sleep(0.1)
                return pinvalues[pin]




#this routine converts a 1 or 2 digit pin into a 2 digit equivalent

def pinString(pin):
        while len(pin)<2:
                pin = "0"+pin;
        return pin




#this routine converts a 1, 2 or 3 digit pin into a 3 digit equivalent

def pwmString(pwmValue):
        if len(pwmValue)<3 and len(pwmValue)>1:
                pwmValue = "0"+pwmValue;
        if len(pwmValue)<2:
                pwmValue = "00"+pwmValue;
        return pwmValue

#this routine will set all pins to output to start the program

def pinResetAll(address):
        #pinReset(0x12)
        pinReset(0x14)
        pinReset(0x16)
        pinReset(0x18)
        pinReset(0x1a)
        #pinReset(0x1c)

#this routine gets the status from all devices

def getStatusAll(address):
        #print("Status of ox12 is "+getStatus(0x12))
        print("Status of 0x14 is "+getStatus(0x14))
        print("Status of 0x18 is "+getStatus(0x16))
        print("Status of 0x18 is "+getStatus(0x18))
        print("Status of 0x1a is "+getStatus(0x1a))
        #print("Status of 0x1c is "+getStatus(0x1c))

#communication test

def testAll(address):
        #writePin(0x12,"13","High")
        #writePin(0x12,"13","Low")
        writePin(0x14,"13","High")
        writePin(0x14,"13","Low")
        writePin(0x16,"13","High")
        writePin(0x16,"13","Low")
        writePin(0x18,"13","High")
        writePin(0x18,"13","Low")
        writePin(0x1a,"13","High")
        writePin(0x1a,"13","Low")
        #writePin(0x1c,"13","High")
        #writePin(0x1c,"13","Low")

def testAll2(address):
        #writePin(0x12,"13","High")
        writePin(0x14,"13","High")
        writePin(0x16,"13","High")
        writePin(0x18,"13","High")
        writePin(0x1a,"13","High")
        #writePin(0x1c,"13","High")
        #writePin(0x12,"13","Low")
        writePin(0x14,"13","Low")
        writePin(0x16,"13","Low")
        writePin(0x18,"13","Low")
        writePin(0x1a,"13","Low")
        #writePin(0x1c,"13","Low")
