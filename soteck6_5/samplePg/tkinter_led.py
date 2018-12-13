import RPi.GPIO as GPIO
import time
import tkinter as tk


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


root = tk.Tk()
root.title('Tkinter and raspy')
root.geometry('800x500')

red = tk.IntVar()
red.set(0)
blue = tk.IntVar()
blue.set(0)
green = tk.IntVar()
green.set(0)

def change_color(n):
    pwmRed.ChangeDutyCycle(red.get())
    pwmBlue.ChangeDutyCycle(blue.get())
    pwmGreen.ChangeDutyCycle(green.get())
    

s1 = tk.Scale(root, label='red', orient='h', from_=0, to=100, variable=red, command=change_color)

s2 = tk.Scale(root, label='blue', orient='h', from_=0, to=100, variable=blue, command=change_color)

s3 = tk.Scale(root, label='green', orient='h', from_=0, to=100, variable=green, command=change_color)


s1.pack(fill='both')
s2.pack(fill='both')
s3.pack(fill='both')

root.mainloop()


"""
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
"""

GPIO.cleanup()
