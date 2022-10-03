def send_mail(email):
    email_content="""<p>Dear Sir/Madam, </p> <p>I am writing on behalf of
    Hack, got to know about your event from Knowafst.com website. </p> 
    <p> Regards 
    MOHANAPRIYA<br>
    Studentk, RMK<BR>
    </p>
    """
    
    sender_address="moha20126.cb@rmkec.ac.in"
    sender_password="Mohana1702"
    receiver_address=email
    
    message=MIMEMultipart()
    message["From"]="STUDENT RMK <moha20126.cb@rmkec.ac.in>"
    message["To"]=receiver_address
    message["Subject"]="just learning"
    message.attach(MIMEText(email_content,"html"))
    
    session=smtplib.SMTP("smtp.gmail.com",587)
    session.starttls()
    session.login(sender_address,sender_password)
    text=message.as_string()
    session.sendmail(sender_address,receiver_address,text)
    session.quit()
    print("Mail sent to",receiver_address)
    
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 

email="priyashanmugam1702@gmail.com"
send_mail("priyashanmugam1702@gmail.com")
