# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
#from email.mime.text import MIMEText
'''
textfile = ('c:\\windows-version.txt')

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(textfile) as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())
'''
# me == the sender's email address
# you == the recipient's email address
#msg['Subject'] = 'The contents of %s' % textfile
msg['Subject'] = 'The contents of'
msg['From'] = 'rmuzatko@gmail.com'
msg['To'] = 'rmuzatko@yahoo.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.login(gmail_user, gmail_pwd)
s.send_message(msg)
s.quit()