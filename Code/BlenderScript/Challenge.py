from bge import logic as gl
import time
import random
import inspect

import Missions
import SocketUDPClose

class Challenge(object) :

    def __init__(self) :
        self.liste_mission = []
        self.liste_evenement = []
        self.score = 0
        self.timer = 30
        self.timer_no_mission = -1
        self.timer_no_event = -1
        self.totalTime = 0
        self.tempsReel = time.time()
        self.difficulty = 0
        self.MAX_MISSION = 3 #nbr de mission en meme temps
        self.MAX_EVENT = 1 #nbr d'event en meme temps

    def run(self) :
        #Game timers
        if (time.time() - self.tempsReel) >= 1.0 :
            self.tempsReel = time.time()
            self.totalTime += 1
            self.timer -= 1
            self.timer_no_mission += 1
            self.timer_no_event += 1
            
        #See if can add a new mission    
        if len(self.liste_mission) < self.MAX_MISSION :
            #self.addMission()   
            pass
            
        #See if can add a new event    
        if len(self.liste_evenement) < self.MAX_EVENT :
            #self.addEvent()
            pass
        
        #launches 'run()' for every mission in the mission list
        for mission in self.liste_mission :
            mission.run()
            if mission.finished :
                mission.finish() #cleaning
                
                #if win
                if mission.won :
                    print("a"+str(self.timer))
                    self.score +=  mission.points
                    self.timer +=  mission.wonTime
                    print("mission won")
                    
                    print("w"+str(mission.wonTime))
                    print("p"+str(self.timer))
                else :
                    print("mission lost")
                
                self.timer_no_mission = 0

        #Deleting
        for i in range(len(self.liste_mission)) :
            if self.liste_mission[i].finished :
                self.liste_mission.pop(i)
                print("mission erased")
                
        #launches 'run()' for every event in the event list
        i = 0
        while i < len(self.liste_evenement) :
            self.liste_evenement[i].run()
            if self.liste_evenement[i].finished :
                self.liste_evenement[i].finish() #cleaning
                self.liste_evenement.pop(i) #deleting
                self.timer_no_event = 0
            else :
                i += 1
    
        #Verify if game over
        self.endCondition()
    
    def addMission(self) :
        
        self.timer_no_mission += 1
        
        mission = Missions.EvenementWhat([5]) 
        self.liste_mission.append(mission)
        
    def addEvent(self) :
        mission = Missions.EvenementWhat([5]) 
        self.liste_mission.append(mission)
        
    def endCondition(self) :            
        if self.timer < 0 :
            #close socket
            SocketUDPClose.main()
            #save score
            gl.globalDict["Score"] = self.score
            gl.globalDict["Time"] = self.totalTime
            #replace scene
            gl.getCurrentScene().replace('GameOver scene')

            
#--------------------------------------------
# Initialise
#--------------------------------------------

def main() :
    #Initialisation liste challenge 
    gl.globalDict["challenge"] = Challenge()
    
    gl.currentGSR = 0.0 #TEMPORAIRE!!!!!!!!!!!
    
    #mission = Missions.MissionVariate([5]) 
    mission = Missions.MissionVariateWait([3, 10]) 
    #mission = Missions.EvenementWhat([3]) 
    gl.globalDict["challenge"].liste_mission.append(mission)
    
if __name__ == "__main__":
    main()