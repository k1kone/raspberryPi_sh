import tkinter as tk
import datetime
import time
import serial
import ast
 
class App:
	
    def __init__(self, master=None):
        self.master = master
        #時刻設定
        self.frame1 = tk.LabelFrame(master, text='時刻設定　　 年　　月　　日　　時　　分　　秒')
        self.frame1.pack(anchor='w')
 
        #時刻設定Spinboxの生成
        tk.Label(self.frame1,text='　　　　').grid(row=0, column=0)
        self.yy_spin = tk.Spinbox(self.frame1, from_=2018, to= 2028, increment=1, width=4)
        self.mn_spin = tk.Spinbox(self.frame1, from_= 1, to= 12, increment=1, width=2)
        self.dd_spin = tk.Spinbox(self.frame1, from_= 1, to= 31, increment=1, width=2)
        self.hh_spin = tk.Spinbox(self.frame1, from_= 0, to= 23, increment=1, width=2)
        self.mm_spin = tk.Spinbox(self.frame1, from_= 0, to= 60, increment=1, width=2)
        self.ss_spin = tk.Spinbox(self.frame1, from_= 0, to= 60, increment=1, width=2)
        self.yy_spin.grid(row=0,column=1)
        self.mn_spin.grid(row=0,column=2)
        self.dd_spin.grid(row=0,column=3)
        self.hh_spin.grid(row=0,column=4)
        self.mm_spin.grid(row=0,column=5)
        self.ss_spin.grid(row=0,column=6)
        
        #設定ボタンの生成
        submit = tk.Button(self.frame1,text='設定',width=4,command=self.asubmit)
        submit.grid(row=0,column=7)
        
        #アラーム設定
        self.frm_alarm = tk.LabelFrame(master, text='アラーム　時　　分')
        self.frm_alarm.pack(anchor='w')
        tk.Label(self.frm_alarm, text='　　　　').grid(row=0, column=0)
        self.alm_hh_spin = tk.Spinbox(self.frm_alarm, from_= 0, to= 23, increment=1, width=2)
        self.alm_mm_spin = tk.Spinbox(self.frm_alarm, from_= 0, to= 60, increment=1, width=2)
        self.alm_hh_spin.grid(row=0,column=1)
        self.alm_mm_spin.grid(row=0,column=2)
 
        #設定ボタンの生成
        submit = tk.Button(self.frm_alarm,text='設定',width=4,command=self.wsubmit)
        submit.grid(row=0,column=7)
        
        #タイマー設定
        self.frm_timer = tk.LabelFrame(master, text='タイマー　分　　秒')
        self.frm_timer.pack(anchor='w')
        tk.Label(self.frm_timer, text='　　　　').grid(row=0, column=0)
        self.tm_mm_spin = tk.Spinbox(self.frm_timer, from_= 0, to= 23, increment=1, width=2)
        self.tm_ss_spin = tk.Spinbox(self.frm_timer, from_= 0, to= 60, increment=1, width=2)
        self.tm_mm_spin.grid(row=0,column=1)
        self.tm_ss_spin.grid(row=0,column=2)
 
        #設定ボタンの生成
        submit = tk.Button(self.frm_timer,text='設定',width=4,command=self.tsubmit)
        submit.grid(row=0,column=7)
 
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
        submit = tk.Button(self.frm_msg,text='送信',width=4,command=self.m_submit)
        submit.grid(row=0, column=1)
        
        self.con = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(5)
 
    #時刻設定「送信」ボタン処理    
    def asubmit(self):
        try:
            date_str='{}/{}/{}'.format(self.yy_spin.get(),
                                       self.mn_spin.get(),
                                       self.dd_spin.get())
            #date_strを strptime使って「文字列」から「日付」に変換する。
            #変換できない場合(2020/2/30など)は例外が発生する
            date_correct =datetime.datetime.strptime(date_str,'%Y/%m/%d') 
 
        except ValueError:
            print("Value Error!")
            return
 
        cmd = 'a,' + self.yy_spin.get() + ',' +  self.mn_spin.get() + ','
        cmd += self.dd_spin.get() + ','
        cmd += self.hh_spin.get() + ',' + self.mm_spin.get() + ','
        cmd += self.ss_spin.get()
        cmd += '\n'
        buf = bytes(cmd,'utf-8')
        self.con.write(buf)
        print(buf)
    
    #アラーム設定「送信」ボタン処理
    def wsubmit(self):
        try:
            hh = int(self.alm_hh_spin.get())
            if (0 <= hh < 24) == False:
                raise ValueError('alarm time out of range')
            mm = int(self.alm_mm_spin.get())
            if (0 <= mm < 60) == False:
                raise ValueError('alarm time out of range')
        except ValueError:
            print("Alarm Value Error!")
            return
 
        cmd = 'w,' + str(hh) + ',' + str(mm) + '\n'
        buf = bytes(cmd, 'utf-8')
        self.con.write(buf)
        print(buf)
 
    #タイマー設定「送信」ボタン処理
    def tsubmit(self):
        try:
            mm = int(self.tm_mm_spin.get())
            if (0 <= mm < 60) == False:
                raise ValueError('Timer out of range')
            ss = int(self.tm_ss_spin.get())
            if (0 <= ss < 60) == False:
                raise ValueError('Timer out of range')
        except ValueError:
            print('Timer Error')
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
    root.geometry("400x250+730+360")
    root.mainloop()