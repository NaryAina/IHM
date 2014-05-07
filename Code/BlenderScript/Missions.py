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
            
        self.setTimer(listArg[0])    
            
            
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
   
class MissionSlowDown(ActionMission):
    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        coef = 0.7
        speed_target = speed_start*coef
        points = 100
        wonTime = 10
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current <= speed_target:
            return True
        else:
            return False        

class MissionSpeedUp(ActionMission):
    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        coef = 1.3
        speed_target = speed_start*coef
        points = 100
        wonTime = 10
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current >= speed_target:
            return True
        else:
            return False  
            
#mission : ne pas depasser une fourchette de variation
class MissionVariate(DangerMission) :

    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        speed_limit = 2.5
        points = 100
        wonTime = 10
        
    def verifyCondition(self) :    
        speed_current = round(gl.currentGSR, 2)
        speed_comp = abs(speed_start - speed_current)
        if speed_comp < speed_limit:
            return True
        else:
            return False
        
class MissionDSlow(DangerMission) :
    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        speed_modifier = 1.5
        speed_limit = speed_start - speed_limit
        points = 100
        wonTime = 10
        
    def verifyCondition(self) :    
        speed_current = round(gl.currentGSR, 2)
        if speed_current < speed_limit:
            return True
        else:
            return False  

class MissionDSpeedUp(DangerMission) :
    def start(self,listArg) :
        speed_start = round(gl.currentGSR, 2)
        speed_modifier = 1.5
        speed_limit = speed_start + speed_limit
        points = 100
        wonTime = 10
        
    def verifyCondition(self) :    
        speed_current = round(gl.currentGSR, 2)
        if speed_current > speed_limit:
            return True
        else:
            return False  