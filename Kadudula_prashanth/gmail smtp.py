# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 19:14:28 2022

@author: Prashanth K
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mail_content = """Hello,
This is a test mail used for testing purpose.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
"""
# The mail addresse and password
sender_address = 'kadudulaprashanth3@gmail.com'
sender_password = 'ktmgegblpasxbkfh'
receiver_address = 'kpeceprashanth@gmail.com'
# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
# The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'nptel joy of computing.pdf'
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)  # encode the attachment

# add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls() # enable security
session.login(sender_address, sender_password)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')