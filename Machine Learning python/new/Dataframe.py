# Code 1 Adding Column using other Columns
import pandas as pd
room_length = [18,20,18,17,10]
room_breadth = [20,20,10,11,19]
room_type = ['Big', 'Normal', 'Big', 'Big', 'Normal']
data = pd.DataFrame({'Length':room_length, 'Breadth':room_breadth, 'Type':room_type})
print(data)
data['Area'] = data['Length']*data['Breadth']
print(data)

# Code 2 One-Hot Encoding 
import pandas as pd
age = [18,20,23,19,18,22]
city = ['city A', 'city B', 'city B', 'city A', 'city C', 'city B']
data = pd.DataFrame({'age':age, 'city':city})
print(data)
dummy_features = pd.get_dummies(data['city'])
data_age = pd.DataFrame(data=data, columns=['age'])
data_mod = pd.concat([data_age.reset_index(drop=True), dummy_features],axis=1)
print(data_mod)

# Code 3 Label Encoding
import pandas as pd
from sklearn import preprocessing
marks_science = [78,56,87,91,45,62]
marks_maths = [75,62,90,95,42,57]
grades = ['A', 'B', 'C', 'A', 'D', 'B']
data = pd.DataFrame({'Science Marks': marks_science, 'Maths Marks': marks_maths, 'Total Grade':grades})
print(data)
le = preprocessing.LabelEncoder()
le.fit(data['Total Grade'])
data['Total Grade'] = le.transform(data['Total Grade'])
print(data)

# Code 4
import pandas as pd
import numpy as np
apartment_area = [420,230,123,234,124]
apartment_price = [23400,23400,2300,22100,16700]
data = pd.DataFrame({'Area': apartment_area, 'Price': apartment_price})
print(data)
data['Price']=np.where(data['Price']>20000, 'High', np.where(data['Price']<15000, 'Low', 'Medium'))
print(data)