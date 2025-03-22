import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x=np.where(arr==12)
print(x)
print(np.where(arr%2 == 1))