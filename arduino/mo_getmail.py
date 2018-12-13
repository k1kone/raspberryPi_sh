import imaplib
import email
import os
import sys
import dateutil.parser
 
class getmail:
    def __init__(self):
        self.IMAP_HOST = 'imap.gmail.com'
        self.IMAP_PORT = 993
        self.LOGIN_USERNAME = 'k1srcufc@gmail.com' 
        self.LOGIN_PASSWORD = '_%YwhnmEKqZj'
     
    def main(self):
        gmail = imaplib.IMAP4_SSL(self.IMAP_HOST,self.IMAP_PORT)
     
        try:
            gmail.login(self.LOGIN_USERNAME, self.LOGIN_PASSWORD)
            gmail.select('inbox')
            typ, [data] = gmail.search(None, "(UNSEEN)")
            #typ, [data] = gmail.search(None, "(ALL)")
     
            #取得したメール一覧の処理
            cnt = 0
     
            for num in data.split():
                cnt += 1
     
        finally:
            gmail.close()
            gmail.logout()
            print('You got {}mail.'.format(cnt))
            return 'You got {}mail.'.format(cnt)
     

if __name__ == '__main__':
    mo = getmail()
    mo.main()
