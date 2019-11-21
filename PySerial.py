#	"$Name: not supported by cvs2svn $";
#	"$Header: /users/chaize/newsvn/cvsroot/Communication/PySerialLine/src/PySerial.py,v 1.1 2007-09-20 12:24:37 jribas Exp $";
#=============================================================================
#
# file :        PySerial.py
#
# description : Python source for the PySerial and its commands. 
#                The class is derived from Device. It represents the
#                CORBA servant object which will be accessed from the
#                network. All commands which can be executed on the
#                PySerial are implemented in this file.
#
# project :     TANGO Device Server
#
# $Author: jribas $
#
# $Revision: 1.1 $
#
# $Log: not supported by cvs2svn $
# Revision 1.2  2007/07/09 09:44:03  jribas
# - Modify serial port values while the port is open. Apply changes when the port is open again. Read the current configuration values and the written values.
#
# Revision 1.1  2007/07/06 13:15:04  jribas
# *** empty log message ***
#
#
# copyleft :    European Synchrotron Radiation Facility
#               BP 220, Grenoble 38043
#               FRANCE
#
#=============================================================================
#  		This file is generated by POGO
#	(Program Obviously used to Generate tango Object)
#
#         (c) - Software Engineering Group - ESRF
#=============================================================================
#


import PyTango
import sys
import serial
import array
import io
import unicodedata
#==================================================================
#   PySerial Class Description:
#
#         Python Serial Line device server for  windows and linux
#
#==================================================================
# 	Device States Description:
#
#   DevState.ON :     Serial Port Open
#   DevState.FAULT :
#   DevState.OFF :
#==================================================================


class PySerial(PyTango.Device_4Impl):

#--------- Add you global variables here --------------------------
	PARITIES = ["none", "odd" , "even"]
	FLOWCONTROL = ["none" , "software", "hardware", "sw/hw"]
	TERMINATOR = ["LF/CR", "CR/LF", "CR", "LF", "NONE"]
	TERMINATORCHAR = ["\n\r", "\r\n", "\r", "\n", ""]
	
#------------------------------------------------------------------
#	Device constructor
#------------------------------------------------------------------
	def __init__(self,cl, name):
		PyTango.Device_4Impl.__init__(self,cl,name)

		self.configure = True
		self.serial = serial.Serial()

		self.baudrate = 9600
		self.serial.baudrate = self.baudrate
        
		#self.port = PySerial.serialScan()
		self.port = "/dev/ttyS0"
		self.serial.port = self.port
		
		self.bytesize = 8
		self.serial.bytesize = self.bytesize
		
		self.parity = PySerial.PARITIES[0]
		self.current_parity = self.parity
		self.serial.parity = serial.PARITY_NONE

		self.stopbits = 1
		self.serial.stopbits = self.stopbits

		self.timeout = 0
		self.serial.timeout = self.timeout
		
		self.flowcontrol = PySerial.FLOWCONTROL[0]
		self.current_flowcontrol = self.flowcontrol
		self.serial.xonxoff = 0
		self.serial.rtscts = 0

		self.terminator = PySerial.TERMINATOR[0]
		self.terminatorchar = PySerial.TERMINATORCHAR[0]
		PySerial.init_device(self)

#------------------------------------------------------------------
#	Device destructor
#------------------------------------------------------------------
	def delete_device(self):
		print "[Device delete_device method] for device",self.get_name()


#------------------------------------------------------------------
#	Device initialization
#------------------------------------------------------------------
	def init_device(self):
		print "In ", self.get_name(), "::init_device()"
		self.set_state(PyTango.DevState.OFF)
		self.get_device_properties(self.get_device_class())

#------------------------------------------------------------------
#	Always excuted hook method
#------------------------------------------------------------------
	def always_executed_hook(self):
		print "In ", self.get_name(), "::always_excuted_hook()"


#---- Aux Methods ----
	def serialScan():
		for i in range(256):
			try:
				s = serial.Serial(i)
				#available.append( (i, s.portstr))
				s.close()   #explicit close 'cause of delayed GC in java
				return s.portstr
			except serial.SerialException:
				pass
		return ""
    
	serialScan = staticmethod(serialScan)

