# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:34:36 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""


string="Python 3.2"
d=0
l=0
for i in string:
    if i.isdigit():
        d+=1
    if i.isalpha():
        l+=1

dict1={"Digits":d,"Letters":l}

for key,value in dict1.items():
    print (key,":",value)