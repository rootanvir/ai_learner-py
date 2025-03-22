import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random 
x = random.randint(10,size=10)
print(x)
sns.distplot([5,6,7,8,9,10,11,12,13])
plt.show()