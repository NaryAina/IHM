#Initialisation liste challenge

import Missions
from bge import logic as gl

gl.globalDict["liste_mission"] = []

mission = Missions.EvenementWhat([5]) 

gl.globalDict["liste_mission"].append(mission)
