#Initialisation liste challenge

import Missions
from bge import logic as gl

gl.globalDict["liste_mission"] = []

mission = Missions.EvenementWhat([1]) 

gl.globalDict["liste_mission"].append(mission)

