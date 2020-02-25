from epics import PV

from sardana import State, SardanaValue
from sardana.pool.controller import MotorController
from sardana.pool.controller import DefaultValue, Description, FGet, FSet, Type


          
class CopleyEpicsController(MotorController):

    ctrl_properties = \
        {
        
          "Device": {Type : str,
                  Description : "connected device server",
                   DefaultValue : ["motor1","motor2"]},
                  
       
        }
    AXIS_NAMES = {1: "pos"}
    ANS = 1
    STATES = {"ON": State.On, "MOVING": State.Moving}

    def __init__(self, inst, props, *args, **kwargs):
        MotorController.__init__(self,inst, props, *args, **kwargs)
        #super_class = super(CopleyController, self)
        #super_class.__init__(inst, props, *args, **kwargs)
	device = self.Device
        #self.copleyController = TangoDSObject(device)
     
    #ef __del__(self):
        #el self.copleyController

    def StateOne(self, axis):
        """
        Read the axis state. asix can be 1, 2, 3, 4. One axis is defined as one motor in spock. 
      
        """
        ans = self.ANS
	if ans == 1:
            state = self.STATES["ON"]
        else:
	    state = self.STATES["MOVING"]
         
       
        return state

    def ReadOne(self, axis):
        """
        Read the position of the axis(motor). When "wa" or "wm motor_name"is called in spock, 
        this method is used. 
        """
       
       
        
        pos = PV('pos')
        ans = pos.get()
        return float(ans)
    #def DefinePosition(self, axis, position):
        #axis_name = self.AXIS_NAMES[axis]
      
        #copleyController = TangoDSObject(axis_name)
     
        #copleyController.setPosition(position)
        
    def StartOne(self, axis, position):
        """
        Move the axis(motor) to the given position. 
        """
        
       
        target= PV('target')
        start = PV('start')
        target.put(float(int(position)))
        start.put(1)
            
       
      
    def GetAxisPar(self, axis, name):
        velocity= PV('vel')
                   
                 
        if name == "velocity":
            ans = float(int(vel.get()))   
                         
      
        return ans
    
    def SetAxisPar(self, axis, name, value):
        velocity= PV('vel')
                    
        if name == "velocity":
            vel.put(float(int(value)))
   
   
    def AbortOne(self, axis):
        """
        Abort the axis(motor).
        """
       
        stop = PV('stop')
        stop.put('1')
