import Evenement

class EvenementWhat(Evenement.Evenement) :
      
    #Create effects for event
    def startEvent(self,listArg) :
        super().startEvent(listArg)
        
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "WHAT"    
            
        self.setTimer(listArg[0])    
            
            
    #Cleaning
    def finish(self) :
        super().finish()
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "Score"    
        
     