#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

Send_host='smtp.gmail.com'  #Set up your Smtp server
Send_user='xxxxxx@gmail.com'    #Input send User
Send_pass='******'   #Input send User password 

sender = 'lai'  #Input send User
recipient = 'zzzzzz@gmail.com'  # Receive User

msg = MIMEText('Python Email Test', 'plain', 'utf-8')
msg['From'] = Send_user
msg['To'] =  'Python Test'
msg['Subject'] = 'Python SMTP TEST'


try:
    start_send = smtplib.SMTP() 
    start_send.connect(Send_host,'587')    # default port25 
    start_send.ehlo()
    start_send.starttls()
    start_send.login(Send_user,Send_pass)  
    start_send.sendmail(sender, recipient, msg.as_string())
    start_send.quit()
    print ("Send Successful")
except smtplib.SMTPException:
    print ("Send Error")
