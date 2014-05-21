# Updates the UI information
# runs the challenge guide (which selects & runs missions)

import Challenge
from bge import logic as gl

scn = gl.getCurrentScene()
obl = scn.objects

obl["eventWallVision"].visible = False
obl["eventJumpScare"].visible = True

if gl.globalDict["modeChallenge"] :
       
    #run time & conditions & add missions/events
    gl.globalDict["challenge"].runTimers()   
       
    #Updates missions & score
    gl.globalDict["challenge"].runMissions()    
    
    #Affichage dans UI
    obl["UItime"].text = str( gl.globalDict["challenge"].timer )
    obl["UIspeed"].text = str( round(gl.currentGSR, 2))
    obl["UIscore"].text = str( gl.globalDict["challenge"].score )
    obl["UIdifficulty"].text = str( gl.globalDict["challenge"].difficulty + 1)
    
    obl["UIscoreText"].text = "Score :"
    obl["UIspeedText"].text = "Speed"
    obl["UIdifficultyText"].text = "Level"
    
    #Affichage des missions
    affichage = ""
    for mission in gl.globalDict["challenge"].liste_mission :
        affichage += "> " + mission.title + " (" + str(mission.timer) + ")" + "\n"
    obl["UImissions"].text = affichage
        
    #run events (affect UI so as to be called after )
    gl.globalDict["challenge"].runEvents()      
        
else:
    obl["UI"].setVisible(False, True)