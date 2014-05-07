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
    obl["UIspeed"].text = "Speed : " +  str( round(gl.currentGSR, 2))
    
else:
    obl["UI"].setVisible(False, True)