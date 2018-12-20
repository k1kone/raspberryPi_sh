from arduino_app import Arduino_app
from bottle import run, route, template, redirect, request
import sqlite3, time, datetime
from collections import OrderedDict


HOST = ['localhost', 0]
PORT = 8080

navlis = OrderedDict()
navlis['top'] = '/'
navlis['setting'] = '/setting'

#nowtime = datetime.datetime.now()
pastime = None

class App(Arduino_app):
    def __init__(self):
        super().__init__()
        
#instance class
app = App()

#make date base
appdb = sqlite3.connect('app.db')
db = appdb.cursor()
#make table in datebase
#db.execute("create table user(mail, pw)")
#db.execute("create table alm_t(h, m, j)")

#date input in table:user of datebase
#db.execute("insert into user values('k1srcufc@gmail.com','_%YwhnmEKqZj')")
'''
db.execute("select mail,pw from user order by mail")
for row in db.fetchall():
    app.set_user(row[0])
    app.set_pass(row[1])
'''

#db.execute("insert into alm_t values(12,30,'=')")
db.execute("select h,m,j from alm_t order by h")
for row in db.fetchall():
    print(row)

appdb.commit()
appdb.close()



def timeset(n):
    pass


@route(navlis['setting'], method=['GET', 'POST'])
def setting():
    return template('form', navlis = navlis)
    

@route(navlis['top'])
def index():
    nowtime = datetime.datetime.now()
    dht_dic = app.cmd_send('d') 
    if not dht_dic :
        dht = '計測できませんでした'
        time.sleep(1)
        return redirect('/')
    else:
        dht = '温度:{} ℃ / 湿度:{} %'.format(dht_dic['T'], dht_dic['H'])
        return template('index', dht=dht, navlis = navlis, ntime=nowtime.strftime('%Y, %m, %d, %H:%M:%S'))



run(host=HOST[0], port=PORT)

