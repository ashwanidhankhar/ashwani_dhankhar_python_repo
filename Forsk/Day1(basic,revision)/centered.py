# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:53:57 2019

@author: ashwa
"""


"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""
list_of_numbers=input("Enter the list of numbers :")
list1=list_of_numbers.split(",")
list1=[int(i) for i in list1]
list1.sort()
list1.pop()
list1.pop(0)
a=0
for i in list1:
    a+=i
    final_average=a//len(list1)
    
print(final_average)