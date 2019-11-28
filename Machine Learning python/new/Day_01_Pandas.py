# PANDAS

import pandas as pd

a = pd.Series((1,2,3,4,5,6))

data = {'Gender':['F','F','M'],'Emp_id':['E001','E002','E003'],'Age':[10,12,13]}
df = pd.DataFrame(data,columns=['Emp_id','Gender','Age'])
print(df)

data_csv = pd.read_csv('zoo.csv')
print(data_csv)