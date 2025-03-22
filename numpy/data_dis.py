from numpy import random

x = random.choice([3, 5, 7, 9], p=[.1, 0.2, 0.6, 0.1], size=(10))

print(x)