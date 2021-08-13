import RPi.GPIO as GPIO
import time


mystate = 0
  
GPIO.setmode(GPIO.BCM) 
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(26,0)

        
def toggleme(mystate):
    if mystate == 1:
        GPIO.output(26,0)
        return 0
    else:
        GPIO.output(26,1)
        return 1

    
while True:
    if GPIO.input(21) == 1:
        mystate = toggleme(mystate)
        while GPIO.input(21) == 1:
              time.sleep(0.1) # Make sure we can't press down until the next trigger
        time.sleep(0.2)
        

GPIO.cleanup()

