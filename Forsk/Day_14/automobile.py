# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:24:00 2019

@author: BSDU ADMIN
"""


"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""


import pandas as pd

df=pd.read_csv("automobile.csv")


# 1 1. Handle the missing values for Price column

#checking the null values
df[df['price'].isnull()]

#calculating the mean for each maker price
mean_audi=df[df['make']=='audi']['price'].mean()
mean_isuzu=df[df['make']=='isuzu']['price'].mean()
mean_porsche=df[df['make']=='porsche']['price'].mean()

#filling the null values at the desired place at the particular place for each maker
df[(df['make']=='isuzu') & (df['price'].isnull())]=df[(df['make']=='isuzu') & (df['price'].isnull())].fillna(mean_isuzu)

df[(df['make']=='audi') & (df['price'].isnull())]=df[(df['make']=='audi') & (df['price'].isnull())].fillna(mean_audi)

df[(df['make']=='porsche') & (df['price'].isnull())]=df[(df['make']=='porsche') & (df['price'].isnull())].fillna(mean_porsche)



# 2. Get the values from Price column into a numpy.ndarray

import numpy as np

array=np.array(df['price'])

print(type(array))
print(array)


#3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price


#minimumprice

minimum_price=df['price'].min()
print(minimum_price)

#maximum price
max_price=df['price'].max()
print(max_price)

#average price or the mean price
avg_price=df['price'].mean()
print(avg_price)

#standard deviation

sd_price=df['price'].std()
print(sd_price)
