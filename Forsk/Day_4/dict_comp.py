# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:28:31 2019

@author: ashwa
"""

"""
Code Challenge

Consider the following problem, where you want to create a new dictionary 
where the key is a number divisible by 2 in a range of 0-10 and 
it's value is the square of the number. 

First write the solution using for loop and then rewrite using Comprehension
"""


dict1={i:i**2 for i in range(10) if i%2== 0}


"""
Code Challenges
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Let's suppose you need to create a new dictionary from a given dictionary 
but with items that are greater than 2

In the problem above, what if you have to not only get the items greater than 2 
but also need to check if they are multiples of 2 at the same time. 

"""


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict2={key:val for key,val in dict1.items() if val > 2 if val % 2== 0}



"""
Code Challenge
Use a dictionary comprehension to count the length of each word in a sentence.
"""

sen = "marry had a little lamb"

dict1={word:len(word) for word in sen.split(" ")}



"""
Code Challenge

For all the numbers 1-1000, use a nested list/dictionary comprehension to find 
the highest single digit any of the numbers is divisible by 3

"""

#using list comprehension
list1 = [max( [i for i in range(1,1000) if i % 3 == 0 if len(str(i)) == 1])]

