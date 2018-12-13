import RPi.GPIO as GPIO
import time
import tkinter as tk

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 500)
pwm.start(0)

GPIO.setup(23, GPIO.OUT)
pwm2 = GPIO.PWM(23, 500)
pwm2.start(0)

class DCMoter:
    def __init__(self, master=None):
        self.chk = tk.BooleanVar()
        self.num = 0.0
        self.scale = tk.Scale(from_=0, to=100, orient='h', command=self.update)
        self.scale.grid(row=0)
        self.btn = tk.Checkbutton(variable=self.chk, text='reverse on/off', command=self.c_spin)
        self.scale.pack()
        self.btn.pack()

    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))
        self.num = duty

    def c_spin(self):
        if float(self.num) < 1:
            if self.chk.get() is True:
                print('true','chk is {}'.format(self.chk.get()))
                pwm.ChangeDutyCycle(float(0))
                pwm2.ChangeDutyCycle(float(duty))
            elif self.chk.get() is False:
                print('false','chk is {}'.format(self.chk.get()))
                pwm.ChangeDutyCycle(float(duty))
                pwm2.ChangeDutyCycle(float(0))



if __name__ == '__main__':
    root = tk.Tk()
    root.title('PWM Power Control')
    app = DCMoter(root)
    root.geometry('300x400')
    root.mainloop()
