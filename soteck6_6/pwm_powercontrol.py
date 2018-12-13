import tkinter as tk
import tkinter.messagebox
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
pwm_fw = GPIO.PWM(18, 500)
pwm_fw.start(0)

GPIO.setup(23, GPIO.OUT)
pwm_rv = GPIO.PWM(23, 500)
pwm_rv.start(0)

class DCMotor:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.scale = tk.Scale(self.frame, from_=0, to=100, orient='h', command=self.update)
        self.scale.grid(row=0)
        self.button = tk.Button(self.frame, text='FWD', width=3, command=self.motor_dir)
        self.button.grid(row=1)
        self.now_duty=0.0

    def update(self, duty):
        self.now_duty = duty
        if self.button.cget('text') == 'FWD':
            pwm_rv.ChangeDutyCycle(float(0))
            pwm_fw.ChangeDutyCycle(float(duty))
        else:
            pwm_rv.ChangeDutyCycle(float(duty))
            pwm_fw.ChangeDutyCycle(float(0))

    def motor_dir(self):
        print(self.now_duty)
        if float(self.now_duty) < 1:
            if self.button.cget('text') == 'FWD':
                self.button.configure(text='RSV')
            else:
                self.button.configure(text='FWD')
                
    def motor_stop(self):
        pwm_fw.stop()
        pwm_rv.stop()



if __name__ == '__main__':
    def callback():
        if tk.messagebox.askyesno('you want exit?'):
            app.motor_stop()
            root.destroy()
        
    root = tk.Tk()
    root.title('PWM Power Control')
    app = DCMotor(root)
    root.geometry('200x150')
    root.protocol('WM_DELETE_WINDOW', callback)
    root.mainloop()
