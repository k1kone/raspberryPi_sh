import RPi.GPIO as GPIO
import tkinter as tk
import re
from collections import OrderedDict

class App:
    
    pin = (23, 18, 15, 24, 25, 7, 8, 14)
    inp = OrderedDict()
    inp = {0:[1,1,1,1,1,1,1,1],
           1:[0,1,1,0,0,0,0,0], 
           2:[1,1,0,1,1,0,1,0],  
           3:[1,1,1,1,0,0,1,0], 
           4:[0,1,1,0,0,1,1,0], 
           5:[1,0,1,1,0,1,1,0], 
           6:[1,0,1,1,1,1,1,0], 
           7:[1,1,1,0,0,0,0,0], 
           8:[1,1,1,1,1,1,1,0], 
           9:[1,1,1,1,0,1,1,0], 
           'A':[1,1,1,0,1,1,1,0],
           'B':[0,1,1,1,1,0,1,0], 
           'C':[1,0,0,1,1,1,0,0], 
           'D':[0,0,1,1,1,1,1,0], 
           'E':[1,0,0,1,1,1,1,0], 
           'e':[1,1,0,1,1,1,1,0],
           'F':[1,0,0,0,1,1,1,0], 
           'Y':[0,1,1,1,0,1,1,0], 
           '.':[0,0,0,0,0,0,0,1], 
           'clear':[0,0,0,0,0,0,0,0]} 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    def __init__(self, master, title='segment tkinter', x=300, y=400):
        self.master = master
        self.master.title(title)
        self.master.geometry(str(x)+'x'+str(y))
        self.frame =tk.Frame(master)
        self.frame.pack(anchor='w')
        self.create_wedg()
        
    def create_wedg(self):
        inp_sub = OrderedDict()
        inp_sub = self.inp
        for i,j in enumerate(inp_sub.keys()):
            btn = tk.Button(self.frame, text=str(j), width=3)
            btn.bind('<Button>', self.date_push)
            btn.grid(column=i%5, row=i//5)

    def date_push(self, event):
        date_str = event.widget['text']
        print('input key is "{}".'.format(date_str))
        if re.match(r'\d', date_str):
            date_str = int(date_str)
        GPIO.output(self.pin, 0)
        GPIO.output(self.pin, self.inp[date_str])



if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
