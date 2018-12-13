import tkinter as tk
 
class Calc:
    def __init__(self,master=None):
        self.frm_results = tk.Frame(master)
        self.frm_results.pack(anchor='e')
        self.frm_func = tk.Frame(master)
        self.frm_func.pack(anchor='w')
        self.frm_button = tk.Frame(master)
        self.frm_button.pack(anchor='w')
        self.create_widgets()
        
    def create_widgets(self):
        self.a=''
        self.b=''
        self.op=''
        self.results=tk.StringVar()
        self.results.set('0')
        
        #results ラベル(結果表示)
        lb = tk.Label(self.frm_results, textvariable=self.results)
        lb.pack()
 
        # create and bind clear button
        btn = tk.Button(self.frm_func,text='C',width=3)
        btn.bind("<Button>", self.clr_pushed)
        btn.grid(column=0, row=0)
 
        # create 1-9. buttons
        for n, cap in enumerate([7,8,9,4,5,6,1,2,3,0,'.']):
            btn = tk.Button(self.frm_button,text=str(cap),width=3)
            btn.bind("<Button>", self.num_pushed)
            btn.grid(column=n%3, row=n//3)
 
        # create operater buttons
        for n, cap in enumerate(['-','+','/','*']):
            btn = tk.Button(self.frm_button, text=cap, width=3)
            btn.bind("<Button>", self.op_pushed)
            btn.grid(column=3, row=n)
 
        # create and bind equal button
        btn = tk.Button(self.frm_button,text='=',width=3)
        btn.bind("<Button>", self.eq_pushed)
        btn.grid(column=2, row=3)
 
 
    # 0-9. button pushed
    def num_pushed(self,event):
        num_str=event.widget['text']
        if len(self.op) == 0:
            self.a += num_str
            self.results.set(self.a)
        else:
            self.b += num_str
            self.results.set(self.b)
 
    # operator(+ - / *) button pushed
    def op_pushed(self,event):
        self.op=event.widget['text']
 
    # equal(=) button pushed
    def eq_pushed(self,event):
        if len(self.a) and len(self.b) and len(self.op):
            if self.op == '+':
                print(float(self.a)+float(self.b))
                self.results.set("{:.2f}".format(float(self.a)+float(self.b)))
 
            elif self.op == '-':
                print(float(self.a)-float(self.b))
                self.results.set("{:.2f}".format(float(self.a)-float(self.b)))
 
            if self.op == '/':
                print(float(self.a)/float(self.b))
                self.results.set("{:.2f}".format(float(self.a)/float(self.b)))
 
            if self.op == '*':
                print(float(self.a)*float(self.b))
                self.results.set("{:.2f}".format(float(self.a)*float(self.b)))
 
        else:
            self.results.set('0')
 
        self.a=self.b=self.op=''
 
    #clear(C) button pushed
    def clr_pushed(self,event):
        self.a=self.b=self.op=''
        self.results.set('0')
    
if __name__ == '__main__':
    root=tk.Tk()
    root.geometry('200x230')
    calc = Calc(master=root)
    root.mainloop()
