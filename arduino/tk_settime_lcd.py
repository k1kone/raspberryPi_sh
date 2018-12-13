import tkinter as tk
import serial, time

class App:
    def __init__(self, master, title='Send to ArduinoClock', x=300, y=200):
        self.con = serial.Serial('/dev/ttyACM0', 9600)
        self.master = master
        self.master.title(title)
        self.master.geometry(str(x) + 'x' + str(y))
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.ent_time = tk.Entry(self.frame)
        self.ent_time.insert(tk.END, 'set time')
        self.ent_time.grid(row=0, column=1)

        self.send_time = tk.Button(self.frame, text='send', width=10, command=self.push_time)
        self.send_time.grid(row=0, column=2)
        
        self.ent_msg = tk.Entry(self.frame)
        self.ent_msg.insert(tk.END, 'set message')
        self.ent_msg.grid(row=1, column=1)

        self.send_msg = tk.Button(self.frame, text='send', width=10, command=self.push_msg)
        self.send_msg.grid(row=1, column=2)

        self.lb = tk.Label(text='時刻設定： a,yyyy,mm,dd,hh,mm,ss\nアラーム： w,hh,mm\nタイマー： t,mm,ss\nメッセージ: m,message', font=('Arial', '9'), justify='left')
        self.lb.pack(fill='both', side='left')

        
    def push_time(self):
        time.sleep(1)
        str_time = str(self.ent_time.get())
        print(str_time)
        buf = bytes(str_time, 'utf-8')
        self.con.write(buf)
        self.ent_time.delete(0, tk.END)

    def push_msg(self):
        time.sleep(1)
        str_msg = str(self.ent_msg.get())
        buf = bytes(str_msg, 'utf-8')
        self.con.write(buf)
        self.ent_msg.delete(0, tk.END)




if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