#==================================================================
#
#	PySerial read/write attribute methods
#
#==================================================================
#------------------------------------------------------------------
#	Read Attribute Hardware
#------------------------------------------------------------------
	def read_attr_hardware(self,data):
		print "In ", self.get_name(), "::read_attr_hardware()"



#------------------------------------------------------------------
#	Read Port attribute
#------------------------------------------------------------------
	def read_Port(self, attr):
		print "In ", self.get_name(), "::read_Port()"
		
		#	Add your own code here
		attr_Port_read = self.serial.port
		attr.set_value(attr_Port_read)


#------------------------------------------------------------------
#	Write Port attribute
#------------------------------------------------------------------
	def write_Port(self, attr):
		print "In ", self.get_name(), "::write_Port()"
		data=[]
		attr.get_write_value(data)
		print "Attribute value = ", data
        
		#	Add your own code here
		self.port = data[0]
		self.configure = True


#---- Port attribute State Machine -----------------
	def is_Port_allowed(self, req_type):
			#	End of Generated Code
			#	Re-Start of Generated Code
		return True


#------------------------------------------------------------------
#	Read Baudrate attribute
#------------------------------------------------------------------
	def read_Baudrate(self, attr):
		print "In ", self.get_name(), "::read_Baudrate()"
		
		#	Add your own code here
		
		attr_Baudrate_read = self.serial.baudrate
		attr.set_value(attr_Baudrate_read)


#------------------------------------------------------------------
#	Write Baudrate attribute
#------------------------------------------------------------------
	def write_Baudrate(self, attr):
		print "In ", self.get_name(), "::write_Baudrate()"
		data=[]
		attr.get_write_value(data)
		print "Attribute value = ", data
		#	Add your own code here
		self.baudrate = data[0]
		self.configure = True

#---- Baudrate attribute State Machine -----------------
	def is_Baudrate_allowed(self, req_type):
			#	End of Generated Code
			#	Re-Start of Generated Code
		return True


#------------------------------------------------------------------
#	Read DataBits attribute
#------------------------------------------------------------------
	def read_DataBits(self, attr):
		print "In ", self.get_name(), "::read_DataBits()"
		
		#	Add your own code here
		
		attr_DataBits_read = self.serial.bytesize
		attr.set_value(attr_DataBits_read)


#------------------------------------------------------------------
#	Write DataBits attribute
#------------------------------------------------------------------
	def write_DataBits(self, attr):
		print "In ", self.get_name(), "::write_DataBits()"
		data=[]
		attr.get_write_value(data)
		print "Attribute value = ", data

		#	Add your own code here
		self.bytesize = data[0]
		self.configure = True

#---- DataBits attribute State Machine -----------------
	def is_DataBits_allowed(self, req_type):
			#	End of Generated Code
			#	Re-Start of Generated Code
		return True


#------------------------------------------------------------------
#	Read StopBits attribute
#------------------------------------------------------------------
	def read_StopBits(self, attr):
		print "In ", self.get_name(), "::read_StopBits()"
		
		#	Add your own code here
		
		attr_StopBits_read = self.serial.stopbits
		attr.set_value(attr_StopBits_read)


#------------------------------------------------------------------
#	Write StopBits attribute
#------------------------------------------------------------------
	def write_StopBits(self, attr):
		print "In ", self.get_name(), "::write_StopBits()"
		data=[]
		attr.get_write_value(data)
		print "Attribute value = ", data

		#	Add your own code here
		self.stopbits = data[0]
		self.configure = True

#---- StopBits attribute State Machine -----------------
	def is_StopBits_allowed(self, req_type):
			#	End of Generated Code
			#	Re-Start of Generated Code
		return True


#------------------------------------------------------------------
#	Read Terminator attribute
#------------------------------------------------------------------
	def read_Terminator(self, attr):
		print "In ", self.get_name(), "::read_Terminator()"
		
		#	Add your own code here
		
		attr_Terminator_read = self.terminator
		attr.set_value(attr_Terminator_read)


