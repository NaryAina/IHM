from bge import logic as gl
import time
import random
import inspect

import Missions
import SocketUDPClose

#constants
MISSION_TYPES = ["ActionSlowDown", "ActionSpeedUp", "DangerVariate", "DangerSlowDown", "DangerSpeedUp", "WaitVariate", "MissionRelax", "MissionAgitate"]
PROBABILITY_NEW_MISSION = 6
TIME_MIN_MISSION = 5
TIME_MAX_MISSION = 20
BONUS_TIME = 5
NBR_MISSION_BETWEEN_DIFFICULTIES = 3

class Challenge(object) :

    def __init__(self) :
        self.liste_mission = [] #current on-going missions
        self.liste_evenement = []
        self.score = 0
        self.timer = 20
        self.timer_no_mission = -1
        self.timer_no_event = -1
        self.totalTime = 0
        self.tempsReel = time.time()
        self.difficulty = 0
        self.MAX_MISSION = 5 #nbr de mission en meme temps
        self.MAX_EVENT = 1 #nbr d'event en meme temps

        self.queue_missions = [] #up-coming missions
        self.nbr_mission_won = 0
        self.nbr_mission_won_since = 0
        
    def run(self) :
        #Game timers
        if (time.time() - self.tempsReel) >= 1.0 :
            self.tempsReel = time.time()
            self.totalTime += 1
            self.timer -= 1
            self.timer_no_mission += 1
            self.timer_no_event += 1
            
            #See if can add a new mission  (each second only)  
            if len(self.liste_mission) < self.MAX_MISSION and len(self.liste_mission) < self.difficulty + 1:
                self.addMission()   
                
            #See if can add a new event (each second only)
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
                    
                    #score + time won
                    realTimeSpent = mission.timeSpent #- (mission.timeSpent - mission.timer)
                    scoreWon =  realTimeSpent * 10 + self.difficulty * 10
                    timeWon = mission.timeSpent / (1+self.difficulty) + BONUS_TIME + (1/BONUS_TIME) * (1+self.difficulty) 
                    
                    self.score += int(scoreWon)
                    self.timer += int(timeWon)
                    
                    print("mission won!")
                    print("Score + " + str(scoreWon) + " Time + " + str(timeWon))
                    
                    self.nbr_mission_won += 1
                    self.nbr_mission_won_since += 1
                    
                    #augmenter difficulte HERE!!
                    if self.nbr_mission_won_since >= (NBR_MISSION_BETWEEN_DIFFICULTIES + self.difficulty) :
                        self.difficulty += 1
                        self.nbr_mission_won_since = 0
                    
                else :
                    print("mission lost")
                self.timer_no_mission = 0

        #Deleting
        i = 0
        while i < len(self.liste_mission) :
            if self.liste_mission[i].finished :
                self.liste_mission.pop(i)
                #print("mission erased")
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
        self.endCondition()
    
    def addMission(self) :
                
        #randomly generates a mission if possible
        prob_new = random.randint(0, PROBABILITY_NEW_MISSION)
        if prob_new > (PROBABILITY_NEW_MISSION - self.timer_no_mission + self.difficulty) :
            
            #verify queue has missions
            if len(self.queue_missions) < 1 :
                self.generateQueue()
            
            #creates the mission
            mission = self.generateMission()
            
            #sets time
            #si moins de 5 secondes, la mission fait d'office le temps qu'il reste
            if self.timer < TIME_MIN_MISSION :
                mission.setTimer(self.timer)
            #sinon, genere mission avec temps rand
            else :
                minTime = TIME_MIN_MISSION
                maxTime = TIME_MAX_MISSION
                if self.timer < maxTime :
                    maxTime = self.timer #si max plus grand que le temps qu'il reste
                timeMission = random.randint(minTime, maxTime)
                mission.setTimer(timeMission)
            
            #sets difficulty
            #add something random?
            mission.setDifficulty(self.difficulty)
            
            #launch mission
            mission.start()
            self.liste_mission.append(mission)       

            #add message to display what the mission is
            print(mission.title)
    
    #creates a random sequence of missions, without doubles
    def generateQueue(self) :
        self.queue_missions = list(MISSION_TYPES)
        random.shuffle(self.queue_missions)
    
    def generateMission(self) :
        type = self.queue_missions.pop(0) #pop first item

        if type == "ActionSlowDown" :
            return Missions.MissionSlowDown()
        elif type == "ActionSpeedUp" :
            return Missions.MissionSpeedUp()
        elif type == "DangerVariate" :
            return Missions.MissionVariate()
        elif type == "DangerSlowDown" :
            return Missions.MissionDSlowDown()
        elif type == "DangerSpeedUp" :
            return Missions.MissionDSpeedUp()
        elif type == "WaitVariate" :
            return Missions.MissionVariateWait()
        elif type == "MissionRelax" :
            return Missions.MissionRelax()
        elif type == "MissionAgitate" :
            return Missions.MissionAgitate()
      
    def addEvent(self) :
        #mission = Missions.EvenementWhat([5]) 
        #self.liste_mission.append(mission)
        pass
        
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
    
    """
    #mission = Missions.MissionVariate([5]) 
    mission = Missions.MissionVariateWait([3, 10]) 
    #mission = Missions.EvenementWhat([3]) 
    gl.globalDict["challenge"].liste_mission.append(mission)
    """
    
if __name__ == "__main__":
    main()