from bge import logic as gl
import time
import random

import Missions

class Challenge(object) :

    def __init__(self) :
        self.liste_mission = []
        self.liste_evenement = []
        self.score = 0
        self.timer = 30
        self.timer_no_mission = -1
        self.timer_no_event = -1
        self.tempsReel = time.time()
        self.difficulty = 0
        self.MAX_MISSION = 3 #nbr de mission en meme temps
        self.MAX_EVENT = 1 #nbr d'event en meme temps

    def run(self) :
        #Game timers
        if (time.time() - self.tempsReel) >= 1.0 :
            self.tempsReel = time.time()
            self.timer -= 1
            self.timer_no_mission += 1
            self.timer_no_event += 1
            
        #See if can add a new mission    
        if len(self.liste_mission) < self.MAX_MISSION :
            self.addMission()   
            
        #See if can add a new event    
        if len(self.liste_evenement) < self.MAX_EVENT :
            self.addEvent()
        
        #launches 'run()' for every mission in the mission list
        i = 0
        while i < len(self.liste_mission) :
            self.liste_mission[i].run()
            if self.liste_mission[i].finished :
                self.liste_mission[i].finish() #cleaning
                
                #if win
                if self.liste_mission[i].won :
                    self.score += self.liste_mission[i].points
                    self.timer += self.liste_mission[i].wonTime

                self.liste_mission.pop(i) #deleting
                self.timer_no_mission = 0
            else :
                i += 1
                
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
        #self.endCondition()
    
    def addMission(self) :
        mission = Missions.EvenementWhat([5]) 
        self.liste_mission.append(mission)
        
    def addMission(self) :
        mission = Missions.EvenementWhat([5]) 
        self.liste_mission.append(mission)
        
    def endCondition(self) :
    
        gameOver = obl['CameraController']["gameOver"]
            
        if gameOver :
            import SocketUDP-Close
            scn.replace('GameOver scene')
    

#Initialisation liste challenge 
gl.globalDict["challenge"] = Challenge()
gl.globalDict["challenge"].addMission()