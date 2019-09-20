# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:26:46 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

from collections import Counter

words="www.google.com"
freq=Counter(words)

print(freq)




#####logical######
words="www.google.com"
words=",".join(words)
words=words.split(",")
dict1=defaultdict()
for i in words:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
print(dict1)