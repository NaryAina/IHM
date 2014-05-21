from Evenement import *
from bge import logic as gl 
import random
               
#-----------------------------------------------   
# Printing messages on screen (mission/results/events)
#-----------------------------------------------           
   
class EvenementMessage(Evenement) :      
    #Create effects for event
    def start(self) :
        super().start()
        self.setTitle("Display")
        
        #create new object
        scn = gl.getCurrentScene()
        obl = scn.objects
        
        #set position
        SIZE_LETTER = 0.3 #? 
        if self.event :
            self.object = obl["UIeventText"]
            self.originalPosition = [14.52026,-6.65681,4.41221]
            self.centered = 0 
        else:
            self.object = obl["UImessage"]
            self.originalPosition  = [13.28884,-6.65681,6.01999]
            self.centered = (len(self.message)*SIZE_LETTER) / 2
            self.centered = 0
           
            #print("center at " + str(self.centered ))
        
        self.object.localPosition = self.originalPosition 
        self.object.applyMovement((0,-self.centered,0))
        self.object.text = self.message
            
    #Cleaning
    def finish(self) :
        super().finish()
        self.object.text = ""   
        self.object.localPosition = self.originalPosition 
        
    def run(self) :
        super().run()    
        #self.object.text = self.message
        if self.message == "Mission won!":
            speed = 0.006
        else :
            speed = 0.003
        self.object.applyMovement((0,0,speed)) #up movement
        
    def setMessageProperties(self, message, event) :
        self.message = message
        self.event = event

#-----------------------------------------------   
# Events
#-----------------------------------------------           

class EventJumpScare(Evenement) :  
    #Create effects for event 
    def start(self) :
        super().start()
        self.setTitle("BOO!")
        
        #get object
        scn = gl.getCurrentScene()
        obl = scn.objects
        self.object = obl["eventJumpScare"]
        
        self.setTimer(1)
    
    def run(self):
        super().run()
        self.object.visible = True
        
class EventBlackScreen(Evenement) : 
    #Create effects for event 
    def start(self) :
        super().start()
        self.setTitle("Play in the dark!")
        
        #get object
        scn = gl.getCurrentScene()
        obl = scn.objects
        self.object = obl["eventWallVision"]

        temps = random.randint(5,15) #5 a 15 secondes
        self.setTimer(temps)
        
    def run(self):
        super().run()
        self.object.visible = True
        
class EventRotatingScreen(Evenement) :     
    #Create effects for event 
    def start(self) :
        super().start()
        self.setTitle("Rotating screen!!")
        
        #get object
        scn = gl.getCurrentScene()
        obl = scn.objects
        self.objectplayer = obl["CameraController"]
        
        temps = random.randint(7,18)
        self.setTimer(temps)
        
        self.speedRotation = random.uniform(0.01,0.09)
        self.directionRotation = random.choice([-1, 1])
        
    def run(self):
        super().run()
        self.objectplayer.applyRotation((0,0,self.directionRotation * self.speedRotation), True) #make camera rotate

class EventNoCubeMov(Evenement) :    
    #Create effects for event 
    def start(self) :
        super().start()
        self.setTitle("No rotation cube!")
        
        #get object
        scn = gl.getCurrentScene()
        obl = scn.objects
        self.object = obl["player"]
        self.textVitesse = obl["UIspeed"]
        
        temps = random.randint(10,15)
        self.setTimer(temps)
        
    def run(self):
        super().run()
        self.object.localOrientation = [0,0,0] #prevents cube from moving
        self.textVitesse.text = "???"

#----------------------------------   
# Missions
#-----------------------------------------------   
   
class MissionSlowDown(ActionMission):
    def setDifficulty(self, difficulty) :
        if difficulty <= 0:
            self.coef = 0.7
        elif difficulty == 1 :
            self.coef = 0.6
        else :
            self.coef = 0.5
            
    def start(self) :
        super().start()
        speed_start = round(gl.currentGSR, 2)
        self.speed_target = speed_start*self.coef

        self.setTitle("Slow down to " + str(round(self.speed_target,2)) + "!")
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current <= self.speed_target:
            return True
        else:
            return False        

