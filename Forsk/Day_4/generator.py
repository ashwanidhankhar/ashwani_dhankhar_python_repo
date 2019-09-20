# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:56:29 2019

@author: ashwa
"""


"""
Code Challenge 1
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]
"""


def gen(list1):
    a=0
    list2=[]
    for i in list1:
        list2.append(i)
        a+=i
        yield(a/len(list2))
        
            
list1=[7, 13, 17, 231, 12, 8, 3]    

result=gen(list1)

next(result)



"""
Code Challenge 7

https://github.com/thecbp/blog_data/blob/master/recipeData.csv

The data contains important beer characteristics from brewers around the world, 
including style of beer, alcohol by volume (ABV), and amount of beer produced.

"""

import csv
def gen_csv():
    with open("recipeData.csv") as file:
        csv_reader=csv.reader(file,delimiter=",")
        for i in csv_reader:
            yield(i)
            
data = gen_csv() 

next(data)

        