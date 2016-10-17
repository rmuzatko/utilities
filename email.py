import smtplib

gmail_user = 'rmuzatko@gmail.com'
yahoo_user = 'rmuzatko@yahoo.com'
gmail_pwd = 'kobra007'
FROM = gmail_user
TO = yahoo_user
SUBJECT = 'pokus'
MSG = 'neco neco'

# Prepare actual message
'''
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
'''

message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

'''
message = """From: From gmail_user
To: rmuzatko@yahoo.com
Subject: SMTP e-mail test

This is a test e-mail message.
"""
'''

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print ('successfully sent the mail')
except:
    print ("failed to send mail")


