import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'value': [1,2,3]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)

print('\n')
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pandas.Series(calories, index = ["day1", "day2"])

print(myvar)