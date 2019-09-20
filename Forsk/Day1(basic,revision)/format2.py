# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:01:06 2019

@author: ashwa
"""


"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

#enter the desired string 
sentence = input("Enter the string   :")

#new string with replaced characters
sen=sentence.replace(" ","*")

#printing the formated string
print(sen)