import datetime
import smtplib
import time
import sys
sys.dont_write_bytecode = True

class MAIL_app:
    def __init__(self):
       self.__USER  = ''
       self.__PASS  = ''
       self.__SERVER  = 'smtp.gmail.com'
       self.__PORT  = 587

    def set_user(self, user):
       self.__USER  = user

    def get_user(self):
       return self.__USER

    def set_pass(self, password):
       self.__PASS  = password

    def get_pass(self):
       return self.__PASS


    def send_email(self, recipient, subject, text):
        smtpserver = smtplib.SMTP(self.__SERVER, self.__PORT)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(self.__USER, self.__PASS)
        header = 'To:' + recipient + '\n' + 'From: ' + self.__USER
        header = header + '\n' + 'Subject:' + subject + '\n'
        msg = header + '\n' + text + '\n\n'
        smtpserver.sendmail(self.__USER, recipient, msg)
        smtpserver.close()






if __name__ == '__main__':
    mail = MAIL_app()
    mail.set_user('k1srcufc@gmail.com')
    mail.set_pass('_%YwhnmEKqZj')

    print(mail.get_user())
    print(mail.get_pass())
    print(mail.get_user())


    msg = 'hello test'

    mail.send_email('k1srsufc+raspy@gmail.com', 'sub', msg)