class MissionSpeedUp(ActionMission):
    def setDifficulty(self, difficulty) :
        if difficulty <= 0:
            self.coef = 1.3
        elif difficulty == 1 :
            self.coef = 1.5
        else :
            self.coef = 1.6

    def start(self) :
        super().start()
        speed_start = round(gl.currentGSR, 2)
        self.speed_target = speed_start*self.coef

        self.setTitle("Speed up to " + str(round(self.speed_target,2)) + "!")
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current >= self.speed_target:
            return True
        else:
            return False  
            
#mission : ne pas depasser une fourchette de variation
class MissionVariate(DangerMission) :
    def setDifficulty(self, difficulty) :
        if difficulty <= 0:
            self.speed_limit = 2.5
        elif difficulty == 1 :
            self.speed_limit = 2
        else :
            self.speed_limit = 1.5

    def start(self) :
        super().start()
        self.speed_start = round(gl.currentGSR, 2)

        self.setTitle("Don't change\nyour speed!")
        
    def verifyCondition(self) :  
        speed_current = round(gl.currentGSR, 2)
        speed_comp = abs(self.speed_start - speed_current)
        
        if speed_comp > self.speed_limit:
            return True
        else:
            return False
        
class MissionDSlowDown(DangerMission) : 
    def setDifficulty(self, difficulty) :
        if difficulty <= 0:
            self.speed_modifier = 1.5
        elif difficulty == 1 :
            self.speed_modifier = 1.3
        else :
            self.speed_modifier = 1
            
    def start(self) :
        super().start()
        speed_start = round(gl.currentGSR, 2)
        self.speed_limit = speed_start - self.speed_modifier

        self.setTitle("Don't reach " + str(round(self.speed_limit,2)) + "!")
        
    def verifyCondition(self) :    
        speed_current = round(gl.currentGSR, 2)
        if speed_current < self.speed_limit:
            return True
        else:
            return False  

class MissionDSpeedUp(DangerMission) : 
    def setDifficulty(self, difficulty) :
        if difficulty <= 0:
            self.speed_modifier = 1.5
        elif difficulty == 1 :
            self.speed_modifier = 1.3
        else :
            self.speed_modifier = 1
       
    def start(self) :
        super().start()
        speed_start = round(gl.currentGSR, 2)
        self.speed_limit = speed_start +  self.speed_modifier

        self.setTitle("Don't reach " + str(round(self.speed_limit,2)) + "!")
        
    def verifyCondition(self) :    
        speed_current = round(gl.currentGSR, 2)
        if speed_current > self.speed_limit:
            return True
        else:
            return False  
        
class MissionVariateWait(WaitingMission) :
    def setDifficulty(self, difficulty) :
        if difficulty <= 0:
            self.speed_limit = 2.5
        elif difficulty == 1 :
            self.speed_limit = 2.3
        else :
            self.speed_limit = 2

    def start(self) :
        super().start()
        self.speed_start = round(gl.currentGSR, 2)

        self.setTitle("Stay at " + str(self.speed_start) + "!")
        
    def verifyCondition(self) :  
        speed_current = round(gl.currentGSR, 2)
        speed_comp = abs(self.speed_start - speed_current)
        if speed_comp < self.speed_limit:
            return True
        else:
            return False
            
class MissionRelax(WaitingMission):
    def setDifficulty(self, difficulty) :
        if difficulty <= 0:
            self.more = 1
        elif difficulty == 1 :
            self.more = 3
        else :
            self.more = 5
            
    def start(self) :
        super().start()
        speed_start = round(gl.currentGSR, 2)
        self.speed_target = speed_start - self.more

        self.setTitle("Try to relax as much\nas possible!")
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current <= self.speed_target:
            return True
        else:
            return False        

class MissionAgitate(WaitingMission):
    def setDifficulty(self, difficulty) :
        if difficulty <= 0:
            self.more = 1
        elif difficulty == 1 :
            self.more = 3
        else :
            self.more = 5

    def start(self) :
        super().start()
        speed_start = round(gl.currentGSR, 2)
        self.speed_target = speed_start + self.more

        self.setTitle("Get excited!!")
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current >= self.speed_target:
            return True
        else:
            return False  