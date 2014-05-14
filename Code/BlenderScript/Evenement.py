#Lifecycle of Missions & Events :
#   1- intiantiate mission
#   2- set timer, difficulty
#   3- start() and add it to stack of events
#   4- each tick, run() is launched on all memebers of stack
#   and verifies if boolean finished
#   if true, then does finish() and removes from stack

#__init__() et run() pas besoin de redefinir (pas sur pour run - depend comment va marcher...)

#TOUJOURS APPELER SUPER()....() dans redef!!!

# (note : on peut peut-etre utiliser des evenements quand fini mission pour afficher resultats ("gagne tant de points"...))



import time

########################################
# Events
########################################  



class Evenement(object) :
    def __init__(self): 
        self.finished = False
      
    #Create effects for event + set the timer here!
    def start(self) :
        #start the timer
        self.__tempsReel = time.time()
        
        #add graphics etc
        pass
      
    #Passes time & finishes if no more
    def run(self):
        if (time.time() - self.__tempsReel) >= 1.0 :
            self.timer -= 1
            if (self.timer <= 0) :
                self.finished = True
            self.__tempsReel = time.time()
            #print("1 sec")
            
    #Cleaning
    def finish(self) :
        #removes graphics
        pass
    
    #Sets how much time
    def setTimer(self, temps) :
        self.timeSpent = temps #pour garder en memoire
        self.timer = temps     
        
########################################
# Missions
########################################        
        
class Mission(Evenement) :
    def __init__(self): 
        super().__init__()
        #Attributes
        self.won = False
        
    #Condition to win - returns boolean    
    def verifyCondition(self) :
        pass
        
    def setTitle(self, title) :
        self.title = title
        
    #sets parameter to be used in condition, according to difficulty
    def setDifficulty(self, difficulty):
        pass
        
########################################
# Main types of missions
########################################
        
class ActionMission(Mission) :    
    #Finish and win if condition
    def run(self) :
        super().run()
        if self.verifyCondition() :
            self.finished = True
            self.won = True
            
class DangerMission(Mission) :
    #base case is that will win after time finished
    def __init__(self):      
        super().__init__()
        self.won = True
        
    #Lose and finish if condition
    def run(self) :  
        super().run()
        if self.verifyCondition() :
            self.finished = True
            self.won = False
    
class WaitingMission(Mission) :    
    #Wins but continues until time    
    def run(self) :  
        super().run()
        if self.verifyCondition() :
            self.won = True