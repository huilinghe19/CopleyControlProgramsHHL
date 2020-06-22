#!/usr/bin/python3
from time import sleep
import PyTango
from sardana import State, SardanaValue
from sardana.pool.controller import MotorController
from sardana.pool.controller import DefaultValue, Description, FGet, FSet, Type

class TangoDSObject(object):
    def __init__(self, device_name):
        self.name = device_name
        ser = self.connectDevice(device_name)
        self.ser = ser
        
    def connectDevice(self, device_name):    
        """ connects with the device server.
        """
        try:
            dev = PyTango.DeviceProxy(device_name)  
            #print("Device Status:", dev.Status())
            return dev
        except:
            print("ERROR: An exception with connecting DS {} occurred. ".format(device))  
            return 
    
    def getNodeID(self, axis):
        """
        get the node id string from db
        """
        db = PyTango.Database()
        dict_nodeID = db.get_device_property(str(self.name),"NodeId")
        return str(dict_nodeID["NodeId"][0])
    
    def setVariable(self, axis, variable_ID, value):
        """
        set variable
        """
        ser=self.ser
        nodeID = self.getNodeID(axis) 
        setCommandFormat = "{} s r{} {}\n".format(str(nodeID), str(variable_ID), str(int(value)))
        return ser.WriteRead(setCommandFormat)
    
    def getVariable(self, axis, variable_ID):
        """
        get variable
        """
        
        ser = self.ser
        nodeID = self.getNodeID(axis) 
        getCommandFormat = "{} g r{}\n".format(str(nodeID), str(variable_ID))
        return ser.WriteRead("{} g r{}\n".format(str(nodeID), str(variable_ID)))
    
    def getStatus(self):
        """
        get status
        :return:
        """
        ser = self.ser
        ans = ser.Status()
        #print(ans)
        return ans
    
    def getPosition(self):
        ser = self.ser
        ans = ser.position 
        return float(int(ans))

    def getVelocity(self):
        ser = self.ser        
        ans = ser.velocity
        return float(int(ans))

    def getAcceleration(self):
        ser = self.ser
        ans = ser.acceleration
        return float(int(ans))

    def getDeceleration(self):
        ser = self.ser
        ans = ser.deceleration
        return float(int(ans))

    def getStepPerUnit(self):
        ans = 1
        return float(ans)
    #def getCwLimit(self):
	    #ser = self.ser
	    #return float(int(ser.CwLimit))
    def getCcwLimit(self):
        ser = self.ser
        return float(int(ser.CcwLimit))

    def setVelocity(self, value):
        ser = self.ser
        ser.velocity = int(value)

    def setAcceleration(self, value):
        ser = self.ser
        ser.acceleration = int(value)

    def setDeceleration(self, value):
        ser = self.ser
        ser.deceleration = int(value)

    def setStepPerUnit(self):
        raise Exception("step_per_unit is always 1")

    def setPosition(self, value):
        ser = self.ser
        ser.SetPoint = int(value) - int(self.getPosition())
        ser.Position = int(value)
        
    def moveMotor(self, axis):
        """
        move the axis.
        """
        ser=self.ser
        nodeID = self.getNodeID(axis) 
        result = ser.WriteRead("{} t 1\n".format(str(nodeID)))   
        return result
    
    def abortMotor(self, axis):
        """
        abort the axis.
        """
        ser=self.ser
        nodeID = self.getNodeID(axis) 
        ser.WriteRead("{} t 0\n".format(str(nodeID)))   
        
    
        
class CopleyController(MotorController):

    ctrl_properties = \
        {
        
          "Device": {Type : str,
                  Description : "connected device server",
                  DefaultValue : ["stepper/hhl/1","stepper/hhl/2"]},
        	  
        }
    AXIS_NAMES = {1: "stepper/hhl/1", 2: "stepper/hhl/2", 3: "stepper/hhl/3"}
    
    STATES = {"ON": State.On, "MOVING": State.Moving, "STANDBY": State.Standby, "FAULT": State.Fault, "ALARM": State.Alarm}

    def __init__(self, inst, props, *args, **kwargs):
        #MotorController.__init__(self,inst, props, *args, **kwargs)
        super_class = super(CopleyController, self)
        super_class.__init__(inst, props, *args, **kwargs)
        device = self.Device
    def __del__(self):
        del self.copleyController

    def StateOne(self, axis):
        """
        Read the axis state. asix can be 1, 2, 3, 4. One axis is defined as one motor in spock. 
      
        """
        #print "StateOne() Start"
        axis_name = self.AXIS_NAMES[axis]
        copleyController = TangoDSObject(axis_name)
        limit_switches = MotorController.NoLimitSwitch
        try:
            ans = copleyController.getStatus()
            if ans == "Negative limit switch Active":
                state = self.STATES["ALARM"]
                limit_switches |= MotorController.LowerLimitSwitch
            elif ans == "Positive limit switch Active":
                state = self.STATES["ALARM"]
                limit_switches |= MotorController.UpperLimitSwitch
            elif ans == 'Status is STANDBY':
                state = self.STATES["ON"]
                #print "State ON, Motion Stopped"
            elif ans == "Status is MOVING":
                state = self.STATES["MOVING"]
                #print "State MOVING, In Moving"
        except:
            #state = self.STATES["FAULT"]
            pass
        #print("StateOne() finished")
        return state,  limit_switches

    def ReadOne(self, axis):
        """
        Read the position of the axis(motor). When "wa" or "wm motor_name"is called in spock, 
        this method is used. 
        """

        axis_name = self.AXIS_NAMES[axis]
        copleyController = TangoDSObject(axis_name)
        ans = copleyController.getPosition()
        return float(ans)
    def DefinePosition(self, axis, position):
        axis_name = self.AXIS_NAMES[axis]
        copleyController = TangoDSObject(axis_name)
        copleyController.setPosition(position)
        
    def StartOne(self, axis, position):
        """
        Move the axis(motor) to the given position. 
        """
        #print("StartOne() start")
        axis_name = self.AXIS_NAMES[axis]
        copleyController = TangoDSObject(axis_name)
        self.DefinePosition(axis, position)
        copleyController.moveMotor(axis)   
        #print("StartOne() finished")
    def GetAxisPar(self, axis, name):
        axis_name = self.AXIS_NAMES[axis]
        copleyController = TangoDSObject(axis_name)
        name = name.lower()
        if name == "acceleration":
            ans = copleyController.getAcceleration()
        elif name == "deceleration":
            ans = copleyController.getDeceleration()
        elif name == "velocity":
            ans = copleyController.getVelocity()
        elif name == "step_per_unit":
            ans = copleyController.getStepPerUnit()
        return ans
    
    def SetAxisPar(self, axis, name, value):
        """
        Set Axis Parameters
        :param axis:
        :param name:
        :param value:
        :return:
        """
        axis_name = self.AXIS_NAMES[axis]
        copleyController = TangoDSObject(axis_name)
        name = name.lower()
        if name == "acceleration":
            copleyController.setAcceleration(value)                      
        elif name == "deceleration":
            copleyController.setDeceleration(value)                     
        elif name == "velocity":
            copleyController.setVelocity(value) 
        elif name == "step_per_unit":
            copleyController.setStepPerUnit()
        
    def AbortOne(self, axis):
        """
        Abort the axis(motor).
        """
        copleyController = TangoDSObject(axis_name)
        copleyController.abortMotor(axis)