import RPi.GPIO as GPIO
import time
import tkinter as tk

class App:
    def __init__(self, master=None):
        self.frame = tk.Frame(master)
        self.frame.pack()
        #buff = tk.StringVar()
        #buff.set('0')
        self.l1 = tk.Label(self.frame, text='Distance(cm)', font=('Arial','30','bold'))
        self.l1.pack()
        self.l2 = tk.Label(self.frame, text='0', font=('Arial','30','bold'))
        self.l2.pack()


trigger_pin = 18
echo_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.0001)
    GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count -1

def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 10000)
    start = time.time()
    wait_for_echo(False, 10000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len*340.29/2*100
    distance_in = distance_cm/2.5
    red = 0;
    blue = 0;
    color = ''
    deng = 3
    safe = 10
    befor = 0.0
    if distance_cm >= safe:
        red=0
        blue = 255
        befor = distance_cm
    elif distance_cm >= deng and distance_cm <= safe:
        if distance_cm >= befor:
            red = int(255 - (distance_cm - deng)/(safe - deng)*255)
            blue = int((distance_cm - deng)/(safe - deng)*255)
            befor = distance_cm
        elif distance_cm <= befor:
            red = int((distance_cm - deng)/(safe - deng)*255)
            blue = int(255 - (distance_cm - deng)/(safe - deng)*255)
            befor = distance_cm

    if distance_cm < deng:
        red = 255
        blue = 0
        befor = distance_cm

    print('RGB({}, 0, {})'.format(red, blue))
    color = '#{:02x}{:02x}{:02x}'.format(red,0,blue)     
    return distance_cm, color

if __name__ == '__main__':
    
    def show():
        #app.buff = str(get_distance())
        t = get_distance()
        app.l2.configure(text='{:.2f}'.format(t[0]), fg=t[1]) 
        #app.l2.configure(background=t[1]) 
        root.after(1000, show)


    root = tk.Tk()
    root.title('pulse senser display Tkinter')
    root.geometry('300x400')
    app = App(root)
    show()
    root.mainloop()

