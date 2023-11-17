from __future__ import print_function
import time
import sys
import math
import qwiic_scmd

myMotor = qwiic_scmd.QwiicScmd()

def runExample():
    print("test")
    R_MTR = 0
    L_MTR = 1
    FWD = 0
    BWD = 1
    
    
    myMotor.begin()
    print("Motor initialized.")
    time.sleep(.250)
    
    # motor speeds
    myMotor.set_drive(0,0,0)
    myMotor.set_drive(1,0,0)
    
    myMotor.enable()
    print("Motor enabled")
    time.sleep(.250)
    

    speed = 125
       
    print(speed)
    myMotor.set_drive(R_MTR,FWD,speed)
    print(speed)
    myMotor.set_drive(L_MTR,BWD,speed*2)
    time.sleep(.05)

try:
    runExample()
except (KeyboardInterrupt, SystemExit) as exErr:
    print("Ending Example 1")
    myMotor.set_drive(0,0,0)
    myMotor.set_drive(1,0,0)
    sys.exit(0)  
   
        