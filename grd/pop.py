from arduino_app import Arduino_app
from bottle import run, route, template, redirect, request
import sqlite3, time, datetime
from collections import OrderedDict

class App(Arduino_app):
    def __init__(self):
        super().__init__()
        
#instance class
app = App()


HOST = ['localhost', 0]
PORT = 8080

navlis = OrderedDict()
navlis['top'] = '/'
navlis['setting'] = '/setting'


'''
almls = [{'h':15, 'm':50},
         {'h':18, 'm':50},
         {'h':19, 'm':50},
         {'h':20, 'm':50}]

ntime = datetime.datetime.now()
t1 = datetime.datetime(ntime.year, ntime.month, ntime.day, ntime.hour, ntime.minute) 
print(t1)
for i in almls:
    t2 = datetime.datetime(ntime.year, ntime.month, ntime.day, i['h'], i['m']) 
    tm = int((t1-t2).total_seconds()/60)
    if tm ==0:
        app.cmd_send('v') 
    elif tm >=-10 and tm<=10:
        app.cmd_send('r') 
    elif tm >10 and tm<=20:
        app.cmd_send('a') 
    else:
        app.cmd_send('c') 
    print(t2, tm)
 
'''
            

#適温判定
'''
・冬　...　温度20～22℃　湿度45～55％
・春秋　...　温度18～20℃　湿度55～70％
・夏　...　温度24～28℃　湿度45～55％
春は3〜5月、夏は6〜8月、秋は9〜11月、冬は12〜2月
'''
def moderate(month):
    if month == 12 or month ==2 or month==1:
        return ('冬(12〜2月)', 20, 22, 45, 55)

    elif month >= 3 or month <=5:
        return ('春(3〜5月)', 18, 20, 55, 70)

    elif month >= 9 or month <=11:
        return ('秋(9〜11月)', 18, 20, 55, 70)

    elif month >= 6 or month <=8:
        return ('夏(6〜8月)', 24, 28, 45, 55)


def modejudge(T, t1, t2, H, h1, h2):
        if T < t1:
            modtxt = '適温度より{}℃低いです。'.format(t1 - T)
        elif T > t2:
            modtxt = '適温度より{}℃高いです。'.format(T - t2)
        else:
            modtxt = '温度は適切です。'

        if H < h1:
            modtxt2 = '適湿度より{}%低いです。'.format(h1 - H)
        elif H > h2:
            modtxt2 = '適湿度より{}%高いです。'.format(H - h2)
        else:
            modtxt2 = '湿度は適切です。'

        return modtxt, modtxt2










@route(navlis['setting'], method=['GET', 'POST'])
def setting():
    return template('form', navlis = navlis)
    

@route(navlis['top'])
def index():
    ntime = datetime.datetime.now()
    almls = []

    appdb = sqlite3.connect('app.db')
    db = appdb.cursor()

    db.execute("create table if not exists result" + str(ntime.year) +str(ntime.month)+"(D,N,H,M,J)")
    db.execute("select mail,pw from user order by mail")
    for row in db.fetchall():
        app.set_user(row[0])
        app.set_pass(row[1])

    db.execute("select n,h,m from alm order by n")
    for i,row in enumerate(db.fetchall()):
        almls += [{'h':row[1], 'm':row[2]}]

    appdb.commit()
    appdb.close()

    stat = app.cmd_send('j') 
    if stat != '_':
        app.cmd_send('c') 
    
    t1 = datetime.datetime(ntime.year, ntime.month, ntime.day, ntime.hour, ntime.minute) 
    dht_dic = app.cmd_send('d') 

    for i in almls:
        t2 = datetime.datetime(ntime.year, ntime.month, ntime.day, i['h'], i['m']) 
        tm = int((t1-t2).total_seconds()/60)
        stat = app.cmd_send('j') 
        if tm ==0:
            if stat=='o' and stat=='_' :
                app.cmd_send('c') 
            else:
                app.cmd_send('s') 
        elif tm >=-10 and tm<0 and stat=='_':
            app.cmd_send('r') 
        elif tm >0 and tm<=20 and stat=='_':
            app.cmd_send('a') 
        
    if not dht_dic :
        dht = '計測できませんでした'
        time.sleep(1)
        return redirect('/')
    else:
        dht_t = int(dht_dic['T'])
        dth_h = int(dht_dic['H'])
        dht = '温度:{} ℃ / 湿度:{} %'.format(dht_dic['T'], dht_dic['H'])
        moddate = moderate(ntime.month)
        mod = '{}の適切な温度は{}~{}℃、適切な湿度は{}~{}%です。'.format(moddate[0], moddate[1],moddate[2],moddate[3],moddate[4])

        modtxt, modtxt2 = modejudge(dht_dic['T'], moddate[1], moddate[2], dht_dic['H'], moddate[3], moddate[4])

        return template('index', dht_t=dht_t, dht_h=dht_h, dht=dht, navlis = navlis, ntime=ntime.strftime('%Y, %m, %d, %H:%M:%S'), mod=mod, modtxt=modtxt, modtxt2=modtxt2, almls=almls ,stat=stat)


run(host=HOST[0], port=PORT)

