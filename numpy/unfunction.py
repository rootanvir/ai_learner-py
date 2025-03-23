import numpy as np

a=[1,2,3,4]
b=[3,4,5,7]
c=[]
for i,j in zip(a,b):
    c.append(i+j)


def myadd(x, y):
  return x*y/2

myadd = np.frompyfunc(myadd, 2, 1)

#print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.divide(arr1,arr2))
#print(np.power(arr1,arr2))
print(np.remainder(arr1,arr2))


print(np.trunc([-3.23232,3.23232]))
print(np.round(3.2121))
print(np.ceil(3.2121))
print(np.floor(3.2121))

print(np.log10([arr1]))

print(np.sum([arr1,arr2]))
x = np.array([1,2,3])
print(np.cumsum(x))
print(np.cumprod(x))
print(np.diff(x))
print(np.lcm(4,6))
print(np.gcd(4,6))
print(np.sin(90))
print(np.cos(90))
print(np.tan(90))
print(np.deg2rad(90))
print(np.rad2deg(22/7))
print(np.hypot(3,4))
print(np.sinh(180))
print(np.cosh(180))
print(np.setdiff1d(arr1,arr2,assume_unique=True))