# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:11:18 2019

@author: BSDU ADMIN
"""

"""
Code Challenge:
  Name:
    Bid Plus
  Filename:
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
         
          # Optional - Do not do this
          7. Name of the PDF file
         
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""

from selenium import webdriver
from time import sleep

url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("C:\\Users\\BSDU ADMIN\\Desktop\\Ashwani\\Data Handling\\Day_09\\chromedriver.exe")

browser.get(url)

sleep(2)

A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []

for i in range(1,11):
   
    bid = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    quantity = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text
    dept = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    start_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[0:10]
    start_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[10:]
    end_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[0:10]
    end_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[10:]
           
    A.append(bid)
    B.append(items)
    C.append(quantity)
    D.append(dept)
    E.append(start_date)
    F.append(start_time.strip())
    G.append(end_date)
    H.append(end_time.strip())

from collections import OrderedDict

col_name = ["BID_No.","Items","Quantity","Department","Start_Date","Start_Time","End_Date","End_Time"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F,G,H]))

import pandas as pd

df = pd.DataFrame(col_data)
df.to_csv('bid_plus.csv')
