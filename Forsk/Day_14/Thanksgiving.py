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
import numpy as np

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


#######################################################################################


#Using apply to gender column

def gender_code(gender_string):  
    if (gender_string == "Male") :
        return 0
    elif (gender_string == "Female") :
        return 1   

df["Gender"]=df["Gender"].apply(gender_code)


#Using apply to cleanup income
df.groupby('Combined Earning')["ID"].count()


def income_cleanup(clean):
    if( clean == "Prefer not to answer"):
        return None
    elif( clean == "nan"):
        return None
    elif( clean == "$200,000 and up"):
        return 200000
    elif(isinstance(clean,float)):
        return None
    a,b=(clean.split("to")[0].replace("$","").replace(",","").strip(),clean.split("to")[1].replace("$","").replace(",","").strip())
    return (int(a)+int(b))/2 

    
    
#int(df["Combined Earning"].tolist()[1].split("to")[0].replace("$","").replace(",","").strip())+int(df["Combined Earning"].tolist()[1].split("to")[1].replace("$","").replace(",","").strip())
    
df["Combined Earning"]=df["Combined Earning"].apply(income_cleanup)

df[df["Combined Earning"].isnull()]


#Handling nan values by forward fill
df["Combined Earning"]=df["Combined Earning"].fillna(df["Combined Earning"].mean())

############################################################################################

"""
compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
"""

df.groupby('Cranberry Saucedo Type').size()

#grouping for sauce Canned
can_sauce=df.groupby('Cranberry Saucedo Type').groups['Canned'].tolist()

can_l=[]
for i in can_sauce:
    can_l.append(df.iloc[i,63])
    
can_df=pd.DataFrame(can_l)



#grouping of people Homemade
home_sauce=df.groupby('Cranberry Saucedo Type').groups['Homemade'].tolist()


home_l=[]
for i in home_sauce:
    home_l.append(df.iloc[i,63])

home_df=pd.DataFrame(home_l)

#mean of income of people
plot_sauce=[home_df.mean(),can_df.mean()]

#plot pie chart for the mean of people who tend for different sauces
plt.pie(plot_sauce,labels=['AVerage Earning of People who tend for Homemade Sauce','AVerage Earning of People who tend for Canned Sauce'])



#########################################################################


"""
find the average income for people who served each type of cranberry sauce
for Thanksgiving (Canned, Homemade, None, etc).
"""

key_list=df.groupby('Cranberry Saucedo Type 2').groups.keys()
key_list=list(key_list)

value_list=[]
for i in key_list[1:]: 
    value_list.append((df.groupby('Cranberry Saucedo Type 2').groups[i].values).item())
q=df.groupby('Cranberry Saucedo Type 2').groups[key_list[0]].values
value_list.append(q[1])
value_list.append(q[0])

value_l=[]
for i in value_list:
    value_l.append(df.iloc[i,63])

value_df=pd.DataFrame(value_l)

value_df.mean()


"""
Do people in Suburban areas eat more Tofurkey than people in Rural areas?
"""
#group of people area wise
df.groupby("Area Category").size()

#list of people in rural areas
rural=df.groupby("Area Category").groups['Rural'].tolist()

rurall=[]
for i in rural:
    rurall.append(df.iloc[i,2])

#People who eat tourkey in rural area
rural_Tofurkey=pd.DataFrame(rurall,columns=['a']).groupby('a').size()['Tofurkey']


#list of people in suburban area
Suburban=df.groupby("Area Category").groups['Suburban'].tolist()

suburbanl=[]
for i in Suburban:
    suburbanl.append(df.iloc[i,2])
    
#People who eat tourkey in suburban area

Suburban_Tofurkey=pd.DataFrame(suburbanl,columns=['a']).groupby('a').size()['Tofurkey']

print("People Who eat Tofurkey in Suburban = ",Suburban_Tofurkey)
print("People Who eat Tofurkey in Rural = ",rural_Tofurkey)



"""
Where do people go to Black Friday sales most often?
"""
#people who shop on black friday sales
Black_yes=df.groupby("Shop Blackfriday").groups['Yes'].tolist()

#Region where people visit for black friday sales 
black_l=[]
for i in Black_yes:
    black_l.append(df.iloc[i,64])

#plotting where people go for shopping on black friday sales
plt.pie(pd.DataFrame(black_l,columns=['b']).groupby('b').size(),labels=(pd.DataFrame(black_l,columns=['b']).groupby('b').size()).index.tolist())
plt.title("On Black Friday Sales PLaces where people go")

"""
Is there a correlation between praying on Thanksgiving and income?
"""

"""
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

#changing names into dataframe
df.columns=col_names
"""
# people who dont pray
Pray_no=df.groupby("Pray").groups['No'].tolist()

#list of people who dont pray with income
PrayNoL=[]
for i in Pray_no:
    PrayNoL.append(df.iloc[i,63])
