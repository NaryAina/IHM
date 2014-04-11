#Aina NARY ANDRIAMBELO
#Samuel CONSTANTINO
#Interface Homme-Machine : TP1 v2 (with data saving in a file this time)

import time
import math
from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import os

import Sensor

import lowpass
import movingAverage

global AllDataGS
global AllDataACC 
AllDataACC = []   
AllDataGS = []
  
Continu = False
Select_GSR = True

speed_ms = 75 #frequence de mesure en ms
sleep = 0.02 #frequence de mesure en s
GSR_file = "save_GSR.txt"
ACC_file = "save.ACC.txt"

maxMSG = 150
limitG = 15000 #inutile?
limitA = 15000

xminG = 0
xmaxG = 20000
yminG = -0.5
ymaxG = 15

xminA = 0
xmaxA = 20000
yminA = -5
ymaxA = 5

Starting = True
fig= plt.figure()

i = 0

xG = list()
yG = list()
xGtest = list()

xA = list()
yA1 = list()
yA2 = list()
yA3 = list()

class Index:
    ind = 0    
    def Start(self, event):
        global Continu
        Continu = True     

    def Stop(self, event):
        global Continu
        Continu = False
        
    def Select(self, event):
        global Select_GSR    

        Select_GSR = not(Select_GSR)
        
    def Save(self, event):
        global Continu
        global yG
        global yA1
        global yA2
        global yA3
        
        global xG
        global yG
        
        SavePNG("figSav", ext="png", close=False, verbose=True)
        
        #stop acquisition during saving
        Continu = False
        if Select_GSR:
            my_file = open(GSR_file,"w")
            my_file.write("GSR Data\n")
            for g in yG:
                
                my_file.write(str(g) + "\n")
            my_file.close()
        else:
            my_file = open(ACC_file,"w")
            my_file.write("x y z\n")
            for a in range(len(yA1)):
                my_file.write(str(yA1[a]) + " " + str(yA2[a])  + " " + str(yA3[a]) + "\n")
            my_file.close()
        Continu = True
        

################
#Initialization#
################

ser = Sensor.Sensor(speed_ms) 

##############
# Plot Draw  #
##############



plt.ion()
plt.show()

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
plt.plot([],[],'m', axes=axplot,label='GSR')
plt.plot([],[],'r',axes=axplot,label='x ACC')
plt.plot([],[],'g',axes=axplot,label='y ACC')
plt.plot([],[],'b', axes=axplot,label='z ACC')
legend = axplot.legend(loc='upper right', shadow=True)

#pour low pass filter
queueY = []
queueLen = 20
for i in range(queueLen) :
    queueY.append(0)

#while i < maxMSG: #a changer : tant que pas stop
while True: #a changer : tant que pas stop
    if Continu:
        #Get the data
        DataReader = ser.getData()
        i+=1
        DataGS = DataReader[0]
        DataACC = DataReader[1]
        if Select_GSR:  #select on
            for g in range (len(DataGS)):
                #Try a changer?
                try :
                    xG += [float(DataGS[g][0])]  
                except:
                    xG += [xG[-1]]
                try :
                    #yG += [float(DataGS[g][1])]
                    queueY.append(float(DataGS[g][1]))
                    
                    if len(queueY) > queueLen :
                        queueY.pop(0)
                    
                    #yG += [lowpass.lowPass(queueY, 50, 50)]
                    yG += [movingAverage.movingAverage(queueY)]
                    
                except: #si bug et n'arrive pas a convertir string
                    yG += [yG[-1]]

                if xG[-1] > xmaxG:
                    xG.pop(0)
                    yG.pop(0)
                
            plt.plot(xG,yG,'m', axes=axplot,label='GSR')
            
            #Resize le plot
            if xG[-1] > xmaxG:
                plt.axis([xG[0],xG[-1],yminG,ymaxG])               
            else:
                plt.axis([xminG,xmaxG,yminG,ymaxG])
            
            plt.ion()
            
            plt.show()
            plt.draw()
            axplot.set_xlabel('time (ms)')
            axplot.set_ylabel('GSR value')
        else:
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

        plt.pause(0.05)
        print i
    else:
        plt.pause(0.05)

ser.stopGS()
print ("end")