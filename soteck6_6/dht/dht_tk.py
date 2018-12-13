import RPi.GPIO as GPIO
import dht11
import time
import datetime
import tkinter as tk

class App:
    def __init__(self, master=None):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.n = datetime.datetime.now().strftime('%H:%M:%S')
        self.l1 = tk.Label(text='time :{}'.format(self.n), font=('Arial','24'))
        self.t = 0
        self.l2 = tk.Label(text='Temperature:{}C'.format(self.t), font=('Arial','24'))
        self.h = 0
        self.l3 = tk.Label(text='Humidity:{}%'.format(self.h), font=('Arial','24'))
        self.l1.pack()
        self.l2.pack()
        self.l3.pack()


    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    def ct(self):
        ins = dht11.DHT11(pin=17)
        result = ins.read()
        if result.is_valid():
           self.t = result.temperature
           self.h = result.humidity
        self.n = datetime.datetime.now().strftime('%H:%M:%S')
        self.l1.configure(text='time :{}'.format(self.n))
        self.l2.configure(text='Temperature:{}C'.format(self.t))
        self.l3.configure(text='Humidity:{}%'.format(self.h))

        print('time :{}'.format(self.n))
        print('Temperature:{}C'.format(self.t))
        print('Humidity:{}%'.format(self.h))

    def show(self):
        self.ct()
        self.master.after(1000, self.show)



if __name__ == '__main__':
    root = tk.Tk()
    root.title('DHT tkinter')
    root.geometry('400x300')
    app = App(root)
    app.show()
    root.mainloop()
