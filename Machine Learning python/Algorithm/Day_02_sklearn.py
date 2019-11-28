from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
x = pd.DataFrame(iris.data, columns = iris.feature_names)

print("Shape : ",x.shape)
print("Head : \n",x.head(5))
print("Description : \n",x.describe())
print(x.corr())
print(x.skew())

# Reading zoo.csv
zoo = pd.read_csv('zoo.csv')

print("Shape : ",zoo.shape)
print("Head : \n",zoo.head(5))
print("Description : \n",zoo.describe())
print(zoo.skew())