# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:44:35 2019

@author: ashwa
"""


"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

# input for marks of exams
assignment1=float(input("Enter marks for assignment 1 :"))
assignment2=float(input("Enter marks for assignment 2 :"))
assignment3=float(input("Enter marks for assignment 3 :"))
exam1=float(input("Enter marks for exam 1 :"))
exam2=float(input("Enter marks for exam 2 :"))

#weighted score for the following marks 
weighted_score=(assignment1+assignment2+assignment3)*0.1+(exam1+exam2)*0.35

print(weighted_score)