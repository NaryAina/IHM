#Lifecycle of Missions & Events :
#   init and add it to stack of events
#   each tick, run() on all memebers of stack
#   and verifies if boolean finished
#   if true, then does finish() and removes from stack

#__init__() et run() pas besoin de redefinir (pas sur pour run - depend comment va marcher...)

# (note : on peut peut-etre utiliser des evenements quand fini mission pour afficher resultats ("gagne tant de points"...))

########################################
# Events
########################################  

class Evenement(object) :

    self.timer = 0
    self.finished = False

    def __init__(self, currentTime):      
        self.setTimer(currentTime)
        # import logic
        # if self.timer > gl.challengeTimer :
        # gl.challengeTimer = self.timer
        self.startEvent()
      
    #Create effects for event
    def startEvent(self) :
        #add graphics etc
        pass
      
    #Passes time & finishes if no more
    def run(self):
        self.timer -= 1
        if (self.timer <= 0) :
            self.finished = True
            
    #Cleaning
    def finish(self) :
        #removes graphics
        pass
    
    #Sets how much time
    def setTimer(self, currentTime) :
        #random timer or according to current...
        pass

########################################
# Missions
########################################        
        
class Mission(Evenement) :
    
    self.won = False
    self.points = 0
    self.wonTime = 0
        
    #Condition to win - returns boolean    
    def verifyCondition(self) :
        pass
    
    #Defines what wins
    def win(self) :
        #something to self.points = 0
        #something to self.wonTime = 0
        pass
        
    #(Losing points if needed)
    def lose(self) :
        #same as win...
        pass
        
    #Cleaning + calls win if won is True + gives points won
    def finish(self) :
        self.super()
        if (self.won) :
            self.win()
        self.__giveReward()
    
    #Add points & time to score & challenge timer
    def __giveReward(self) :
        # A COMPLETER!!!!!
        #import bge etc...
        #bl.score += ...
        # .........
        pass
        
########################################
# Main types of missions
########################################
        
class ActionMission(Mission) :
    #Finish and win if condition
    def run(self) :  
        self.super()
        if self.verifyCondition() :
            self.finish = True
            self.won = True
            
class DangerMission(Mission) :
    #base case is that will win after time finished
    def __init__(self, currentTime):      
        self.super(currentTime)
        self.won = True
        
    #Lose and finish if condition
    def run(self) :  
        self.super()
        if self.verifyCondition() :
            self.finish = True
            self.won = False
    
class WaitingMission(Mission) :
    #Wins but continues until time    
    def run(self) :  
        self.super()
        if self.verifyCondition() :
            self.won = True