# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:23:19 2019

@author: BSDU ADMIN
"""

"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
"""


import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("thanksgiving-2015-poll-data.csv")


#converting column names to single word names

col_names=list(df.columns)

m=1
for i in range(11,26):
    col_names[i]="Side Dish"+" "+str(m)
    m+=1
m=1
for i in range(26,39):
    col_names[i]="Pie"+" "+str(m)
    m+=1  
m=1
for i in range(31,51):
    col_names[i]="Dessert"+" "+str(m)
    m+=1

col_names[62]="Gender"
col_names[63]="Combined Earning"
col_names[60]="Area Category"
col_names[51]="Pray"
col_names[52]="Travel"
col_names[53]="Macy's Parade"
col_names[54]="Age Cutoff Kids"
col_names[55]="Hometown Meetup"
col_names[56]="Attended Friendsgiving"
col_names[57]="Shop Blackfriday"
col_names[58]="Retail Work"
col_names[59]="Employer Blackfriday"
col_names[1]="Celebration"
col_names[2]="Main Dish"
col_names[3]="Main Dish 2"
col_names[4]="Cooking Process"
col_names[5]="Cooking Process 2"
col_names[6]="Stuffing/Dressing"
col_names[7]="Stuffing/Dressing 2"
col_names[8]="Cranberry Saucedo Type"
col_names[9]="Cranberry Saucedo Type 2"
col_names[10]="Gravy"
col_names[0]="ID"

##########################################

#changing names into dataframe
df.columns=col_names

#people region wise
df.groupby('US Region').size()

#group wise described data
df.groupby('US Region').groups

#########################################

#List ID for people in East North Central Region
ID_ENC=df.groupby('US Region').groups['East North Central'].tolist()
ID_ESC=df.groupby('US Region').groups['East South Central'].tolist()
ID_MA=df.groupby('US Region').groups['Middle Atlantic'].tolist()
ID_MOUNT=df.groupby('US Region').groups['Mountain'].tolist()
ID_NE=df.groupby('US Region').groups['New England'].tolist()
ID_PACI=df.groupby('US Region').groups['Pacific'].tolist()
ID_SA=df.groupby('US Region').groups['South Atlantic'].tolist()
ID_WNC=df.groupby('US Region').groups['West North Central'].tolist()
ID_WSC=df.groupby('US Region').groups['West South Central'].tolist()

#REGION BASED DATA SEGRIGATION 

#cREATING LISTS FOR DINNER REGION WISE
ID_ENCL=[]
for i in ID_ENC:
    ID_ENCL.append(list(df.iloc[i,2:51]))

ID_ESCL=[]
for i in ID_ESC:
    ID_ESCL.append(list(df.iloc[i,2:51]))

ID_MAL=[]
for i in ID_MA:
    ID_MAL.append(list(df.iloc[i,2:51]))

ID_MOUNTL=[]
for i in ID_MOUNT:
    ID_MOUNTL.append(list(df.iloc[i,2:51]))

ID_NEL=[]
for i in ID_NE:
    ID_NEL.append(list(df.iloc[i,2:51]))

ID_PACIL=[]
for i in ID_PACI:
    ID_PACIL.append(list(df.iloc[i,2:51]))
    
ID_SAL=[]
for i in ID_SA:
    ID_SAL.append(list(df.iloc[i,2:51]))
    
ID_WNCL=[]
for i in ID_WNC:
    ID_WNCL.append(list(df.iloc[i,2:51]))
    
ID_WSCL=[]
for i in ID_WSC:
    ID_WSCL.append(list(df.iloc[i,2:51]))




#Dataframes for Region wise dinner
East_North_Central=pd.DataFrame(ID_ENCL,columns=col_names[2:51])
East_South_Central=pd.DataFrame(ID_ESCL,columns=col_names[2:51])
Middle_Atlantic=pd.DataFrame(ID_MAL,columns=col_names[2:51])
Mountain=pd.DataFrame(ID_MOUNTL,columns=col_names[2:51])
New_england=pd.DataFrame(ID_NEL,columns=col_names[2:51])
Pacific=pd.DataFrame(ID_PACIL,columns=col_names[2:51])
South_Atlantic=pd.DataFrame(ID_SAL,columns=col_names[2:51])
West_North_Central=pd.DataFrame(ID_WNCL,columns=col_names[2:51])
West_South_Central=pd.DataFrame(ID_WSCL,columns=col_names[2:51])
                 
    
# Pattern in East Central Region

