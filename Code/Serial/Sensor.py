import serial

class Sensor :

    def __init__(self, speed_ms):
        self.ser = serial.Serial() 
        self.ser.port = 3

        while not self.ser.isOpen() :
            try :
                self.ser.open()
            except :
                if self.ser.port == 3 :
                    self.ser.port = 2 #Aina
                else :
                    self.ser.port = 3 #Sam

        print("start program")
        length = self.ser.inWaiting()
        self.startGS(speed_ms)
        
        
    #Read the data (string) from Sensor S
    def reader(self):
        out = '' 
        length = self.ser.inWaiting()
        out = self.ser.read(length)
        return out
       
    #return the data from sensor S (GS,ACC,Others)
    #The data are in string format (of real number)
    def getData(self):
        
        #From first data exchange of the sensor :
        #Format pour le GSR: g,timestamp [ms],gsr-value [??]
        #Format pour l'accelerometre: a,timestamp [ms],axe-x [g],axe-y [g],axe-z [g]   
        GS = [] 
        ACC = []
        Others = []
        AllData = self.reader() #string with all data
        
        #sort the data into the 3 list GS,ACC and Others
        AllDataSplit = AllData.splitlines()
        for l in AllDataSplit:
            if l[0:2] == 'g,': #GSR Data
                
                DataG = l.split(',')
                if len(DataG) == 3:
                    DataGname = DataG[0]
                    DataGTime = DataG[1]
                    DataGS = DataG[2]
                    GS.append([DataGTime,DataGS])
                
            elif l[0:2] == 'a,': #Accelerometer Data
                DataA = l.split(',')
                if len(DataA) == 5:
                    DataAname = DataA[0]
                    DataATime = DataA[1]
                    DataAx = DataA[2]
                    DataAy = DataA[3]
                    DataAz = DataA[4]
                    ACC.append([DataATime,DataAx,DataAy,DataAz])
            else:
                Others.append(l)
        
        return [GS,ACC,Others]


    #Send stop command
    def stopGS(self):
        self.ser.write('gstop\n')
        self.ser.close()
        
    #Start the device, with ms period aquisition 
    def startGS(self,ms):
        msg = 'gstartf ' + str(ms) + '\n'
        self.ser.write(msg)
