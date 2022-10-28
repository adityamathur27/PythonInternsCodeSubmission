import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "shivani.140026@gmail.com"
Sender_pass = input("YOUR PASSWORD")
Reciever_Email = "shivangishivani.5854@gmail.com","shivanig5858@gmail.com"


newMessage = EmailMessage()                         
newMessage['Subject'] = "Check out the new logo"
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('In this mail we are sending some attachments.Let me know what you think. Image attached!')
print('image sent proccess')
with open('Event.png', 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name

newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
print('image sent proccess end')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(Sender_Email, Sender_pass)             
            smtp.send_message(newMessage)

print('sent successfull')
