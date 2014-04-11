import bge  

def main():

    cont = bge.logic.getCurrentController()
    cameraController = cont.owner
    
    keyboard = bge.logic.keyboard
    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
    ACTIVE = bge.logic.KX_SENSOR_ACTIVE 
    
    if keyboard.events[bge.events.LEFTARROWKEY] == bge.logic.KX_SENSOR_ACTIVE :
        cameraController.applyRotation((0,0,-0.2), True)
    if keyboard.events[bge.events.RIGHTARROWKEY] == bge.logic.KX_SENSOR_ACTIVE :
        cameraController.applyRotation((0,0,0.2), True)
    
    #update valeur vitesse
    #cont.activate(vitesse) 
    
    #print('wja')
    
main()
