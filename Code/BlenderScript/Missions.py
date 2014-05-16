from Evenement import *
from bge import logic as gl

class EvenementWhat(Evenement) :      
    #Create effects for event
    def start(self) :
        super().start()
        
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "WHAT"    
            
        #self.setTimer()    
            
            
    #Cleaning
    def finish(self) :
        super().finish()
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "Score"    
        
#-----------------------------------------------   
# Events
#-----------------------------------------------           
   
class EvenementMessageMission(Evenement) :      
    #Create effects for event
    def start(self) :
        super().start()
        
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UImessageMission"].text = "WHAT"                
            
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
            self.speed_limit = 2.3
        else :
            self.speed_limit = 2

    def start(self) :
        super().start()
        self.speed_start = round(gl.currentGSR, 2)

        self.setTitle("Don't change your speed!")
        
    def verifyCondition(self) :  
        speed_current = round(gl.currentGSR, 2)
        speed_comp = abs(self.speed_start - speed_current)
        
        if speed_comp < self.speed_limit:
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

        self.setTitle("Try to get agitated as\nmuch as possible!")
        
    def verifyCondition(self) :
        speed_current = round(gl.currentGSR, 2)
        if speed_current >= self.speed_target:
            return True
        else:
            return False  