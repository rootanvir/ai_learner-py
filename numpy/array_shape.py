import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8 ]])

print(arr.shape)
#output 2 ,4 which mean 2 dim and 4 elements
##Reshape


b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newb = b.reshape(2,3,2)
newb = b.reshape(4,3)
print(newb)
