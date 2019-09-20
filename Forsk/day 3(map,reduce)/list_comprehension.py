# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:20:24 2019

@author: ashwa
"""

"""
Code Challenges
"""

"""
Find all of the numbers from 1-1000 that are divisible by 7
"""

numbers = [x for x in range(1,1001) if x%7==0]
print(numbers)

#or by using filter

numbers = filter(lambda x:x%7==0,range(1,1001))
print(list(numbers))

"""
Find all of the numbers from 1-1000 that have a 3 in them
"""

numbers = [x for x in range(1,1001) if '3' in str(x)]

#or by using filter

numbers= filter(lambda x:'3' in str(x),range(1,1001))
print(list(numbers))

"""
Count the number of spaces in a string
"""
string="Bhartiya skill development university "
spaces =[x+1 for i in string if i==" "]
print (sum(spaces))

#or
string="Bhartiya skill development university "
spaces=filter(lambda x:True if(x==" ") else False,string)
print(list(spaces))


"""
Remove all of the vowels in a string

Find all of the words in a string that are less than 4 letters

A list of all consonants in the sentence 'The quick brown fox jumped over the lazy dog'

A list of all the capital letters (and not white space) in 'The Quick Brown Fox Jumped Over The Lazy Dog'

A list of all square numbers formed by squaring the numbers from 1 to 1000.


"""
