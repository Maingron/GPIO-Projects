import RPi.GPIO as GPIO
import time


mystate = 0
  
GPIO.setmode(GPIO.BCM) 
GPIO.setup(3, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(3,1)
time.sleep(.00001)
GPIO.output(3,0)
time.sleep(.12)
GPIO.output(3,1)
time.sleep(.0001)
GPIO.output(3,0)

        
def toggleme(mystate):
    if mystate == 1:
        GPIO.output(3,0)
        print("off")
        return 0
    else:
        GPIO.output(3,1)
        print("on")
        return 1

    
while True:
    time.sleep(.02) # Needs a little less CPU time than without the line
    if GPIO.input(15) == 1:
        mystate = toggleme(mystate)
        while GPIO.input(15) == 1:
              time.sleep(0.1) # Make sure we can't press down until the next trigger
        time.sleep(0.25)
        

GPIO.cleanup()

