# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:17:34 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""


user=input("Enter the list of numbers :")

list1=user.strip().split(",")

tuple1=tuple(list1)

print(list1,"\n",tuple1)