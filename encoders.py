from __future__ import print_function
import qwiic_dual_encoder_reader
import time
import sys
import pi_servo_hat
def runExample():
    
    print("\nSparoder Reader Example 1\n")
    myEncoders = qwiic_dual_encoder_reader.QwiicDualEncoderReader()
    
    if myEncoders.connected == False:
        print("The Qwiic Dual Encoder Reader Device isn't conneted to the system. pleast check your connection",\
              file=sys.stderr)
        return
    myEncoders.begin()
    
    while True:
        print("Count1: %d" % (myEncoders.get_count1()))
        print("degreegs: %d" % (myEncoders.get_count1()*9))
        print("radians: %s" % (myEncoders.get_count1()*9* (3.14159/180)))
        time.sleep(.3)
if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        