import os
import json
import ssl
import smtplib
from email.message import EmailMessage
from email.header import Header
from email.utils import formataddr


def lambda_handler(event, context):
    
    send_email(email_body=event["message"], sender=event["from"])
    
    return {
        'statusCode': 200
    }
    

def send_email(email_body: str, sender: str) -> None:
    recipient_email = os.environ['RECIPIENT_EMAIL']
    smtp_email = os.environ['SMTP_EMAIL']
    smtp_password = os.environ['SMTP_PASSWORD']
    
    message = EmailMessage()
    message.set_content(email_body)
    
    message['Subject'] = f'Contact form submitted by {sender}'
    message['From'] = formataddr((str(Header('LRS4.github.io', 'utf-8')), smtp_email))
    message['To'] = recipient_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(smtp_email, smtp_password)
    server.send_message(message)
    server.quit()
