import pandas as pd

df = pd.read_csv('file/sample.csv')
df = df.dropna()
dj = pd.read_json("file/data.json")
#print(df.to_string())
#print(dj.to_string())

x = df["Calories"].median()
y = df["Calories"].mean()
z = df["Calories"].mode()[0]
print(x)
print(y)
print(z)