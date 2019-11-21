# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:00:01 2019

@author: BSDU ADMIN
"""

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url= "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

source=requests.get(url).text

bs=BeautifulSoup(source,"lxml")


table=bs.find('table',class_='table')

a=[]
b=[]
c=[]
d=[]
e=[]


for row in table.findAll('tr'):
    col=row.findAll('td')
    if len(col)==5:
        a.append(col[1].text.strip())
        
        b.append(col[2].text.strip())
        
        c.append(col[3].text.strip())
        
        d.append(col[4].text.strip())
        
        e.append(col[0].text.strip())
        
        

import pandas as pd
from collections import OrderedDict


col_names=['Position','Country','Matches','points','Rating']

col_data=OrderedDict(zip(col_names,[e,a,b,c,d]))
        
df=pd.DataFrame(col_data)

print(df)

#df.to_csv("odi.csv")