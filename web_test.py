#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_size(1400, 1000)
driver.get('http://cgf.cz/TournRegistrations.aspx?IDTournament=472878377&IDTournCategory=0')

def get_element(self):
    element = self.driver.find_element_by_partial_link_text('Vše')

    for elem in element:
        print ("ele")

driver.close()