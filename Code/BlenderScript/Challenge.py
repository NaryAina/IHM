from bge import logic as gl
import time
import random
import inspect

import Missions
import SocketUDPClose

#constants
MISSION_TYPES = ["ActionSlowDown", "ActionSpeedUp", "DangerVariate", "DangerSlowDown", "DangerSpeedUp", "WaitVariate", "MissionRelax", "MissionAgitate"]
EVENT_TYPES = ["EventBlackScreen", "EventRotatingScreen", "EventNoCubeMov", "EventJumpScare"]
PROBABILITY_NEW_MISSION = 6
PROBABILITY_NEW_EVENT = 1 #22
TIME_MIN_MISSION = 5
TIME_MAX_MISSION = 20
BONUS_TIME = 5
NBR_MISSION_BETWEEN_DIFFICULTIES = 3

class Challenge(object) :

    def __init__(self) :
        self.liste_mission = [] #current on-going missions
        self.liste_event = []
        self.score = 0
        self.timer = 20
        self.timer_no_mission = -1
        self.timer_no_event = -1
        self.totalTime = 0
        self.tempsReel = time.time()
        
        self.difficulty = 0
        self.MAX_MISSION = 5 #nbr de mission en meme temps
        self.MAX_EVENT = 2 #nbr d'event en meme temps

        self.queue_missions = [] #up-coming missions
        self.queue_events = []
        self.nbr_mission_won = 0
        self.nbr_mission_won_since = 0
        
    # Each logic tick    
    #----------------
        
    def runMissions(self) :
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
            if len(self.liste_event) < self.MAX_EVENT :
                self.addEvent()
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
                    
                    self.addMessage("Mission Won!", False)
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

        #Deleting old missions
        i = 0
        while i < len(self.liste_mission) :
            if self.liste_mission[i].finished :
                self.liste_mission.pop(i)
                #print("mission erased")
            else :
                i += 1

        #Verify if game over
        self.endCondition()
        
    def runEvents(self) :
        #launches 'run()' for every event in the event list
        i = 0
        while i < len(self.liste_event) :
            self.liste_event[i].run()
            if self.liste_event[i].finished :
                self.liste_event[i].finish() #cleaning
                self.liste_event.pop(i) #deleting
                self.timer_no_event = 0
            else :
                i += 1 
        
    # For missions    
    #----------------
    
    def addMission(self) :
                
        #randomly generates a mission if possible
        prob_new = random.randint(0, PROBABILITY_NEW_MISSION)
        if prob_new > (PROBABILITY_NEW_MISSION - self.timer_no_mission + self.difficulty) :
            
            #verify queue has missions
            if len(self.queue_missions) < 1 :
                self.generateQueueMission()
            
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
            self.addMessage(mission.title, False)
    
    #creates a random sequence of missions, without doubles
    def generateQueueMission(self) :
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
         
    # For events   
    #----------------
     
    def addEvent(self) :
        #time min between events
        if self.timer_no_event >= 7 :
            #randomly generates an event or not
            prob_new = random.randint(0, PROBABILITY_NEW_EVENT)
            if prob_new > (PROBABILITY_NEW_EVENT - self.timer_no_event) :
                
                #verify queue has missions
                if len(self.queue_events) < 1 :
                    self.generateQueueEvent()
                
                #creates the special event
                #(events have predefined time)
                #(and no difficulty)
                evenement = self.generateEvent()

                #launch event
                evenement.start()
                self.liste_event.append(evenement)       
    
                #add message to display what the mission is
                print(evenement.title)
                self.addMessage(evenement.title, True)
    
            
    #creates a random sequence of events, without doubles
    def generateQueueEvent(self) :
        self.queue_events = list(EVENT_TYPES)
        random.shuffle(self.queue_events)
        
    def generateEvent(self) :
        type = self.queue_events.pop(0) #pop first item

        if type == "EventBlackScreen" :
            return Missions.EventBlackScreen()
        elif type == "EventRotatingScreen" :
            return Missions.EventRotatingScreen()
        elif type == "EventNoCubeMov" :
            return Missions.EventNoCubeMov()
        elif type == "EventJumpScare" :
            return Missions.EventJumpScare()
    
    def addMessage(self, message, event) :
        evenement = Missions.EvenementMessage()
        evenement.setTimer(4)
        evenement.setMessageProperties(message, event)
        evenement.start()
        gl.globalDict["challenge"].liste_event.append(evenement)
        
    # End challenge mode    
    #----------------
        
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
    event = Missions.EventNoCubeMov()
    event.start()
    gl.globalDict["challenge"].liste_event.append(event)
    """
    
if __name__ == "__main__":
    main()