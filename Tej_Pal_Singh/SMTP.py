import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Hello,
This is Tej Pal Singh from Hackveda side.
In this mail we are sending some attachments.
Just to get the acknoledgement about the mail sending.
Thank You
                                              Regards
                                              Tej Pal Singh 
'''
#The mail addresses and password
sender_address = "singh.junky@gmail.com"
sender_pass = "tej@12345"
receiver_address = "coolboytejsingh@gmail.com"
#Setup the MIME
message = MIMEMultipart()
message_from = sender_address
message_to = receiver_address
message_subject = "A test mail sent by Python. It has an attachment."
#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = "tej.png"
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase("application", "octate-stream")
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header("Content-Decomposition", "attachment", filename=attach_file_name)
message.attach(payload)
#Create SMTP session for sending the mail
session = smtplib.SMTP("smtp.gmail.com", 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address , sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print("Mail Sent successfully.....")