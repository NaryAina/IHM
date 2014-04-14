#Aina NARY ANDRIAMBELO
#Samuel CONSTANTINO
#Interface Homme-Machine : TP1 v2 (with data saving in a file this time)

import time

import Sensor
import ClientSocket

import lowpass
import movingAverage
  
Select_GSR = True

speed_ms = 75 #frequence de mesure en ms
sleepMeasure = 0.05 #frequence de mesure en s

maxMSG = 150

xG = list()
yG = list()
xA = list()
yA1 = list()
yA2 = list()
yA3 = list()

################
#Initialization#
################

#connect sensor
ser = Sensor.Sensor(speed_ms) 

#create socket client
socket = ClientSocket.ClientSocket("127.0.0.1", 5005)

################
#Get data#
################

#pour filter
queueY = []
queueLen = 20
for el in range(queueLen) :
    queueY.append(0)

i = 0
#while i < maxMSG: #a changer : tant que pas stop
while True: #a changer : tant que pas stop

    #Get the data
    DataReader = ser.getData()
    DataGS = DataReader[0]
    DataACC = DataReader[1]
    
    for g in range (len(DataGS)):
        try :
            #yG += [float(DataGS[g][1])]
            queueY.append(float(DataGS[g][1]))
            
            if len(queueY) > queueLen :
                queueY.pop(0)
            
            #yG += [lowpass.lowPass(queueY, 50, 50)]
            y = movingAverage.movingAverage(queueY)
            
            print y
            socket.envoyerMsg(str(y))
            #socket.envoyerMsg(str(0.1))
            
        except: #si bug et n'arrive pas a convertir string
            pass     
       
    #Accelerometer data??
    """
    for a in range(len(DataACC)):
        yA1 += [float(DataACC[a][1])]
        yA2 += [float(DataACC[a][2])]
        yA3 += [float(DataACC[a][3])]
        xA += [float(DataACC[a][0])]    
   
    plt.plot(xA,yA1,'r',axes=axplot,label='x ACC')
    plt.plot(xA,yA2,'g',axes=axplot,label='y ACC')
    plt.plot(xA,yA3,'b', axes=axplot,label='z ACC')
    
    indice = xA[len(xA)-1]
    if indice > limitA:
        plt.axis([indice-limitA,limitA+indice/2,yminA,ymaxA])
    else:
        plt.axis([xminA,xmaxA,yminA,ymaxA])

    plt.ion()
    plt.show()
    plt.draw()
    
    axplot.set_xlabel('temps (ms)')
    axplot.set_ylabel('Accelerometer values')
    """
    time.sleep(sleepMeasure)
    i+=1

ser.stopGS()
print ("end")