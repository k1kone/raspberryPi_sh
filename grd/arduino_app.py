import serial
import time, ast, sys, re
from sendMail import MAIL_app
sys.dont_write_bytecode = True

class Arduino_app(MAIL_app):
    def __init__(self):
        self.con = serial.Serial('/dev/ttyACM0',9600)
        super().__init__()
        #self.setup_cmp()

    '''
    def setup_cmp(self):
        while not self.con.readline():
            print('loading...')
            time.sleep(1)
        date = self.con.readline().decode()
        print('ok')
        print(date)
    '''

    def cmd_send(self, command):
        cmd = bytes(command + '\n', 'utf-8')
        time.sleep(1)
        self.con.write(cmd)
        
        if command is 'd':
            return   self.dht_inp(5)

    def dht_inp(self, r):
        if r is 0:
            return False

        time.sleep(1)
        dht = self.con.readline().decode()

        if re.match(r"{'H':", dht):
            return ast.literal_eval(dht)
        else : 
            print('read agein {}'.format(r))
            self.dht_inp(r-1)


if __name__ == '__main__':
    app = Arduino_app()
    

    ppp = app.cmd_send('d')
    print('T:{} / H:{}'.format(ppp['T'], ppp['H']))

    app.set_user('k1srcufc@gmail.com')
    app.set_pass('_%YwhnmEKqZj')

    print(app.get_user())
    print(app.get_pass())


    msg = 'hello test'

