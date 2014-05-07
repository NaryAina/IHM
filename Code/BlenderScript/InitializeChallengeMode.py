#Initialisation liste challenge

import Missions
from bge import logic as gl

gl.globalDict["liste_mission"] = []

gl.globalDict["score"] = 0

gl.globalDict["timer"] = 0

mission = Missions.EvenementWhat([5]) 

gl.globalDict["liste_mission"].append(mission)
