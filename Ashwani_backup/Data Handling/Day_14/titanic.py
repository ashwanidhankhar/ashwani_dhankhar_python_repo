# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:54:59 2019

@author: BSDU ADMIN
"""

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Titanic
  Filename: 
      titanic.py
  Dataset:
      training_titanic.csv
  Data Description:      
      survival: Survival (0 = No; 1 = Yes)
      pclass: Passenger Class (1 = Upper; 2 = Middle; 3 = Lower)
      name: Name
      sex: Sex
      age: Age 
      sibsp: Number of Siblings/Spouses Aboard
      parch: Number of Parents/Children Aboard
      ticket: Ticket Number
      fare: Passenger Fare
      cabin: Cabin
      embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

  Problem Statement:
      Titanic ship that crashed in April, 1912.
      Real-world data containing the details of titanic ships passengers list.
      There were lifeboats for only 1178 people
      There were 2224 passengers on board
      Answer the Following:
      0. Total number of Passengers in the dataset
      0. Find all large families (Sibsp > 3)
      0. Find all the features which has missing
      0. Drop the column which has the max missing
      0. Embarked Feature missing values needs to be fixed
      0. Age missing value needs to be fixed
      1. How many people survived the disaster ?
      2. How many people died the disaster ?
      3. Plot the people who survived Vs died appropriately.
      4. Calculate and print the survival rates as proportions (percentage) 
      5. Which gender have greater survival rate ?
         Were females given high priority while rescue.
         Males that survived vs males that passed away
         Females that survived vs Females that passed away
         Also plot it
      6. Does age play a role for survival?
         Since it's probable that children were saved first.
  
  Advanced Problem Statements:
     7. Does Pclass feature plays role in survival
         Survived Vs Died according to Pclass and sex
         Plot it (FactorPlot and CrossTab)
      8. Who was the oldest person survived 
      9. Yougest person survived
      10. Is there a relationship between Pclass and the survival 
          Draw violen plots PClass and Age Vs Survived 
          Sex and Age Vs Survived 
      11. Find the title from the name and show its value counts
          train['title'] = train.Name.str.extract('\, ([A-Z][^ ]*\.)',expand=False)
      12. If a passanger is alone in ship with no siblings, survival rate is 
          If I have a family onboard, I will save them instead of saving myself.
          But there’s something wrong, the survival rate for families 
          with 5–8 members is 0%. Is this because of PClass? Yes this is PClass,
          large families in Pclass3(>3) died.
      13. Everything except ‘PassengerId’, ‘Ticket’ and ‘Name’ would be 
          correlated with a high survival rate
      14. Do Not Delete the Cabin Column, but recreate using Deck
      
      
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
 
     You can test this by creating a new column with a Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.

      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
      
"""


import pandas as pd

df=pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Ashwani\\Data Handling\\Day_14\\training_titanic.csv")

#  0. Total number of Passengers in the dataset

df.count().max()


#  0. Find all large families (Sibsp > 3)

df[df['SibSp']>3]

#  0. Find all the features which has missing

df[df['PassengerId'].isnull()]

#  0. Drop the column which has the max missing

max_nan=df.isnull().sum()
print(max_nan)
del(df['Cabin'])

#  0. Embarked Feature missing values needs to be fixed

df[df['Embarked'].isnull()]

df['Embarked']=df['Embarked'].fillna(method='ffill')

""" or
df.dropna(subset=['Embarked'])
"""

#  0. Age missing value needs to be fixed





#1. How many people survived the disaster ?
 """     2. How many people died the disaster ?
      3. Plot the people who survived Vs died appropriately.
      4. Calculate and print the survival rates as proportions (percentage) 
      5. Which gender have greater survival rate ?
         Were females given high priority while rescue.
         Males that survived vs males that passed away
         Females that survived vs Females that passed away
         Also plot it
      6. Does age play a role for survival?
         Since it's probable that children were saved first.
"""

df = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Ashwani\\Data Handling\\Day_14\\thanksgiving-2015-poll-data.csv)













