from bge import logic as gl
import os

FICHIER_SCORE = "gameCubeScoreFile.sav"

#if file doesn't exist
if not os.path.exists(FICHIER_SCORE):
    f = open(FICHIER_SCORE, "w")
    f.close()
    highScore = 0
else :
    try :
        file = open(FICHIER_SCORE)
        #get highscore
        highScore = int(file.read())
        file.close()
    except:
        highScore = 0

#get score
missionscore = int(gl.globalDict["challenge"].score)
timescore = int(gl.globalDict["challenge"].totalTime) * 10
difficultyscore = (int(gl.globalDict["challenge"].difficulty) + 1)*100
total = missionscore + timescore + difficultyscore

#change objects
scn = gl.getCurrentScene()
obl = scn.objects
obl["missionscore"].text = str(missionscore)
obl["timescore"].text = str(timescore)
obl["difficulty"].text = str(difficultyscore)
obl["total"].text = str(total)

#highscore
if total > highScore :
    obl["highscore"].text = "NEW HIGHSCORE!!!"
    file = open(FICHIER_SCORE, "w")
    file.write(str(total))
    file.close()
else :
    obl["highscore"].text = "Highscore :     " + str(highScore)