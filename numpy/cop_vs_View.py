import numpy as np
arr = np.array([1,2,3,4,5,6])
x = arr.copy()
arr[0] = -1
print(arr)
print(x)

# view

b = np.array([1, 2, 3, 4, 5])
y = b.view()
b[0] = -6

print(b)
print(y)