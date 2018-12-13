import RPi.GPIO as GPIO
import time
import tkinter as tk

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 500)
pwm.start(0)

class DCMoter:
    def __init__(self, master=None):
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.scale = tk.Scale(self.frame, from_=0, to=100, orient='h', command=self.update)
        self.scale.grid(row=0)
        self.btn = tk.Checkbutton()

    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))

if __name__ == '__main__':
    root = tk.Tk()
    root.title('PWM Power Control')
    app = DCMoter(root)
    root.geometry('300x400')
    root.mainloop()
