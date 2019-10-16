# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:49:16 2019

@author: BSDU ADMIN
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&apiKey=56d770544bdf8552cc75
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR&appid=56d770544bdf8552cc75
    
"""

import requests

USD=int(input("Enter the amount in USD :"))

url="http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&apiKey=56d770544bdf8552cc75"

response=requests.get(url)

response.content

data=response.json()

INR=data["results"]["USD_INR"]["val"]

Conversion=USD*INR

print("{} USD TO INR  =  {} ".format(USD,Conversion))
