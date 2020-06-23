import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

file = open("text.txt")
line = file.read()
file.close()

spam_count = 10             # REPLACE TEXT
email_addr = "from_email"   # REPLACE TEXT
to_email = "to_email"       # REPLACE TEXT
password = "pass"           # REPLACE TEXT
subject = "enter_subjet"    # REPLACE TEXT    

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = email_addr
msg['To'] = to_email
msg.set_content(line)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_addr, password)
    for i in range(spam_count):
        smtp.send_message(msg)

