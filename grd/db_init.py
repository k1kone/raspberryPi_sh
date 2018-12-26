import sqlite3, time, datetime


#make date base
appdb = sqlite3.connect('app.db')
db = appdb.cursor()

#make table in datebase
db.execute("drop table if exists user")
db.execute("create table if not exists user(mail, pw,send_mail)")
db.execute("drop table if exists alm")
db.execute("create table if not exists alm(n,h,m)")

#date input in table:user of datebase
db.execute("insert into user values('k1srcufc@gmail.com','_%YwhnmEKqZj','k1srsufc@gmail.com')")
db.execute("insert into alm values(1,13,50)")

db.execute("select mail,pw,send_mail from user order by mail")
for row in db.fetchall():
    print(row)


db.execute("select n,h,m from alm order by n")
for row in db.fetchall():
    print(row)

'''
db.execute("select D,N,H,M,J from result201812 order by D")
for row in db.fetchall():
    print(row)
'''

appdb.commit()
appdb.close()


