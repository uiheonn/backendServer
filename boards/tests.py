import json
import imaplib
import email
from email.header import decode_header, make_header
'''
dict_string = '{"foo":"bar", "foo2":"bar2"}'
# type(dict_string)
# 

dict = json.loads(dict_string)

# {u'foo': u'bar', u'foo2': u'bar2'}
# type(dict)

print(dict)
subject = 2
fr=3
body=10

dite_string = {"title":subject}
dite = json.dumps(dite_string)
print(dite)

emaillist = {}
dada_string = {"tite":subject, "fr":fr}
dada = json.dumps(dada_string)
print(dada)
'''

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'ky7662'
pw = 'ekun40867662!!?'
imap.login(id, pw)
imap.select("INBOX")
status, messages = imap.uid('search', None, 'ALL')
messages = messages[0].split()

r_email = messages[-1]

res, msg = imap.uid('fetch', r_email, "(RFC822)")

raw = msg[0][1].decode('utf-8')

email_message = email.message_from_string(raw)

# 보낸사람
fr = make_header(decode_header(email_message.get('From')))
fr = str(fr)
print(fr)

# 메일 제목
subject = make_header(decode_header(email_message.get('Subject')))
subject = str(subject)
print(subject)



# 메일 내용
if email_message.is_multipart():
    for part in email_message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
        
else:
    body = email_message.get_payload(decode=True)
body = body.decode('utf-8')
print(body)