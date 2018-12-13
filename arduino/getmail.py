import imaplib
import email
import os
import sys
import dateutil.parser
 
IMAP_HOST = 'imap.gmail.com'
IMAP_PORT = 993
LOGIN_USERNAME = 'k1srcufc@gmail.com' 
LOGIN_PASSWORD = '_%YwhnmEKqZj'
 
def main():
    gmail = imaplib.IMAP4_SSL(IMAP_HOST,IMAP_PORT)
 
    try:
        gmail.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        gmail.select('inbox')
        typ, [data] = gmail.search(None, "(UNSEEN)")
        #typ, [data] = gmail.search(None, "(ALL)")
 
        #取得したメール一覧の処理
        cnt = 0
 
        for num in data.split():
            cnt += 1
            ### 各メールへの処理 ###
            result, d = gmail.fetch(num, "(RFC822)")
            raw_email = d[0][1]
            msg = email.message_from_bytes(raw_email)
 
            #文字コード取得用
            msg = email.message_from_string(raw_email.decode('iso-2022-jp'))
            msg_encoding = email.header.decode_header(msg.get('Subject'))[0][1] or 'iso-2022-jp'
 
            #パースして解析準備
            msg = email.message_from_string(raw_email.decode(msg_encoding))
 
            date = dateutil.parser.parse(msg.get('Date')).strftime("%Y/%m/%d %H:%M:%S")
 
            subject = email.header.decode_header(msg.get('Subject'))
            title = ""
            for sub in subject:
                if isinstance(sub[0], bytes):
                    title += sub[0].decode(msg_encoding)
                else:
                    title += sub[0]
 
            body = ""
            if msg.is_multipart():
                for payload in msg.get_payload():
                    if payload.get_content_type() == "text/plain":
                        body = payload.get_payload()
            else:
                if msg.get_content_type() == "text/plain":
                    body = msg.get_payload()
 
            print(str(cnt) + " : " + title)
            print(date)
            print(msg_encoding)
            print(body)
            print('')
    finally:
        gmail.close()
        gmail.logout()
        return(cnt)
 
##メイン
main()
