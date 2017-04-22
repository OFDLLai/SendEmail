#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


Send_host='smtp.gmail.com'  #Set up your Smtp server
Send_user='xxxxxx@gmail.com'    #Input send User
Send_pass='******'   #Input send User password 

sender = 'lai'  #Input send User
receivers = 'zzzzzz@gmail.com'  # Receive User

message = MIMEText('Python Email Test...', 'plain', 'utf-8')
message['From'] = Send_user
message['To'] =  'Python Test'

subject = 'Python SMTP TEST'
message['Subject'] = Header(subject, 'utf-8')


try:
    start_send = smtplib.SMTP() 
    start_send.connect(Send_host,'587')    # default port25 
    start_send.ehlo()
    start_send.starttls()
    start_send.login(Send_user,Send_pass)  
    start_send.sendmail(sender, receivers, message.as_string())
    start_send.quit()
    print ("Send Successful")
except smtplib.SMTPException:
    print ("Send Error")
