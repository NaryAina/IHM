import serial
import time
import StringIO

#Read the data (string) from Sensor S
def reader(S):
    out = '' 
    length = S.inWaiting()
    out = S.read(length)
    return out
   
#return the data from sensor S (GS,ACC,Others)
#The data are in string format (of real number)
def getData(S):
    #####
    #From first data exchange of the sensor :
    #Format pour le GSR: g,timestamp [ms],gsr-value [??]
    #Format pour l'accelerometre: a,timestamp [ms],axe-x [g],axe-y [g],axe-z [g]
    #####
    GS = [] #timeSt
    ACC = []
    Others = []
    AllData = reader(S) #string avec toute les donnees
    AllDataSplit = AllData.splitlines()
    for l in AllDataSplit:
        if l[0:2] == 'g,': #GS Data
            DataG = l.split(',')
            DataGname = DataG[0]
            DataGTime = DataG[1]
            DataGS = DataG[2]
            GS.append([DataGTime,DataGS])
            
        elif l[0:2] == 'a,': #Accelerometer Data
            DataA = l.split(',')
            DataAname = DataA[0]
            DataATime = DataA[1]
            DataAx = DataA[2]
            DataAy = DataA[3]
            DataAz = DataA[4]
            ACC.append([DataATime,DataAx,DataAy,DataAz])
        else:
            Others.append(l)
    
    return [GS,ACC,Others]


#Arreter le device s
def stopGS(S):
    S.write('gstop\n')
    
#Demarrer le device s, mesurer tout les ms milliseconde
def startGS(S,ms):
    msg = 'gstartf ' + str(ms) + '\n'
    S.write(msg)
 
AllDataGS = []
AllDataACC = []   
ser = serial.Serial()
ser.port = 2
ser.timeout = 1

speed_ms = 50 #frequence de mesure en ms
sleep = 0.05 #frequence de mesure en s
#ser.open()
ser = serial.Serial(2)

print("start program")
length = ser.inWaiting()
startGS(ser,speed_ms)

#test de lecture de x Message
x = 0
maxMSG = 10
while x < maxMSG:
    #print("----------------\n")
    DataReader = getData(ser)
    DataGS = DataReader[0]
    DataACC = DataReader[1]
    for g in DataGS:
        AllDataGS.append(g)
    for a in DataACC:
        AllDataACC.append(a)
    x += 1
    time.sleep(sleep)

#test : voir les donnee recuperer
print "\nDonne GS : \n"
for g in AllDataGS:
    print g

print "\nDonne ACC : \n"
for a in AllDataACC:
    print a

    
stopGS(ser)
ser.close()
print ("end")