#for main dish
East_North_Central.groupby('Main Dish').size()

#for cooking process
East_North_Central.groupby('Cooking Process').size()

#Dressing used
East_North_Central.groupby('Stuffing/Dressing').size()

#pie charts for East North Central
plt.pie(East_North_Central.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','others','Rice-Base'])
plt.title("East Central Region Stuffing/Dressing")

plt.pie(East_North_Central.groupby('Cooking Process').size(),labels=['Baked','Fried','I dont know','Other','Roasted'])
plt.title("East Central Region Cooking Process")

plt.pie(East_North_Central.groupby('Main Dish').size(),labels=['Ham/Pork','Other','Tofurkey','Turkey'])
plt.title("East Central Region Main Dish")


# Pattern in East South Region

#for main dish
East_South_Central.groupby('Main Dish').size()

#for cooking process
East_South_Central.groupby('Cooking Process').size()

#Dressing used
East_South_Central.groupby('Stuffing/Dressing').size()

#pie charts for East south 
plt.pie(East_South_Central.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','others'])
plt.title("East South Region Stuffing/Dressing")


plt.pie(East_South_Central.groupby('Cooking Process').size(),labels=['Baked','Fried','I dont know','Other','Roasted'])
plt.title("East South Region Cooking Process")


plt.pie(East_South_Central.groupby('Main Dish').size(),labels=['Ham/Pork','Other','Roast Beef','Turkey'])
plt.title("East South Region Main Dish")




# Pattern in Middle_Atlantic Region

#for main dish
Middle_Atlantic.groupby('Main Dish').size()

#for cooking process
Middle_Atlantic.groupby('Cooking Process').size()

#Dressing used
Middle_Atlantic.groupby('Stuffing/Dressing').size()

#pie charts forMiddle_Atlantic
plt.pie(Middle_Atlantic.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','others','Rice based'])
plt.title("Middle_Atlantic Region Stuffing/Dressing")


plt.pie(Middle_Atlantic.groupby('Cooking Process').size(),labels=['Baked','Fried','Other','Roasted'])
plt.title("Middle_Atlantic Region Cooking Process")


plt.pie(Middle_Atlantic.groupby('Main Dish').size(),labels=['Chicken','Ham/Pork','Other','Roast Beef','Tofurkey','Turducken','Turkey'])
plt.title("Middle_Atlantic Region Main Dish")



# Pattern in Mountain Region

#for main dish
Mountain.groupby('Main Dish').size()

#for cooking process
Mountain.groupby('Cooking Process').size()

#Dressing used
Mountain.groupby('Stuffing/Dressing').size()

#pie charts forMiddle_Atlantic
plt.pie(Mountain.groupby('Stuffing/Dressing').size(),labels=['Bread Based','others','Rice based'])
plt.title("Mountain Region Stuffing/Dressing")


plt.pie(Mountain.groupby('Cooking Process').size(),labels=['Baked','Other','Roasted'])
plt.title("Mountain Region Cooking Process")


plt.pie(Mountain.groupby('Main Dish').size(),labels=['Chicken','Ham/Pork','Tofurkey','Turkey'])
plt.title("Mountain Region Main Dish")



# Pattern in New_england Region

#for main dish
New_england.groupby('Main Dish').size()

#for cooking process
New_england.groupby('Cooking Process').size()

#Dressing used
New_england.groupby('Stuffing/Dressing').size()

#pie charts for New_england
plt.pie(New_england.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','Other'])
plt.title("New_england Region Stuffing/Dressing")


plt.pie(New_england.groupby('Cooking Process').size(),labels=['Baked','Fried','I dont know','Other','Roasted'])
plt.title("New_england Region Cooking Process")


plt.pie(New_england.groupby('Main Dish').size(),labels=['Chicken','other','Tofurkey','Turkey'])
plt.title("New_england Region Main Dish")



# Pattern in Pacific Region

#for main dish
Pacific.groupby('Main Dish').size()

#for cooking process
Pacific.groupby('Cooking Process').size()

#Dressing used
Pacific.groupby('Stuffing/Dressing').size()

#pie charts for New_england
plt.pie(Pacific.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','Other','Rice based'])
plt.title("Pacific Region Stuffing/Dressing")


plt.pie(Pacific.groupby('Cooking Process').size(),labels=['Baked','Fried','I dont know','Other','Roasted'])
plt.title("Pacific Region Cooking Process")


plt.pie(Pacific.groupby('Main Dish').size(),labels=['Ham/Pork','I dont know','Other','Roast Beef','Tofurkey','Turducken','Turkey'])
plt.title("Pacific Region Main Dish")



# Pattern in South_Atlantic Region

#for main dish
South_Atlantic.groupby('Main Dish').size()

#for cooking process
South_Atlantic.groupby('Cooking Process').size()

#Dressing used
South_Atlantic.groupby('Stuffing/Dressing').size()

#pie charts for South_Atlantic
plt.pie(South_Atlantic.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','Other','Rice based'])
plt.title("South_Atlantic Region Stuffing/Dressing")


plt.pie(South_Atlantic.groupby('Cooking Process').size(),labels=['Baked','Fried','I dont know','Other','Roasted'])
plt.title("South_Atlantic Region Cooking Process")


plt.pie(South_Atlantic.groupby('Main Dish').size(),labels=['Chicken','Ham/Pork','Other','Roast Beef','Tofurkey','Turkey'])
plt.title("South_Atlantic Region Main Dish")





# Pattern in West_North_Central Region

#for main dish
West_North_Central.groupby('Main Dish').size()

#for cooking process
West_North_Central.groupby('Cooking Process').size()

#Dressing used
West_North_Central.groupby('Stuffing/Dressing').size()

#pie charts for West_North_Central
plt.pie(West_North_Central.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','Other','Rice based'])
plt.title("West_North_Central Region Stuffing/Dressing")


plt.pie(West_North_Central.groupby('Cooking Process').size(),labels=['Baked','Fried','I dont know','Other','Roasted'])
plt.title("West_North_Central Region Cooking Process")


plt.pie(West_North_Central.groupby('Main Dish').size(),labels=['Chicken','Ham/Pork','I dont know','Other','Tofurkey','Turkey'])
plt.title("West_North_Central Region Main Dish")



# Pattern in West_South_Central Region

#for main dish
West_South_Central.groupby('Main Dish').size()

#for cooking process
West_South_Central.groupby('Cooking Process').size()

#Dressing used
West_South_Central.groupby('Stuffing/Dressing').size()

#pie charts for West_South_Central
plt.pie(West_South_Central.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','Other','Rice based'])
plt.title("West_South_Central Region Stuffing/Dressing")


plt.pie(West_South_Central.groupby('Cooking Process').size(),labels=['Baked','Fried','Other','Roasted'])
plt.title("West_South_Central Region Cooking Process")


plt.pie(West_South_Central.groupby('Main Dish').size(),labels=['Chicken','Ham/Pork','Other','Tofurkey','Turkey'])
plt.title("West_South_Central Region Main Dish")




# Creating subplots of region based dinner division

fig,axs = plt.subplots(2,3)
fig.suptitle('Vertically  subplots')
axs[0,0].pie(East_North_Central.groupby('Stuffing/Dressing').size(),labels=['Bread Based','None','others','Rice-Base'])
axs[0,0].set_title('East_North_Central Region Stuffing/Dressing')
axs[0,1].pie(East_North_Central.groupby('Cooking Process').size(),labels=['Baked','Fried','I dont know','Other','Roasted'])
axs[0,1].set_title('East_North_Central Region Stuffing/Dressing')
axs[0,2].pie(East_North_Central.groupby('Main Dish').size(),labels=['Ham/Pork','Other','Tofurkey','Turkey'])
axs[0,2].set_title('East_North_Central Region Stuffing/Dressing')







#people income wise




df.groupby('Combined Earning')["ID"].count()

