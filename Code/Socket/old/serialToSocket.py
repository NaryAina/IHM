import socket
import serial
import time

class Bridge:
    def __init__(self):
        self.initSocket()
        self.initSerial()
        self.start()
        self.close()
        
    def initSocket(self, host = '127.0.0.1', port = 12800):
        self.host = host
        self.port = port
        
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.connect((self.host, self.port))
            print("connection sucessfull")
        except Exception as inst:
            print("connection error")
            pass

    def initSerial(self, serialName = 'COM7', baudrate = 9600):
        self.serial = serial.Serial()
        self.serial.baudrate = baudrate
        self.serial.port = serialName
        self.serial.open()

        self.serial.write('gstartf 50' + '\n')
        

    def start(self):
        for i in range(0, 1200):
            length = self.serial.inWaiting()
            
            if length > 0:
                data = self.serial.read(length)
                print("send " + data)
                self.socket.send(data)
                
            time.sleep(0.050)

        
    def close(self):
        self.serial.write('gstop' + '\n')
        self.socket.close()
        self.serial.close()


Bridge()




