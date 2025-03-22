from numpy import random

x = random.uniform(10,2,size=(2, 3))

print(x)
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()