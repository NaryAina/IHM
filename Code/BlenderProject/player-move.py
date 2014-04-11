import bge   
import ManageSpeed

def main():

    cont = bge.logic.getCurrentController()
    player = cont.owner

    #la valeur de la propriete passee dans l'actuator
    vitesse = cont.actuators['speed_actuator']
    
    #value = player.get(vitesse.propName)
    value = ManageSpeed.computeSpeed(player.get(vitesse.propName))
        
    keyboard = bge.logic.keyboard
    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
    ACTIVE = bge.logic.KX_SENSOR_ACTIVE 
    
    """
    if keyboard.events[bge.events.UPARROWKEY] == bge.logic.KX_SENSOR_ACTIVE :
        value += .002
    if keyboard.events[bge.events.DOWNARROWKEY] == bge.logic.KX_SENSOR_ACTIVE :
        value -= .002
    """
    
    #update valeur vitesse
    vitesse.value = str(value)
    cont.activate(vitesse) 
         
    player.applyRotation((0,0,player.get(vitesse.propName)), True)
    
    #print(vitesse.value)
        
main()