#------------------------------------------------------------------
#	Write Terminator attribute
#------------------------------------------------------------------
	def write_Terminator(self, attr):
		print "In ", self.get_name(), "::write_Terminator()"
		data=[]
		attr.get_write_value(data)
		print "Attribute value = ", data
		
		#	Add your own code here
		
		data[0] = data[0].upper()
		if data[0] in PySerial.TERMINATOR:
			self.terminator = data[0]
			self.terminatorchar = PySerial.TERMINATORCHAR[PySerial.TERMINATOR.index(data[0])]
		else: 
			PyTango.Except.throw_exception("PySerial_write_Terminator", "Allowed terminator values are CR/LF, CR, LF", "write_Terminator()")


#---- Terminator attribute State Machine -----------------
	def is_Terminator_allowed(self, req_type):
			#	End of Generated Code
			#	Re-Start of Generated Code
		return True


#------------------------------------------------------------------
#	Read FlowControl attribute
#------------------------------------------------------------------
	def read_FlowControl(self, attr):
		print "In ", self.get_name(), "::read_FlowControl()"
		
		#	Add your own code here
		
		attr_FlowControl_read = self.current_flowcontrol
		attr.set_value(attr_FlowControl_read)


#------------------------------------------------------------------
#	Write FlowControl attribute
#------------------------------------------------------------------
	def write_FlowControl(self, attr):
		print "In ", self.get_name(), "::write_FlowControl()"
		data=[]
		attr.get_write_value(data)
		print "Attribute value = ", data

		#	Add your own code here
		data[0] = data[0].lower()
		if data[0] in PySerial.FLOWCONTROL:
			self.flowcontrol = data[0]
			self.configure = True	
		else:
			PyTango.Except.throw_exception("PySerial_write_FlowControl", "Allowed flow control values are none, software, hardware and sw/hw", "write_FlowControl()")



#---- FlowControl attribute State Machine -----------------
	def is_FlowControl_allowed(self, req_type):
			#	End of Generated Code
			#	Re-Start of Generated Code
		return True


#------------------------------------------------------------------
#	Read Timeout attribute
#------------------------------------------------------------------
	def read_Timeout(self, attr):
		print "In ", self.get_name(), "::read_Timeout()"
		
		#	Add your own code here
		
		attr_Timeout_read = int(self.serial.timeout * 1000)
		attr.set_value(attr_Timeout_read)


#------------------------------------------------------------------
#	Write Timeout attribute
#------------------------------------------------------------------
	def write_Timeout(self, attr):
		print "In ", self.get_name(), "::write_Timeout()"
		data=[]
		attr.get_write_value(data)
		print "Attribute value = ", data

		#	Add your own code here
		if data[0] == 0:
			self.timeout = 0
		else:
			self.timeout = float(data[0])/1000
		self.configure = True

#---- Timeout attribute State Machine -----------------
	def is_Timeout_allowed(self, req_type):
			#	End of Generated Code
			#	Re-Start of Generated Code
		return True


#------------------------------------------------------------------
#	Read Parity attribute
#------------------------------------------------------------------
	def read_Parity(self, attr):
		print "In ", self.get_name(), "::read_Parity()"
		
		#	Add your own code here

		attr_Parity_read = self.current_parity
		attr.set_value(attr_Parity_read)


#------------------------------------------------------------------
#	Write Parity attribute
#------------------------------------------------------------------
	def write_Parity(self, attr):
		print "In ", self.get_name(), "::write_Parity()"
		data=[]
		attr.get_write_value(data)
		print "Attribute value = ", data

		#	Add your own code here
		data[0] = data[0].lower()
		if data[0] in PySerial.PARITIES:
			self.parity = data[0]
			self.configure = True
		else:
			PyTango.Except.throw_exception("PySerial_write_Parity", "Allowed parity values are none, odd, even", "write_Parity()")

			



#---- Parity attribute State Machine -----------------
	def is_Parity_allowed(self, req_type):
			#	End of Generated Code
			#	Re-Start of Generated Code
		return True


#------------------------------------------------------------------
#	Read InputBuffer attribute
#------------------------------------------------------------------
	def read_InputBuffer(self, attr):
		print "In ", self.get_name(), "::read_InputBuffer()"
		
		#	Add your own code here
		try:
			attr_InputBuffer_read = self.serial.inWaiting()
			attr.set_value(attr_InputBuffer_read)
		except:
			pass


