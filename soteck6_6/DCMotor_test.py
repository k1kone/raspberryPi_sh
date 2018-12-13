import tkinter as tk
import tkinter.messagebox
from pwm_powercontrol import DCMotor

def callback():
    if tk.messagebox.askyesno('you want exit?'):
        app.stop_motor()
        root.destroy()

root = tk.Tk()
root.title('PWM Power Control')
app = DCMotor(root)
root.geometry('200x150')
root.protocol('WM_DELETE_WINDDOW', callback)
root.mainloop()
