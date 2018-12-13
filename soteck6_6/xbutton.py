import tkinter
import tkinter.messagebox


class app:
    def __init__(self, master=None):
        self.flame = tkinter.Frame(master)
        self.flame.pack()
        self.lb = tkinter.Label(text='Window Destroy')

    def callback(self):
        if tkinter.messagebox.askyesno('exit?'):
            root.destroy()

if __name__ == '__main__':

    root = tkinter.Tk()
    root.title('tkinter.inter : destroy')
    root.geometry('400x300')

    r = app(root)
    root.protocol('WM_DELETE_WINDOW', r.callback)
    root.mainloop()
