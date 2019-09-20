# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:34:26 2019

@author: ashwa
"""

"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""


import re


pattern = re.compile(r"[\w\d_-]*\@[\w\d]+\.[\w]{3}")

user=input("enter the email  :")

matched=pattern.match(user)

if matched:
    print(user)
else:
    print("Not valid")