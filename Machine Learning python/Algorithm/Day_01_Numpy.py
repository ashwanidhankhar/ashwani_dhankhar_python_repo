import numpy as np
a = np.array([[0,1,2],
             [3,4,5]])

print(a)
print(a.shape)

a_1 = np.array([[1,2,3],
                [4,5,6]])

# Addition
print(a+a_1)
# OR
print(np.add(a,a_1))

# Substraction
print(a-a_1)
# OR
print(np.subtract(a,a_1))

# Multiplication
print(np.multiply(a,a_1))

# Divide
print(np.divide(a,a_1))

# Square
print(np.sqrt(a))

# Sum
print(np.sum(a))

# Transpose
print(a.T)

# Zero Matrics
b = np.zeros((3,3))
print(b)

# One Matrics
c = np.ones((3,3))
print(c)