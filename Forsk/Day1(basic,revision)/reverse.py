# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:50:38 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

#string to be reversed
string=input("Enter the string to be reversed :")

#reversed string
new_string=string[::-1]

#printing the reversed string
print(new_string)