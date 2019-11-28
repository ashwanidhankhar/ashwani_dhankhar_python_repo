# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:11:27 2019

@author: ashwa
"""

from sklearn.datasets import load_iris
import pandas as pd

dataset=load_iris()

x=pd.DataFrame(dataset.data,columns=dataset.feature_names)

x.shape
print(x.head(10))

#tells some details for the columns
print(x.describe())

#shows the corealtion
x.corr()


"""
data=pd.read_csv('students.csv')

data.head()
data.describe()
"""

