import pandas as pd

a = [1, 7, 2]
print(pd.Series(a))
print(pd.Series(a,index=["x","y","z"]))
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
calories = {"day1": 420, "day2": 380, "day3": 390}

#Key/value
print(pd.Series(calories))
#DataFrames
print(pd.DataFrame(data))