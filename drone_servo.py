from gpiozero import Servo
from time import sleep

# Use GPIO pin 22
servo = Servo(22)

def dropPackage():
    try:
        print('Servo started...')
        sleep(1)
        setAngle(1)  # set to 180 degrees
        sleep(5)
        setAngle(-1)  # set to 0 degrees
    except KeyboardInterrupt:
        print('Servo interrupted..')

def setAngle(position):
    servo.value = position
    sleep(1)

# Start at 0 degrees (equivalent to position -1)
setAngle(-1)
