import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('file/sample.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()