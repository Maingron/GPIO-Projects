import RPi.GPIO as GPIO
import time

# Variables
mystate = 0

# Init GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT) # Our output pin which then controls our NPN Transistor; #! Pin enabled by default = Power on
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Out input pin which checks if our button is pressed; Pull down resistor


# Init animation
GPIO.output(3,1)
time.sleep(.00001)
GPIO.output(3,0)
time.sleep(.12)
GPIO.output(3,1)
time.sleep(.0001)
GPIO.output(3,0)


def toggleme(mystate): # Toggle on or off
    if mystate == 1:
        GPIO.output(3,0)
        print("off")
        return 0
    else:
        GPIO.output(3,1)
        print("on")
        return 1


while True: # Loop
    time.sleep(.02) # Needs less CPU time than without waiting
    if GPIO.input(15) == 1: # If button is pressed
        mystate = toggleme(mystate)
        while GPIO.input(15) == 1:
                time.sleep(0.1) # Make sure we can't press down until the next trigger
        time.sleep(0.25)

GPIO.cleanup()

# Author: Maingron 2021-08