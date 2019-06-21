"""
A program to send a rich html email
"""

import smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "autobot193245@gmail.com"
receiver_email = "lrspencer@hotmail.co.uk"

# create message details
message = MIMEMultipart("alternative")
message["Subject"] = "How are you?"
message["From"] = "Lewis Spencer"
message["To"] = receiver_email

# create email
# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""
# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# enter password
password = getpass.getpass()

# connect to server and login
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

# send email
server.sendmail(sender_email, receiver_email, message.as_string())
print("Email sent!")