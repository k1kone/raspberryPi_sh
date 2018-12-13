import RPi.GPIO as GPIO
import tkinter as tk
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(2.5)

root = tk.Tk()
root.title('Servo Motor Control')
root.geometry('200x400')
v=tk.IntVar()
v.set(0)

def change_angle():
    duty = float(v.get()/20/+2.5)
    pwm.ChangeDutyCycle(duty)
    print(duty)




rd1 = tk.Radiobutton(text="Left", variable=v, value=0, command=change_angle)
rd2 = tk.Radiobutton(text="Center", variable=v, value=90, command=change_angle)
rd3 = tk.Radiobutton(text="Right", variable=v, value=180, command=change_angle)

rd1.pack()
rd2.pack()
rd3.pack()

root.mainloop()