#---- InputBuffer attribute State Machine -----------------
	def is_InputBuffer_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.FAULT,
		                        PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True



#==================================================================
#
#	PySerial command methods
#
#==================================================================

#------------------------------------------------------------------
#	Open command:
#
#	Description: Open serial port
#                
#------------------------------------------------------------------
	def Open(self):
		print "In ", self.get_name(), "::Open()"
		#	Add your own code here
		self.port = '/dev/ttyS0'
		# configure port
		if self.configure:
			self.serial.baudrate = self.baudrate
			self.serial.port = self.port
			self.serial.bytesize = self.bytesize
			self.serial.stopbits = self.stopbits
			
			self.serial.timeout = self.timeout
			self.current_flowcontrol = self.flowcontrol
			if self.current_flowcontrol == "none":
				self.serial.xonxoff = 0
				self.serial.rtscts = 0
			elif self.current_flowcontrol == "software":
				self.serial.xonxoff = 1
				self.serial.rtscts = 0
			elif self.current_flowcontrol == "hardware":
				self.serial.xonxoff = 0
				self.serial.rtscts = 1
			elif self.current_flowcontrol == "sw/hw":
				self.serial.xonxoff = 1
				self.serial.rtscts = 1

			self.current_parity = self.parity				
			if self.current_parity == PySerial.PARITIES[0]:
				self.serial.parity = serial.PARITY_NONE
			elif dself.current_parity == PySerial.PARITIES[1]:
				self.serial.parity = serial.PARITY_ODD
			elif self.current_parity == PySerial.PARITIES[1]:
				self.serial.parity = serial.PARITY_EVEN

			
		self.serial.open()
		self.set_state(PyTango.DevState.ON)
		self.configure = False


#---- Open command State Machine -----------------
	def is_Open_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.FAULT]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Close command:
#
#	Description: Close serial line
#                
#------------------------------------------------------------------
	def Close(self):
		print "In ", self.get_name(), "::Close()"
		#	Add your own code here
		try:
			self.serial.close()
			self.set_state(PyTango.DevState.OFF)
		except:
			pass


