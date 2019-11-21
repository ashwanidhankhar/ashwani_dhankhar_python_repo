# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:59:44 2019

@author: BSDU ADMIN
"""


from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"


#For Windows System
browser = webdriver.Chrome("C:\\Users\\BSDU ADMIN\\Desktop\\Ashwani\\Data Handling\\Day_09\\chromedriver.exe")
#browser = webdriver.Firefox(executable_path="D:/geckodriver")

# For Mac System
#browser = webdriver.Chrome(executable_path="/Users/sylvester/chromedriver")
#browser = webdriver.Firefox(executable_path="/Users/sylvester/geckodriver")


browser.get(url)

sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)


sleep(2)


#get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result = browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/input[1]')

get_school_result.click()


sleep(10)
 
html_page = browser.page_source

soup = BS(html_page,"lxml")

# Now you can add your logic of reading from BeautifulSoup

sleep(10)


browser.quit()

table=soup.find("table",id='Table4')

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
k=[]
l=[]
m=[]


for row in table.findAll('tr'):
    cell=row.findAll('td')
    if len(cell)==13:
        a.append(cell[0].text)
        b.append(cell[1].text)
        c.append(cell[2].text)
        d.append(cell[3].text)
        e.append(cell[4].text)
        f.append(cell[5].text)
        g.append(cell[6].text)
        h.append(cell[7].text)
        i.append(cell[8].text)
        j.append(cell[9].text)
        k.append(cell[10].text)
        l.append(cell[11].text)
        m.append(cell[12].text)

col_name=[]
lists=[a,b,c,d,e,f,g,h,i,j,k,l,m]
for i in lists:
    col_name.append(i[0])
    i.pop(0)
        
from collections import OrderedDict

col_data=OrderedDict(zip(col_name,[a,b,c,d,e,f,g,h,i,j,k,l,m]))

import pandas as pd

df=pd.DataFrame(col_data)

print(df)