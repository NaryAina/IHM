from bge import logic as gl

scn = gl.getCurrentScene()
obl = scn.objects

objectChallenge = obl['ButtonChallenge']
objectRelax = obl['ButtonRelax']

#boolean to control the game mode
if objectChallenge["buttonPressed"] :
    gl.globalDict["modeChallenge"] = True
    print("OK")
if objectRelax["buttonPressed"] :
    gl.globalDic["modeChallenge"] = False
    print("OK")
    
if objectRelax["buttonPressed"] or objectChallenge["buttonPressed"] :
    scn.replace('GameScene')