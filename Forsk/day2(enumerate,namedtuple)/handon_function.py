# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:55:50 2019

@author: ashwa
"""
"""
 Hands On 1  
 Make a function to find whether a year is a leap year or no, return True or False 
 The year can be evenly divided by 4;
If the year can be evenly divided by 100, it is NOT a leap year, unless;
The year is also evenly divisible by 400. Then it is a leap year.

"""

user=int(input("Enter Year   :"))

def leap_year(year):
    leap=False
    if year%4==0 and year%400==0:
        leap=True
    elif year%100==0 and year%400!=0:
        leap=False
    return(leap)
    
leap_year(year=user)
                


"""
Hands On 2
Make a function days_in_month to return the number of days in a specific month of a year
"""



def days_in_month(user):
    dict1={"Jan":,"Feb":,"Mar":,}
    
    



"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

user="I am testing"

def reverse(string):
    string=string[::-1]
    return(string)
    
reverse(string=user)
    



"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse2.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a integer.
    Take input from User  
  Input: 
    -321
  Output:
    -123  
"""
user=input("Enter the number :")

if user[0]=="-"or user[0]=="+":
    user=user[0]+user[:0:-1]
    print(user)
else:
    user=user[::-1]
    print(user)
    

"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

user="This is fun"

def translate(user_t):
    user1=""
    vowels=["a","e","i","o","u"]
    for i in user:
        if i ==" ":
            user1+=i
        elif i not in vowels:
            user1+=i+"o"+i
        else:
            user1+=i
    return(user1)
    
translate(user_t=user)

    


"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""

user1=[5,2,6,2,3]
sum(user)
def operation(user):
    sum1=sum(user)
    Multiply=1
    for i in user:
        Multiply=Multiply*i
    Largest=max(user)
    Smallest=min(user)
    Sort=sorted(user)
    Sets=list(set(user))
    return(print(" Sum = {}\n Multiplication = {}\n Max = {}\n Smallest = {}\n Sorted = {}\n Without Duplicates = {}".format(sum1,Multiply,Largest,Smallest,Sort,Sets)))
    
operation(user=user1)
    