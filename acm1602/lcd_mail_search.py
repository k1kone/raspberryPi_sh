import smbus, time
import imaplib

from acm1602 import acm1602

SERVER_NAME = 'imap.gmail.com'

Usr = 'k1srcufc'
Pw = '_%YwhnmEKqZj'

mail = imaplib.IMAP4_SSL(SERVER_NAME) 

mail.login(Usr, Pw)

#mail.list()

mail.select('Inbox')

#(st, mlist) = mail.status('Inbox', '(UNSEEN)')
st, b_mlist = mail.search(None, "UNSEEN")

if (st == 'OK'):
    lcd = acm1602(1, 0x50, 4)

    lcd.move_home()

    lcd.set_cursol(0)

    lcd.set_blink(0)

    #mcount = int(mlist[0].split()[2].strip(').,]')) it is for python
    mlist = b_mlist[0].decode().split()
    mcount = len(mlist)
    print(b_mlist[0].decode())

    if (mcount > 0):
        lcd.backlight(1)
        lcd.write('You got')
        lcd.move(0x00, 0x01)
        lcd.write('    ' + str(mcount) + ' Mail.')
    else:
        lcd.backlight(0)
        lcd.write('No new mail.')

else:
    print("Can't get Mail status.")

mail.close()
mail.logout()
