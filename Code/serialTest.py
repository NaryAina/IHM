import serial

for i in range(0, 255):
    try:
        ser = serial.Serial()
        ser.port = i
        #ser.baudrate = 9600
        ser.open()
        ser.close()
        print "port disponible : " + ser.name
    except:
        i

""" 
ser = serial.Serial(2)

while not ser.isOpen():
    i = 0
    
ser.write("startf 1000")
ser.write("info")
i = 0
while i < 1000000:
    i = i + 1   
    length = ser.inWaiting()
    if length > 0:
        print ser.read(length)

        
ser.write("stop")
ser.close()
"""
