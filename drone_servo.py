#import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

servo = 22

#GPIO.setmode(GPIO.BOARD)

#GPIO.setup(servo,GPIO.OUT)
#p = GPIO.PWM(servo,50)# 50hz frequency


def dropPackage():
  try:
    time.sleep(5)
    print('Servo started...')
    # time.sleep(1)
    # setAngle(180)
    # time.sleep(5)
    # setAngle(0 )
    # p.stop()
    # GPIO.cleanup()
  except KeyboardInterrupt:
    print('Servo error..')
    # p.stop()
    # GPIO.cleanup()

# def setAngle(angle):
#     duty = angle / 18 + 3
#     p.ChangeDutyCycle(duty)
#     time.sleep(1)
    
# p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )
