import tkinter as tk
import datetime
import time
import serial
import ast
from tkinter import messagebox
from mo_getmail import getmail
 
class App(getmail):
	
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        #時刻設定
        self.frame1 = tk.LabelFrame(master, text='時刻設定')
        self.frame1.pack(anchor='w')
        self.date_time = tk.StringVar()
        self.date_time.set('')
        #時刻設定Spinboxの生成
        tk.Label(self.frame1,textvariable=self.date_time ,width=15).grid(row=0, column=0)
        
        #設定ボタンの生成
        self.submit1 = tk.Button(self.frame1,text='設定',width=4,command=self.asubmit)
        self.submit1.grid(row=0,column=7)
        
        #アラーム設定
        self.frm_alarm = tk.LabelFrame(master, text='アラーム　時　　分')
        self.frm_alarm.pack(anchor='w')
        tk.Label(self.frm_alarm, text='　　　　').grid(row=0, column=0)
        self.alm_hh_spin = tk.Spinbox(self.frm_alarm, from_= 0, to= 23, increment=1, width=2)
        self.alm_mm_spin = tk.Spinbox(self.frm_alarm, from_= 0, to= 60, increment=1, width=2)
        self.alm_hh_spin.grid(row=0,column=1)
        self.alm_mm_spin.grid(row=0,column=2)
 
        #設定ボタンの生成
        self.submit1 = tk.Button(self.frm_alarm,text='設定',width=4,command=self.wsubmit)
        self.submit1.grid(row=0,column=7)
        
        #タイマー設定
        self.frm_timer = tk.LabelFrame(master, text='タイマー　分　　秒')
        self.frm_timer.pack(anchor='w')
        tk.Label(self.frm_timer, text='　　　　').grid(row=0, column=0)
        self.tm_mm_spin = tk.Spinbox(self.frm_timer, from_= 0, to= 23, increment=1, width=2)
        self.tm_ss_spin = tk.Spinbox(self.frm_timer, from_= 0, to= 60, increment=1, width=2)
        self.tm_mm_spin.grid(row=0,column=1)
        self.tm_ss_spin.grid(row=0,column=2)
 
        #設定ボタンの生成
        self.submit1 = tk.Button(self.frm_timer,text='設定',width=4,command=self.tsubmit)
        self.submit1.grid(row=0,column=7)
        
        #Humidity & Temparature
        self.dht_val = tk.StringVar()
        self.dht_val.set('')
        self.frm_dht = tk.LabelFrame(master, text = '湿度 温度')
        self.frm_dht.pack(anchor = 'w')
        tk.Label(self.frm_dht, textvariable = self.dht_val, width=15).grid(row=0, column=0)
 
        #読取ボタンの生成
        submit = tk.Button(self.frm_dht,text='読取',width=4,command=self.dht_submit)
        submit.grid(row=0,column=1)
        
        #メッセージEditBox
        self.frm_msg = tk.LabelFrame(master,text='メッセージ：')
        self.frm_msg.pack(anchor='w')
        self.msgEditBox = tk.Entry(self.frm_msg, width=40)
        self.msgEditBox.grid(row=0,column=0)
        self.submit2 = tk.Button(self.frm_msg,text='送信',width=4,command=self.m_submit)
        self.submit2.grid(row=0, column=1)
        
        self.con = serial.Serial('/dev/ttyACM0',9600)
        # ArduinoClockの初期化終了待ち
        time.sleep(5)
        self.mailCheck()

    def mailCheck(self):
        mc = self.main()        
        cmd = 'm,' + mc +'\n'
        buf = bytes(cmd,'utf-8')
        self.con.write(buf)
        self.master.after(10*1000, self.mailCheck)
       

    #時刻設定「設定」ボタン処理    
    def asubmit(self):
        d= datetime.datetime.now()
        cmd = d.strftime('a,%Y,%m,%d,%H,%M,%S') + '\n'
        buf = bytes(cmd,'utf-8')
        self.con.write(buf)
        print(buf)
        time.sleep(1)
        self.con.write(bytes('r\n','utf-8'))
        buf = self.con.readline()
        print(buf)
        ardclk = ast.literal_eval(buf.decode())
        self.date_time.set(ardclk['RTC'])
    
    #アラーム設定「設定」ボタン処理
    def wsubmit(self):
        try:
            #walmを strptime使って「文字列」から「日付」に変換する
            #変換できない場合(9:60など)は例外が発生する
            walm = '{}:{}'.format(self.alm_hh_spin.get(),self.alm_mm_spin.get())
            walm_correct = time.strptime(walm,'%H:%M')
 
        except ValueError:
            print("Alarm Value Error!")
            return
 
        cmd = 'w,' + self.alm_hh_spin.get() + ',' + self.alm_mm_spin.get() + '\n'
        buf = bytes(cmd, 'utf-8')
        self.con.write(buf)
        print(buf)
 
    #タイマー設定「設定」ボタン処理
    def tsubmit(self):
        try:
            #設定値が範囲外の場合raiseで例外を発生させる
            mm = int(self.tm_mm_spin.get())
            if (0 <= mm < 60) == False:
                raise ValueError('分の設定が範囲を超えています')
            ss = int(self.tm_ss_spin.get())
            if (0 <= ss < 60) == False:
                raise ValueError('秒の設定が範囲を超えています')
        except ValueError as e:
            messagebox.showerror('ArdClock',str(e))
            print(str(e))
            return
        
        cmd = 't,' + str(mm) + ',' + str(ss) + '\n'
        buf = bytes(cmd, 'utf-8')
        self.con.write(buf)
        print(buf)
            
    def m_submit(self):
        cmd = 'm,' + self.msgEditBox.get() +'\n'
        buf = bytes(cmd,'utf-8')
        self.con.write(buf)
        
    def dht_submit(self):
        self.con.write(bytes('r\n','utf-8'))
        buf = self.con.readline()
        print(buf)
        ardclk = ast.literal_eval(buf.decode())
#        rh_tmp = '湿度:'+str(ardclk['RH'])+'温度' + str(ardclk['TMP'])
        rh_tmp = '湿度:{:.0f}% 温度:{:.0f}℃'.format(ardclk['RH'],ardclk['TMP'])
        print(rh_tmp)
        self.dht_val.set(rh_tmp)
 
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('ArdClock')
    app = App(master=root)
    root.geometry("400x300+730+360")
    root.mainloop()
