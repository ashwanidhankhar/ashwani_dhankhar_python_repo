# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:44:32 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
#enter the number of maximum number of columns
num=5


#loop for pattern in ascending order
for i in range(0,num+1):
    print("*"*i)

#loop for patter in descending order
for i in range(num-1,0,-1):
    print("*"*i)