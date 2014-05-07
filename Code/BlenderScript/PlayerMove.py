import bge
from bge import logic as gl
import ManageSpeed

def main():

    cont = gl.getCurrentController()
    player = cont.owner

    #la valeur de la propriete passee dans l'actuator
    vitesse = cont.actuators['speed_actuator']
    
    #Recoit et traite valeur du GSR pour la rotation
    value = ManageSpeed.computeSpeed(gl.currentGSR)
    
    #Keyboard controlled (Debug)
    """
    keyboard = gl.keyboard
    JUST_ACTIVATED = gl.KX_INPUT_JUST_ACTIVATED
    ACTIVE = gl.KX_SENSOR_ACTIVE 
    
    if keyboard.events[bge.events.UPARROWKEY] == gl.KX_SENSOR_ACTIVE :
        value += .002
    if keyboard.events[bge.events.DOWNARROWKEY] == gl.KX_SENSOR_ACTIVE :
        value -= .002
    """
    
    #update valeur vitesse dans la propriete
    vitesse.value = str(value)
    cont.activate(vitesse) 
         
    #Rotation
    player.applyRotation((0,0,player.get(vitesse.propName)), True)
   
    #Affichage dans UI
    scn = gl.getCurrentScene()
    obl = scn.objects
    if gl.globalDict["modeChallenge"] :
        obl["UIspeed"].text = "Speed : " +  str( round(gl.currentGSR, 2))
    else:
        obl["UIspeed"].setVisible(False, True)
             
main()