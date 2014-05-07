#Lifecycle of Missions & Events :
#   init and add it to stack of events
#   each tick, run() on all memebers of stack
#   and verifies if boolean finished
#   if true, then does finish() and removes from stack

#__init__() et run() pas besoin de redefinir (pas sur pour run - depend comment va marcher...)

# (note : on peut peut-etre utiliser des evenements quand fini mission pour afficher resultats ("gagne tant de points"...))



import time

########################################
# Events
########################################  



class Evenement(object) :
    def __init__(self, listArg): 
        self.finished = False
        
        self.__tempsReel = time.time()
        self.setTimer(listArg)
        self.start(listArg)
      
    #Create effects for event + set the timer here!
    def start(self,listArg) :
        #add graphics etc
        pass
      
    #Passes time & finishes if no more
    def run(self):
        if (time.time() - self.__tempsReel) >= 1.0 :
            self.__timer -= 1
            if (self.__timer <= 0) :
                self.finished = True
            self.__tempsReel = time.time()
            print("1 sec")
            
    #Cleaning
    def finish(self) :
        #removes graphics
        pass
    
    #Sets how much time
    def setTimer(self, temps) :
        #self.__timer = temps
        self.__timer = temps[0]
       
        
########################################
# Missions
########################################        
        
class Mission(Evenement) :
    def __init__(self, listArg): 
        super().__init__(listArg)
        #Attributes
        self.points = 0
        self.wonTime = 0
        self.won = False
        
    #Condition to win - returns boolean    
    def verifyCondition(self) :
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
    def __init__(self, listArg):      
        super().__init__(listArg)
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