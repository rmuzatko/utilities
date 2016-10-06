#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_size(1400, 1000)
driver.get('http://cgf.cz/TournRegistrations.aspx?IDTournament=472878377&IDTournCategory=0')

#element_vse = ("/html/body[@id='ctl00_mainbody']/form[@id='aspnetForm']/div[@id='bodybig']/div[@id='pagebig']/div[@id='contentbig']/div[@class='MainHolder'][2]/div[@class='padding5'][1]/div/table[@id='ctl00_MainPlaceHolder_gvCategories']/tbody/tr[@class='GVAltRow'][4]/td[4]")

list_of_elements = driver.find_elements_by_xpath("//*")
neco = "/html/body[@id='ctl00_mainbody']/form[@id='aspnetForm']/div[@id='bodybig']/div[@id='pagebig']/div[@id='contentbig']/div[@class='MainHolder'][2]/div[@class='padding5'][1]/div/table[@id='ctl00_MainPlaceHolder_gvCategories']/tbody/tr[@class='GVHeader']/th[2]"
print (list_of_elements)

for elem in list_of_elements:
    if elem == neco:
        print ('radek')
    else:
        print ('element not found')

driver.close()
