from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPin=11
GPIO.setup(servoPin,GPIO.OUT)
pwm = GPIO.PWM(servoPin,50)
pwm.start(8)

for i in range(0,20):
    desiredPosition=input("where do want?")
    DC=1./18.*(desiredPosition)+3.
    pwm.ChangeDutyCycle(DC)
    sleep(0.3)
pwm.stop()
GPIO.cleanup()
    
    