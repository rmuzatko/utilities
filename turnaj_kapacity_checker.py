#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
import smtplib

driver = webdriver.Chrome()
driver.set_window_size(1400, 1000)
driver.get('http://cgf.cz/TournRegistrations.aspx?IDTournament=472878377&IDTournCategory=0')

try:
    elements = driver.find_element_by_xpath('//*[@id="ctl00_MainPlaceHolder_gvCategories"]/tbody/tr[9]/td[4]')
    print ('Pocet prihlasenych hracu:', elements.text)

    if elements.text == '92':
        print ('porad plno')
    else:
        print ('muzes se prihlasit')

except Exception as e:
    print ('Exception found', format(e))

# send email to me with required action
gmail_user = 'rmuzatko@gmail.com'
gmail_pwd = 'kobra007'
FROM = gmail_user
TO = 'rmuzatko@yahoo.com'
SUBJECT = 'pokus'
TEXT = 'neco neco'

# Prepare actual message
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
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

time.sleep(3)

driver.quit()