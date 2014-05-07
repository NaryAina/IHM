from Evenement import *
from bge import logic as gl

class EvenementWhat(Evenement) :      
    #Create effects for event
    def start(self,listArg) :
        super().start(listArg)
        
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "WHAT"    
            
        #self.setTimer(listArg)    
            
            
    #Cleaning
    def finish(self) :
        super().finish()
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "Score"    
        

class Evenement2(Evenement) :      
    #Create effects for event
    def start(self,listArg) :
        super().start(listArg)
        
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "event2"    
            
        self.setTimer(listArg[0])    
            
            
    #Cleaning
    def finish(self) :
        super().finish()
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "Score"    
        
                

class Evenement3(Evenement) :      
    #Create effects for event
    def start(self,listArg) :
        super().start(listArg)
        
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "event3"    
            
        self.setTimer(3)    
            
            
    #Cleaning
    def finish(self) :
        super().finish()
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "Score"    
   
#-----------------------------------------------   
# Missions
#-----------------------------------------------   
   
class MissionSlowDown(ActionMission):
    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        coef = 0.7
        self.speed_target = speed_start*coef
        self.setReward(10,100)
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current <= self.speed_target:
            return True
        else:
            return False        

class MissionSpeedUp(ActionMission):
    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        coef = 1.3
        self.speed_target = speed_start*coef
        self.setReward(10,100)
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current >= self.speed_target:
            return True
        else:
            return False  
            
#mission : ne pas depasser une fourchette de variation
class MissionVariate(DangerMission) :
    def start(self,listArg) :
        self.speed_start = round(gl.currentGSR, 2)
        self.speed_limit = 2.5
        self.setReward(10,100)
        
    def verifyCondition(self) :  
        speed_current = round(gl.currentGSR, 2)
        speed_comp = abs(self.speed_start - speed_current)
        
        if speed_comp < self.speed_limit:
            return True
        else:
            return False
        
class MissionDSlowDown(DangerMission) :        
    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        speed_modifier = 1.5
        self.speed_limit = speed_start - speed_limit
        self.setReward(10,100)
        
    def verifyCondition(self) :    
        speed_current = round(gl.currentGSR, 2)
        if speed_current < self.speed_limit:
            return True
        else:
            return False  

class MissionDSpeedUp(DangerMission) :        
    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        speed_modifier = 1.5
        self.speed_limit = speed_start + speed_limit
        self.setReward(10,100)
        
    def verifyCondition(self) :    
        speed_current = round(gl.currentGSR, 2)
        if speed_current > self.speed_limit:
            return True
        else:
            return False  
        
class MissionVariateWait(WaitingMission) :
    def start(self,listArg) :
        #self.speed_start = round(gl.currentGSR, 2)
        self.speed_start = 22
        self.speed_limit = 2.5
        #time, point
        self.setReward(listArg[1],100)
        
    def verifyCondition(self) :  
        speed_current = round(gl.currentGSR, 2)
        speed_comp = abs(self.speed_start - speed_current)
        if speed_comp < self.speed_limit:
            return True
        else:
            return False