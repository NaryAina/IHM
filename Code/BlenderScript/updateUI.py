# Updates the UI information
#

###VERIFY IF MISSION MODE!!!!

import Missions
from bge import logic as gl

liste_mission = gl.globalDict["liste_mission"]

#for m in gl.globalDict["liste_mission"] :
i = 0
while i < len(liste_mission) :
    liste_mission[i].run()
    if liste_mission[i].finished :
        liste_mission[i].finish()
        liste_mission.pop(i)
    else :
        i += 1

#from bge import logic as gl

#scn = gl.getCurrentScene()
#obl = scn.objects

#obl["UIscore"].text = "WHAT"