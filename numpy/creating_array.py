import numpy as np
def creating_array():
    arr = np.array([1,2,3,4])
    arr2 = np.array([[1,2,3],[4,5,6]])
    arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr3)
    print(arr3.ndim)
    print(arr[-1]) # negative mean start from end
creating_array()