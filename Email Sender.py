#go over to our gmail account and setup 2 factor authentication
#generate app password
#create a function to send the mail

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'email@gmail.com'
email_password = 'email app code'

email_receiver = 'email@gmail.com'

subject = "Dont forget to Subscribe"
body =""" team knockout"""

em = EmailMessage()
em ['From'] = email_sender
em ['To']   = email_receiver
em ['subject'] = subject
em.set_content (body)

context = ssl.create_default_context ()

with smtplib.SMTP_SSL('smtp.gmail.com',context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

