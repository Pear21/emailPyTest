#!/usr/bin/python

import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/email')
sys.path.reverse()

import smtplib
from email import encoders
from email.Header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

sender="emailPyTestG@gmail.com"
receiver=["pengye@genomics.cn", "498010784@qq.com"]#, "zhouze@genomics.cn"]
subject="python email test 160807"
usrname=sender
passwd="naafmdealogofnmq"

"""
## faking text
import random
word=100*random.random()
word=str(word)
"""

## sending
text='test160807night'
# msg=MIMEText(text, 'plain', 'utf-8')
msg=MIMEMultipart()
msg.attach(MIMEText(text, 'plain', 'utf-8'))
msg['Subject']=Header(subject, 'utf-8')
msg['From']=Header(sender, 'utf-8')
msg['To']=Header("%s"% ", ".join(receiver), 'utf-8')

att1=MIMEText(open('README.md', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"]='application/octet-stream'
att1["Content-Disposition"]='attachment; filename="email.py"'
msg.attach(att1)

image=open('/home/pear/Downloads/8.jpg')
att2=MIMEBase('image', 'jpeg', filename='earthEatsMoon.jepg')
att2.add_header('Content-Disposition', 'attachment', filename='earthEatsMoon')
att2.add_header('Content-ID', '<0>')
att2.add_header('X-Attachment-Id', '0')
att2.set_payload(image.read())
encoders.encode_base64(att2)
msg.attach(att2)

smtpserver="smtp.gmail.com"
smtpport=587
smtp=smtplib.SMTP()
smtp.set_debuglevel(1)
try:
    print "Connecting..."
    smtp.connect(smtpserver, smtpport)
    smtp.ehlo()
    smtp.starttls()
    print "Connected."
except:
    print "Error: cannot connect"
    exit(1)

try:
    print "Logging in..."
    smtp.login(usrname, passwd)
    print "Logged in."
except:
    print "Error: cannot log in"
    exit(1)

try:
    print "Senting..."
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print "Sent"
except:
    print "Error: cannot send"
    exit(1)
