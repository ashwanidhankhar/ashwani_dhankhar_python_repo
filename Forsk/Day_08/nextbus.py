# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:23:28 2019

@author: BSDU ADMIN
"""


"""
Code Challenge
  Name: 
    Next Bus
  Filename: 
    nextbus.py
  Problem Statement:
    Write a Python code to find when will the next bus come
    Try to make the program generalised so that is in not hard wired for bus route 22 and stop id 14787
    Also try if you can take the arguments from the command line
    Also try if you can run the program as a script from comand line
    
  Sample:
      Route 22 and Stop 14787
      Route 0 and Stop 5037
      
  Hint: 
    http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route=22&stop=14787 
"""


import requests

url="    http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route=22&stop=14787 "

response=requests.get(url)

data=response.text

import re

pattern=re.compile(r'min*|delayed*')

time=re.search(pattern,data)

print(time)