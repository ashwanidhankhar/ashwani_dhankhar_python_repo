# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:10:45 2019

@author: ashwa
"""


"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
  Hint:
      Try to use enumerate
"""
user=input(" Enter the list of numbers :")

nums=user.split(",")

nums=[int(i) for i in nums]
 
sum1 = 0

if not nums:
    print(0)

for x in range(len(nums)):
    if nums[x]!=13:
        if x==0 or nums[x-1]!=13:
            sum1+=nums[x]
print("The sum after unlucky 13 is {}".format(sum1))