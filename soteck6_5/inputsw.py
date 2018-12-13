import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    print(GPIO.input(9))
    time.sleep(0.5)


GPIO.clean()
