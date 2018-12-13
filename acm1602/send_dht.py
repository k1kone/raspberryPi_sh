import RPi.GPIO as GPIO
import dht11
import smtplib, time
from getpass import getpass
from acm1602 import acm1602

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PROT = 587

Usr = 'k1srcufc'
Pw = '_%YwhnmEKqZj'

def send_mail(recipient, address_from, password, subject, text):
    gmail_user = address_from
    gmail_pass = password

    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PROT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_pass)
    header = 'To:' + recipient + '\n' + 'From:' + gmail_user
    header = header + '\n' + 'Subject:' + subject + '\n\n'
    msg = header + '\n' + text + '\n\n'
    smtpserver.sendmail(gmail_user, recipient, msg)
    smtpserver.close()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
ins = dht11.DHT11(pin=17)

if __name__ == '__main__':
    print('test')
    email_address_to = input('Enter email address To:\n')
    email_address_from = input('Enter email address From:\n') if not Usr else Usr
    email_password = input('Enter email Password:\n') if not Pw else Pw
    
    result = ins.read()
    txt = 'test'
    print('txt = {}'.format(txt))
    if result.is_valid():
        txt = 'Temp:' + str(result.temperature) + 'C '+'RM:'+ str(result.humidity) + '%' 
    else:
        txt = '***can\'t get date.***'

    print('txt = {}'.format(txt))
    body = 'Hello' + time.strftime('%I:%M:%S') + txt

    send_mail(email_address_to, email_address_from, email_password, 'test send mail', body)
"""
mail = imaplib.IMAP4_SSL(SERVER_NAME) 

mail.login(Usr, Pw)

mail.list()

mail.select('Inbox')

(st, mlist) = mail.status('Inbox', '(UNSEEN)')

if (st == 'OK'):
    lcd = acm1602(1, 0x50, 4)

    lcd.move_home()

    lcd.set_cursol(0)

    lcd.set_blink(0)

    #mcount = int(mlist[0].split()[2].strip(').,]')) it is for python
    print('{}'.format(mlist[0].split()[2])) 
    mcount = int(mlist[0].split()[2].decode().strip(').,]')) #for python3

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
"""
