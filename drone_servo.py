from gpiozero import AngularServo
from time import sleep

# Use GPIO pin 22
servo = AngularServo(22, min_angle=0, max_angle=180)

def dropPackage():
    try:
        print('Servo started...')
        sleep(1)
        setAngle(180)  # set to 180 degrees
        sleep(5)
        setAngle(0)    # set to 0 degrees
    except KeyboardInterrupt:
        print('Servo interrupted..')

def setAngle(angle):
    servo.angle = angle
    sleep(1)

# Start at 0 degrees
setAngle(0)
