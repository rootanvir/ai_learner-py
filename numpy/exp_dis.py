from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


sns.displot(random.exponential(size=1000),kde=False)
plt.show()