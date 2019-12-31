"which male and female prof has the highest and the lowest salary"


import pandas as pd

df=pd.read_csv("salaries.csv")


df_max=df.groupby(['sex','rank'])['salary'].max()
df_min=df.groupby(['sex','rank'])['salary'].min()

df_min['Female','Prof']
df_min['Male','Prof']
df_max['Male','Prof']
df_max['Female','Prof']



##########################################################
"Which prof takes the highest and lowest salary"

prof_max=df.groupby(['rank'])['salary'].max()
prof_min=df.groupby(['rank'])['salary'].min()


print(prof_min['Prof'])

print(prof_max['Prof'])

####################################################

"""Missing salaries- should be mean of the matching salaries of 
whose service is same 
"""
import numpy as np

#finding null values
df[df['salary'].isnull()]

mean=df.groupby('service')['salary'].mean()

df['salary'].fillna(df.groupby('service')['salary'].mean())

df1=pd.DataFrame(df['salary'].isnull(),index=df['service'])

