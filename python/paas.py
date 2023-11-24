from email.message import EmailMessage
import ssl
import smtplib
from reciever import myresult
email_sender = 'project101offical@gmail.com'
email_password = 'qqir tgch qjud ugky'

email_receiver = myresult

subject = 'time for class'
body = '''
Your schedule for the day...
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


