# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:58:09 2019

@author: ashwa
"""


"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

      names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)



(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)


Rewrite the above code using map.
    

"""

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)

#######
new= map(lambda names : hash(names),names)
print(list(new))

