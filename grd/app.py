from arduino_app import Arduino_app
from bottle import run, route, get, post, template, redirect, request
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

sendmail = ''
stls = []            

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
    cl = ['','']
    if T < t1:
        modtxt1 = '適温度より{}℃低いです。'.format(t1 - T)
        if (t1-T)<=3:
            cl[0] = 'hard_d'
        elif (t1-T)>3:
            cl[0] = 'dng_d'
    elif T > t2:
        modtxt1 = '適温度より{}℃高いです。'.format(T - t2)
        if (T-t2)<=3:
            cl[0] = 'hard_u'
        elif (T-t2)>3:
            cl[0] = 'dng_u'
    else:
        modtxt1 = '温度は適切です。'
        cl[0] = 'normal'

    if H < h1:
        modtxt2 = '適湿度より{}%低いです。'.format(h1 - H)
        if (h1-H)<=3:
            cl[1] = 'hard_d'
        elif (h1-H)>3:
            cl[1] = 'dng_d'
    elif H > h2:
        modtxt2 = '適湿度より{}%高いです。'.format(H - h2)
        if (H-h2)<=3:
            cl[1] = 'hard_u'
        elif (H-h2)>3:
            cl[1] = 'dng_u'
    else:
        modtxt2 = '湿度は適切です。'
        cl[1] = 'normal'

    return modtxt1, modtxt2, cl


@route(navlis['top'])
def index():
    global stls
    global sendmail

    ntime = datetime.datetime.now()
    almls = []

    appdb = sqlite3.connect('app.db')
    db = appdb.cursor()

    db.execute("create table if not exists result" + str(ntime.year) +str(ntime.month)+"(D,N,H,M,J)")
    db.execute("select mail,pw,send_mail from user order by mail")
    for row in db.fetchall():
        app.set_user(row[0])
        app.set_pass(row[1])
        sendmail = row[2]

    db.execute("select n,h,m from alm order by n")
    for i,row in enumerate(db.fetchall()):
        almls += [{'n':row[0], 'h':row[1], 'm':row[2]}]

    appdb.commit()
    appdb.close()

    stat = app.cmd_send('j') 
    
    t1 = datetime.datetime(ntime.year, ntime.month, ntime.day, ntime.hour, ntime.minute) 
    dht_dic = app.cmd_send('d') 
    #if not stls:
        #stls =['' for i in range(len(almls))]

    for ind,i in enumerate(almls):
        t2 = datetime.datetime(ntime.year, ntime.month, ntime.day, i['h'], i['m']) 
        tm = int((t1-t2).total_seconds()/60)

        if tm<-5:
            #stls[ind] = 'out of alarm time.'
            app.cmd_send('c') 
        elif tm >=-5 and tm<0:
            if 'o' in stat:
                #stls[ind] = 'success!'
                app.cmd_send('b') 
            else:
                app.cmd_send('r') 
                #stls[ind] = 'waiting...'
        elif tm >=0 and tm<=5:
            if 'o' in stat:
                #stls[ind] = 'success!'
                app.cmd_send('b') 
            else:
                app.cmd_send('a') 
                app.cmd_send('s') 
                #stls[ind] = 'not pushed button'
        elif tm >5:
            app.cmd_send('c') 
            #stls[ind] = 'not success.'
        
    if not dht_dic :
        dht = '計測できませんでした'
        time.sleep(1)
        return redirect('/')
    else:
        dht_t = int(dht_dic['T'])
        dht_h = int(dht_dic['H'])
        dht = '温度:{} ℃ / 湿度:{} %'.format(dht_dic['T'], dht_dic['H'])
        moddate = moderate(ntime.month)
        mod = '{}の適切な温度は{}~{}℃、適切な湿度は{}~{}%です。'.format(moddate[0], moddate[1],moddate[2],moddate[3],moddate[4])

        modtxt1, modtxt2, cl= modejudge(dht_dic['T'], moddate[1], moddate[2], dht_dic['H'], moddate[3], moddate[4])

        return template('index', dht_t=dht_t, dht_h=dht_h, dht=dht, navlis = navlis, ntime=ntime.strftime('%Y年%m月%d日 %H:%M:%S'), mod=mod, modtxt1=modtxt1, modtxt2=modtxt2, cl=cl, almls=almls ,stat=stat)


@route(navlis['setting'], method=['GET', 'POST'])
def setting():
    global stls

    if request.method =='POST':
        time_h = int(request.POST.getunicode('time_h'))
        time_m = int(request.POST.getunicode('time_m'))

        appdb = sqlite3.connect('app.db')
        db = appdb.cursor()

        new_n = db.execute("select max(n) + 1 from alm").fetchone()[0]
        if not new_n:
            new_n=1
        db.execute("insert into alm values(?,?,?)",(new_n,time_h,time_m))

        appdb.commit()
        appdb.close()

        return '''success<script>
                setTimeout(function(){location.href='/setting';}, 5000);
                </script>
        '''

    else:
        almls = []
        appdb = sqlite3.connect('app.db')
        db = appdb.cursor()
        db.execute("select n,h,m from alm order by n")
        for i,row in enumerate(db.fetchall()):
            almls += [{'n':row[0], 'h':row[1], 'm':row[2]}]

        appdb.commit()
        appdb.close()
        #stls =['' for i in range(len(almls))]

        return template('form',navlis = navlis, almls=almls,ntime=datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S') )

@route('/del/<n:int>')
def del_alm(n):
    
    appdb = sqlite3.connect('app.db')
    db = appdb.cursor()
    db.execute("delete from alm where n=?", (n,))
    appdb.commit()
    appdb.close()

    return redirect('/setting')

run(host=HOST[0], port=PORT)