#grouping of people income who doesnt pray
pd.DataFrame(PrayNoL,columns=['c']).groupby('c').size()
#Plotting income groups of people who dont pray on thanksgiving
plt.pie(pd.DataFrame(PrayNoL,columns=['c']).groupby('c').size(),labels=(pd.DataFrame(PrayNoL,columns=['b']).groupby('b').size()).index.tolist())
plt.title("Income Groups Of people who dont pray")


# people who pray
Pray_yes=df.groupby("Pray").groups['Yes'].tolist()

#list of people who pray with income
PrayYesL=[]
for i in Pray_yes:
    PrayYesL.append(df.iloc[i,63])
#grouping of people income who pray
pd.DataFrame(PrayYesL,columns=['d']).groupby('d').size()

#plotting the income group of people who pray on thanksgiving
plt.pie(pd.DataFrame(PrayYesL,columns=['d']).groupby('d').size(),labels=(pd.DataFrame(PrayYesL,columns=['b']).groupby('b').size()).index.tolist())
plt.title("Income Groups Of people who pray")




"""
    What income groups are most likely to have homemade cranberry sauce?

"""

#grouping of people Homemade
home_cran=df.groupby('Cranberry Saucedo Type').groups['Homemade'].tolist()


home_cranl=[]
for i in home_cran:
    home_cranl.append(df.iloc[i,63])

pd.DataFrame(home_cranl,columns=['d']).groupby('d').size().max()

plt.pie(pd.DataFrame(home_cranl,columns=['d']).groupby('d').size(),labels=(pd.DataFrame(home_cranl,columns=['b']).groupby('b').size()).index.tolist(),explode=[0,0,0,0,0,0,0,0.1,0,0,0])
plt.title("Income groups of people who prefer homemade cranbery sauce")


#df.groupby(['Cranberry Saucedo Type'])['Combined Earning'].value_counts().unstack()['Homemade']

"""
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
"""

#group of people area wise
df.groupby("Area Category").size()

#list of people in rural areas
rural_main=df.groupby("Area Category").groups['Rural'].tolist()

rural_mainl=[]
for i in rural_main:
    rural_mainl.append(df.iloc[i,2])

#People who live in rural area group wise main dish
rural_people=pd.DataFrame(rural_mainl,columns=['Rural']).groupby('Rural').size()

print(rural_people)

#list of people in suburban area
Suburban_main=df.groupby("Area Category").groups['Suburban'].tolist()

suburban_mainl=[]
for i in Suburban_main:
    suburban_mainl.append(df.iloc[i,2])
    
#People who live in  suburban area

Suburban_people=pd.DataFrame(suburban_mainl,columns=['Suburban']).groupby('Suburban').size()

print(Suburban_people)


#list of people in urban area
urban_main=df.groupby("Area Category").groups['Urban'].tolist()

urban_mainl=[]
for i in urban_main:
    urban_mainl.append(df.iloc[i,2])
    
#People who live in urban area
urban_people=pd.DataFrame(urban_mainl,columns=['Urban']).groupby('Urban').size()

print(urban_people)

#df.groupby(['Main Dish'])['Area Category'].value_counts().unstack()


"""
   Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
"""
final_pattern=[]
#number of people cranberry sauce and turducken
df.groupby(['Main Dish'])['Cranberry Saucedo Type'].value_counts()['Turducken']

#index for people eat turducken as dinner
Main_index=df.groupby(['Main Dish']).groups['Turducken'].tolist()
#index of people who prefer homemade cranberry sauce
Sauce_index=df.groupby(['Cranberry Saucedo Type']).groups['Homemade'].tolist()

#combining people who eat turducken and home made cranberry sauce
tur_home_index=[]
for i in Main_index:
    if i in Sauce_index:
        tur_home_index.append(i)
#income of people who eat turducken and homemade cranberry
income_tur_home_index=[]        
for i in tur_home_index:
    income_tur_home_index.append(df.iloc[i,63] )

final_pattern.extend((pd.DataFrame(income_tur_home_index)).mean().tolist())


#Canned

Sauce_Cran=df.groupby(['Cranberry Saucedo Type']).groups['Canned'].tolist()
income_can_index=[]        
for i in Sauce_Cran:
    income_can_index.append(df.iloc[i,63] )
    
final_pattern.extend((pd.DataFrame(income_can_index)).mean().tolist())

#roast beef

Main_roast=df.groupby(['Main Dish']).groups['Roast beef'].tolist()

income_roast=[]        
for i in Main_roast:
    income_roast.append(df.iloc[i,63] )

final_pattern.extend((pd.DataFrame(income_roast)).mean().tolist())

#plotting income based pattern verification
plt.pie(final_pattern,labels=['Homemade cranberry turducken','Canned cranberry','Roast beef'],autopct='%1.2f%%')
plt.title("Income Patterns")