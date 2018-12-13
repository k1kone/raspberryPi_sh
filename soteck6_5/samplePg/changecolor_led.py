import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


pwmRed = GPIO.PWM(18, 500)
pwmRed.start(0)

pwmBlue = GPIO.PWM(23, 500)
pwmBlue.start(0)

pwmGreen = GPIO.PWM(24, 500)
pwmGreen.start(0)

while True:
    for b in range(101):
        pwmBlue.ChangeDutyCycle(b)
        time.sleep(0.1)


    for r in range(101):
        pwmRed.ChangeDutyCycle(r)
        time.sleep(0.1)

    for b in range(101):
        pwmBlue.ChangeDutyCycle(100-b)
        time.sleep(0.1)
    pwmBlue.ChangeDutyCycle(0)

    for g in range(101):
        pwmGreen.ChangeDutyCycle(g)
        time.sleep(0.1)
#    pwmGreen.ChangeDutyCycle(0)

    for r in range(101):
        pwmRed.ChangeDutyCycle(100 - r)
        time.sleep(0.1)
    pwmRed.ChangeDutyCycle(0)

    for g in range(101):
        pwmGreen.ChangeDutyCycle(100 - g)
        time.sleep(0.1)
    pwmGreen.ChangeDutyCycle(0)

GPIO.cleanup()
