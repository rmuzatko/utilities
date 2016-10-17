#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_size(1400, 1000)
driver.get('http://cgf.cz/TournRegistrations.aspx?IDTournament=472878377&IDTournCategory=0')
#driver.get('http://localhost/testpage.html')
#driver.get('http://python.org')

try:
    elements = driver.find_element_by_xpath('//*[@id="ctl00_MainPlaceHolder_gvCategories"]/tbody/tr[9]/td[4]')
    #elements = driver.find_element_by_link_text('Vše')
    #elements = driver.find_element_by_name('username')
    #elements = driver.find_element_by_xpath('//h2')
    print ('Pocet prihlasenych hracu:', elements.text)
    if elements.text == '92':
        print ('porad plno')
    else:
        print ('muzes se prihlasit')

except Exception as e:
    print ('Exception found', format(e))

time.sleep(3)

driver.quit()