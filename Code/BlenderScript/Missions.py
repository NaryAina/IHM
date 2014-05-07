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
        

class Evenement2(Evenement.Evenement) :
      
    #Create effects for event
    def startEvent(self,listArg) :
        super().startEvent(listArg)
        
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "event2"    
            
        self.setTimer(listArg[0])    
            
            
    #Cleaning
    def finish(self) :
        super().finish()
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "Score"    
        
                

class Evenement3(Evenement.Evenement) :
      
    #Create effects for event
    def startEvent(self,listArg) :
        super().startEvent(listArg)
        
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "event3"    
            
        self.setTimer(3)    
            
            
    #Cleaning
    def finish(self) :
        super().finish()
        from bge import logic as gl

        scn = gl.getCurrentScene()
        obl = scn.objects

        obl["UIscore"].text = "Score"    
        
        