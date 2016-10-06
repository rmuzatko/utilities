#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_size(1400, 1000)
driver.get('http://localhost/testpage.html')

def get_element(self):
    element = self.driver.find_element_by_name('username')

    for elem in element():
        if elem == element:
            print ("OK")
        else:
            print ('not good')

time.sleep(7)

driver.close()