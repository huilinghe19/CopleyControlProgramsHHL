from epics import *
from sardana import State, SardanaValue
from sardana.pool.controller import MotorController
from sardana.pool.controller import DefaultValue, Description, FGet, FSet, Type

          
class CopleyEpicsController(MotorController):

    STATES = {"ON": State.On, "MOVING": State.Moving, "FALUT": State.Fault}

    def __init__(self, inst, props, *args, **kwargs):
        MotorController.__init__(self,inst, props, *args, **kwargs)
        #super_class = super(CopleyController, self)
        #super_class.__init__(inst, props, *args, **kwargs)
        #self.copleyController = TangoDSObject(device)
    #def __del__(self):
        #del self.copleyController

    def StateOne(self, axis):
        """
        Read the axis state. One axis is defined as one motor in spock. 
      
        """
        motorState = int(caget("state"))
        print motorState
        if motorState == 0:
            state = self.STATES["ON"]
        elif motorState == 134217728:
            state = self.STATES["MOVING"]
        else: 
            state = self.STATES["FAULT"]
        limit_switches = MotorController.NoLimitSwitch
        return state, limit_switches

    def ReadOne(self, axis):
        """
        Read the position of the axis(motor). When "wa" or "wm motor_name"is called in spock, this method is used. 
        """
        ans = caget('pos')
        return float(ans)
    
    #def DefinePosition(self, axis, position):
        #caput('target', position)

    def StartOne(self, axis, position):
        """
        Move the axis(motor) to the given position. 
        """ 
       
        caput("move", position)
   
    def AbortOne(self, axis):
        """
        Abort the axis(motor).
        """
        caput('stop', 1)
        
    def GetAxisPar(self, axis, name):
        if name == "velocity":
            ans = float(caget("vel"))  
            
        #elif name == "acceleration":    
        #elif name == "deceleration":
        
        return ans
    
    def SetAxisPar(self, axis, name, value):
        if name == "velocity":
            caput("vel", value) 
        #elif name == "acceleration":
        #elif name == "deceleration":
        

        