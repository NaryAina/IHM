import serial
import time

def reader(s):
    out = ''
    while ser.inWaiting() > 0:
        out += s.read(1)
    if out != '':
        print out
    return out
 
def stopGS(s):
    s.write('gstop\n')
    
def startGS(s,ms):
    msg = 'gstartf ' + str(ms) + '\n'
    s.write(msg)
    
ser = serial.Serial()
ser.port = 2
ser.timeout = 1

#ser.open()
ser = serial.Serial(2)

print("start program")

#ser.write('ginfo\n')

time.sleep(2)
#line = reader(ser)
length = ser.inWaiting()
line = ser.read(length)


length = ser.inWaiting()
line = ser.read(length)

#ser.write('gstartf 50\n')
startGS(ser,50)
time.sleep(2)
ser.inWaiting()

# while ser.inWaiting() > 0:
    # out += ser.read(1)
# if out != '':
    # print out
x = 0
while x < 2:
    length = ser.inWaiting()
    line =ser.read(length)
    print("line : " + line)
    x += 1
    time.sleep(1)
stopGS(ser)
ser.close()
print ("end")