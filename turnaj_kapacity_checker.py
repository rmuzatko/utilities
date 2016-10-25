#!/usr/bin/env python
# -*- coding: cp1252 -*-

import email
import os
import time
import smtplib
import win32traceutil
from selenium import webdriver


driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get('http://cgf.cz/TournRegistrations.aspx?IDTournament=472878377&IDTournCategory=0')

try:
    elements = driver.find_element_by_xpath('//*[@id="ctl00_MainPlaceHolder_gvCategories"]/tbody/tr[9]/td[4]')
    print ('Pocet prihlasenych hracu:', elements.text)
    #tournament = driver.find_element_by_xpath('//*[@id="ctl00_MainPlaceHolder_userHead_hypTournDetail"]')
    #print ('Tournament name:', tournament.text)

    if elements.text == '92':
        print ('kapacita turnaje prekrocena')
    else:
        neco = ('muzes se prihlasit do turnaje', elements.text)
        print (neco)
        sendemail (FROM, TO, SUBJECT, TEXT)

except Exception as e:
    print ('Exception found', format(e))

# send email to me with required action (below are config data)
#tournament = driver.find_element_by_xpath('//*[@id="ctl00_MainPlaceHolder_userHead_hypTournDetail"]')
gmail_user = 'rmuzatko@gmail.com'
gmail_pwd = 'Rambo007'
FROM = gmail_user
TO = 'rmuzatko@yahoo.com'
SUBJECT = 'Pocet prihlasenych hracu:' + elements.text
TEXT = 'python tournaments sniffer'

def sendemail (FROM, TO, SUBJECT, TEXT):
    
    # Prepare actual message
    #message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, TO, SUBJECT, TEXT)
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