from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

x = iris.data[:,:1]
y = iris.target

# Box Plot
plt.boxplot(x)
plt.show()

# Histogram
plt.hist(x)

# Scratter PLot
x = iris.data[:,:3]

plt.scatter(x[:,2],x[:,0])
plt.xlabel('Petal Length')
plt.ylabel('Sepal Length')