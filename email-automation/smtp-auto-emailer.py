"""
A program to send an email
"""

import smtplib, ssl, getpass

# create message details
email = "lrspencer@hotmail.co.uk"
message = "Hello, world!"

# enter password
password = getpass.getpass()

# connect to server and login
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("autobot193245@gmail.com", password)

# send email
server.sendmail("autobot193245@gmail.com", email, message)
print("Email sent!")