#---- Close command State Machine -----------------
	def is_Close_allowed(self):
		if self.get_state() in [PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	FlushInput command:
#
#	Description: 
#------------------------------------------------------------------
	def FlushInput(self):
		print "In ", self.get_name(), "::FlushInput()"
		#	Add your own code here
		try:
			self.serial.flushInput()
		except:
			pass


#---- FlushInput command State Machine -----------------
	def is_FlushInput_allowed(self):
		if self.get_state() in [PyTango.DevState.FAULT,
		                        PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	FlushOutput command:
#
#	Description: 
#------------------------------------------------------------------
	def FlushOutput(self):
		print "In ", self.get_name(), "::FlushOutput()"
		#	Add your own code here
		try:
			self.serial.flushOutput()
		except:
			pass


#---- FlushOutput command State Machine -----------------
	def is_FlushOutput_allowed(self):
		if self.get_state() in [PyTango.DevState.FAULT,
		                        PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Write command:
#
#	Description: Write the string to the serial line
#                
#	argin:  DevString	
#------------------------------------------------------------------
	def Write(self, argin):
		print "In ", self.get_name(), "::Write()"
		#	Add your own code here
		#print "char array ", argin
		#s = array.array('B', argin).tostring()
		#value = s + self.terminatorchar
		#print "string " ,value
		#self.serial.write(value)

		print "string " , argin
		self.serial.write(argin+ '\n')

#---- Write command State Machine -----------------
	def is_Write_allowed(self):
		if self.get_state() in [PyTango.DevState.FAULT,
		                        PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
            
       
		return True


#-----------------------------------------------------------------
#	Read command:
#
#	Description: 
#	argin:  DevUShort	Characters to read
#	argout: DevString	Characters readed
#----------------------------------------------------------------
	def Read(self, argin):
		print "In ", self.get_name(), "::Read()"
		#	Add your own code here
		argout =  []
		s = self.serial.read(argin)
		print s
		#b = array.array('B', s)
		#argout = b.tolist()
		return s
    



#---- Read command State Machine -----------------
	def is_Read_allowed(self):
		if self.get_state() in [PyTango.DevState.FAULT,
		                        PyTango.DevState.OFF]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	ReadLine command:
#
#	Description: 
#	argout: DevVarCharArray Characters readed
#------------------------------------------------------------------
	def ReadLine(self):
		print "In ", self.get_name(), "::ReadLine()"
#	Add your own code here
		### this is old code, in which eol is not supported any more. Use unicodedata instead.
		#argout =  []
		#s = self.serial.readline(eol=self.terminatorchar)
		#print s
		#b = array.array('B', s)
		#argout = b.tolist()
		#return argout
		### old code to end
        
		sio = io.TextIOWrapper(io.BufferedRWPair(self.serial, self.serial))
		sio.flush() # it is buffering. required to get the data out *now*
		s = sio.readline()
		argoutstring = unicodedata.normalize('NFKD', s).encode('ascii','ignore')      
		b = array.array('B', argoutstring)
		argout = b.tolist()
		return argout


#---- ReadLine command State Machine -----------------
	def is_ReadLine_allowed(self):
		if self.get_state() in [PyTango.DevState.FAULT,
		                        PyTango.DevState.OFF]:
			#	End of Generated Code
			#self.Open()
			#	Re-Start of Generated Code
			return False
		return True

#---- Aux Methods ----
	def serialScan():
		for i in range(256):
			try:
				s = serial.Serial(i)
				#available.append( (i, s.portstr))
				s.close()   #explicit close 'cause of delayed GC in java
				return s.portstr
			except serial.SerialException:
				pass
		return ""
    
	serialScan = staticmethod(serialScan)
#==================================================================
#
#	PySerialClass class definition
#
#==================================================================
class PySerialClass(PyTango.DeviceClass):

	#	Class Properties
	class_property_list = {
		}


	#	Device Properties
	device_property_list = {
		}


	#	Command definitions
	cmd_list = {
		'Open':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'Close':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'FlushInput':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'FlushOutput':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'Write':
			[[PyTango.DevString, ""],
			[PyTango.DevVoid, ""]],
		'Read':
			[[PyTango.DevUShort, "Characters to read"],
			[PyTango.DevString, "Characters readed"]],
		'ReadLine':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVarCharArray, "Characters readed"]],
		}


	#	Attribute definitions
	attr_list = {
		'Port':
			[[PyTango.DevString,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'Memorized':"true",
			} ],
		'Baudrate':
			[[PyTango.DevShort,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'label':"Baudrate",
				'Memorized':"true",
			} ],
		'DataBits':
			[[PyTango.DevShort,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'label':"DataBits",
				'max value':8,
				'min value':5,
				'Memorized':"true",
			} ],
		'StopBits':
			[[PyTango.DevShort,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'label':"StopBits",
				'max value':2,
				'min value':1,
				'description':"1\n2\n",
				'Memorized':"true",
			} ],
		'Terminator':
			[[PyTango.DevString,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'description':"CR\nLF\nCR/LF\nNONE",
				'Memorized':"true",
			} ],
		'FlowControl':
			[[PyTango.DevString,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'label':"FlowControl",
				'description':"none\nhardware\nsoftware",
				'Memorized':"true",
			} ],
		'Timeout':
			[[PyTango.DevShort,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'label':"Timeout",
				'min value':0,
				'description':"timeout=None            #wait forever\ntimeout=0               #non-blocking mode (return immediately on read)\ntimeout=x               #set timeout to x miliseconds (float allowed)",
				'Memorized':"true",
			} ],
		'Parity':
			[[PyTango.DevString,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'description':"none\nodd\neven",
				'Memorized':"true",
			} ],
		'InputBuffer':
			[[PyTango.DevLong,
			PyTango.SCALAR,
			PyTango.READ]],
		}


#------------------------------------------------------------------
#	PySerialClass Constructor
#------------------------------------------------------------------
	def __init__(self, name):
		PyTango.DeviceClass.__init__(self, name)
		self.set_type(name);
		print "In PySerialClass  constructor"

#==================================================================
#
#	PySerial class main method
#
#==================================================================


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(PySerialClass,PySerial,'PySerial')
        #----- PROTECTED REGION ID(Socket.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Socket.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
   
