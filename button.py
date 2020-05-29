import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(18) == False:
        print "button on"
        os.system("python ./message.py")
        time.sleep(1)
