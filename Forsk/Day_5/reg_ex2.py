# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:08:43 2019

@author: ashwa
"""

"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""



import re

pattern = re.compile(r"[\w\d_-]*@[\w\d]*\.[\w]{2,4}")

user=input("Enter the website name  :").split(",")

matched=[pattern.findall(i) for i in user]

print(sorted(matched))
