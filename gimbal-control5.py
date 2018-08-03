import sys
sys.path.append(r"C:\Users\Justin Hai\AppData\Local\Programs\Python\Python36-32\Lib\site-packages")
import serial
import clr
import MissionPlanner
clr.AddReference("MAVLink")
from System import Byte
import MAVLink
from MAVLink import mavlink_command_long_t
import MAVLink
import time
#Controlling the Servo
#Use doCommand->sends a "do" command to Pixhawk
#MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, SERVO OUTPUT #, PWM, N/A, N/A, N/A, N/A, N/A)

ser=serial.Serial('COM7', 9600) #May need to change this COM 
min_pwm=553 #pwm value of left-most rotation
max_pwm=2250
#pwm value of right-most rotation
max_voltage=5.0
slope=(max_pwm-min_pwm)/max_voltage
counter = 0

while True:
    #1. Read serial line
    a=ser.readline()
    
    #2. Decode
    voltage=float(a.decode('utf-8'))
    print(voltage)
    #3. See if there was any change
    #3A. Figure out which servo needs to be changed using identifier
    '''Identifier:
        1: bLval (mapped to channel 9)
        2: bRval (mapped to channel 10)
        3: TLval (mapped to channel 11)
        4: TCval (mapped to channel 12)
        5: TRval (mapped to channel 13)
    '''
    identifier = voltage//10
    print ("Identifier: ", identifier) 
    
    #3B. Write to the relevant channel based on identifier
    #Take remainder of dividing voltage by 10 (releases identifier)
    try:
        pwm=min_pwm+(voltage%10)*slope
        MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO, (8 + identifier), pwm, 0, 0, 0, 0, 0);

    except ValueError:
        bbb=1
     
    #Housekeeping    
    print(counter)
    print (voltage)
    counter +=1