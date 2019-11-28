# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:08:49 2019

@author: ashwa
"""

from sklearn import datasets

iris=datasets.load_iris()

import matplotlib.pyplot as plt

x= iris.data[:,:4]
y=iris.target


plt.boxplot(x)

plt.show()

plt.hist(x)

`9