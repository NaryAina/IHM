# Updates the UI information
# runs the challenge guide (which selects & runs missions)

import Challenge
from bge import logic as gl

scn = gl.getCurrentScene()
obl = scn.objects

if gl.globalDict["modeChallenge"] :

    #Updates missions & score
    gl.globalDict["challenge"].run()
        
    #Affichage dans UI
    obl["UItime"].text = str( gl.globalDict["challenge"].timer )
    obl["UIspeed"].text = str( round(gl.currentGSR, 2))
    obl["UIscore"].text = str( gl.globalDict["challenge"].score )
    
    obl["UIscoreText"].text = "Score :"
    obl["UIspeedText"].text = "Speed"
    
    #Affichage des missions
    affichage = ""
    for mission in gl.globalDict["challenge"].liste_mission :
        affichage += "> " + mission.title + " (" + str(mission.timer) + ")" + "\n"
    obl["UImissions"].text = affichage
        
else:
    obl["UI"].setVisible(False, True)