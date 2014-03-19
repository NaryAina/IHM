import serial
import time
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

global AllDataGS
global AllDataACC   
global GS_X
global Continu
global Select_GSR

class Index:
    ind = 0
    def Start(self, event):
        print "start"

    def Stop(self, event):
        print "stop"
        
    def Select(self, event):
        print "select"
        
    def Save(self, event):
        print "save"
        
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


#Arreter le device s
def stopGS(S):
    S.write('gstop\n')
    
#Demarrer le device s, mesurer tout les ms milliseconde
def startGS(S,ms):
    msg = 'gstartf ' + str(ms) + '\n'
    S.write(msg)


AllDataACC = []   
AllDataGS = []
ser = serial.Serial()
ser.port = 2
ser.timeout = 1

speed_ms = 50 #frequence de mesure en ms
sleep = 0.05 #frequence de mesure en s
#ser.open()


################
#Initialization#
################

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
    #print DataGS
    #print AllDataGS
    time.sleep(sleep)

#test : voir les donnee recuperer
# print "\nDonne GS : \n"
# for g in AllDataGS:
    # print g

# print "\nDonne ACC : \n"
# for a in AllDataACC:
    # print a

##############
# Plot Draw  #
##############

limit = 1000
maxMSG = 50
xmin = 0
xmax = 200
ymin = -1
ymax = 20
fig= plt.figure()

i=0
x=list()
y=list()

plt.ion()
plt.show()
#plt.axis([xmin,xmax,ymin,ymax])

#Draw buttons
callback = Index()
axstart = plt.axes([0.5, 0.05, 0.1, 0.075])
axstop = plt.axes([0.61, 0.05, 0.1, 0.075])
axselect = plt.axes([0.72, 0.05, 0.1, 0.075])
axsave = plt.axes([0.83, 0.05, 0.1, 0.075])
axplot = plt.axes([0.1,0.2,0.75,0.75])

bstart = Button(axstart, 'Start')
bstart.on_clicked(callback.Start)
bstop = Button(axstop, 'Stop')
bstop.on_clicked(callback.Stop)

bselect = Button(axselect, 'Select')
bselect.on_clicked(callback.Select)
bsave = Button(axsave, 'Save')
bsave.on_clicked(callback.Save)

while i < maxMSG: #a changer : tant que pas stop
    
    #Get the data
    DataReader = getData(ser)
    DataGS = DataReader[0]
    #print DataGS[0]
    DataACC = DataReader[1]
    for g in range (len(DataGS)):
        x += [float(DataGS[g][0])]
        y += [float(DataGS[g][1])]
        #AllDataGS.append(g[1])
        #GS_X.append(g[0])
    #for a in DataACC:
        #AllDataACC.append(a)
    
    #Plot the data
    GScur = 0
    temp_GS = AllDataGS

    # temp_y=math.sin(i)
    # x.append(i)
    # y.append(temp_y)
    plt.plot(x,y,'b', axes=axplot)
    i+=1
    indice = x[len(x)-1]
    if indice > limit:
        plt.axis([indice-limit,limit+indice,ymin,ymax])
        #plt.axis([0+i*0.5,3+i*0.5,-1,1])
    else:
        plt.axis([xmin,xmax,ymin,ymax])
        #plt.axis([0,3,-1,1])
    plt.ion()
    plt.show()
    

    
    plt.draw()
    
    plt.pause(0.05)
    print i
stopGS(ser)
ser.close()
print ("end")