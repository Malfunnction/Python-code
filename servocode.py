import pi_servo_hat
import time

servo = pi_servo_hat.PiServoHat()

servo.restart()

servo.move_servo_position(0, 0)

time.sleep(1)

try:
    servo.set_duty_cycle(3,100)
    while True:
        for i in range(0, 60):
            print(i)
            if(i%10==0):
                servo.move_servo_position(0, i/10*6)
            time.sleep(1)
except (KeyboardInterrupt, SystemExit) as exErr:
    print("\nEnding Example 1")
    sys.exit(0)