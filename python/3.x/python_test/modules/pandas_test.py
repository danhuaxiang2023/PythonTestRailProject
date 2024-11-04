# py -m pip install pandas

import pandas as pd

#check pandas version
# print(pd.__version__)

#Check the number of maximum returned rows:
# print(pd.options.display.max_rows)

df = pd.read_csv('./python/3.x/output/UnstableCases_BaaS - Regression - WMMC - Milestone 161.csv')
# print(df.head(5))  # Get a quick overview by printing the first 5 rows of the DataFrame
# print(df.tail()) # Print the last 5 rows of the DataFrame
print(df.info())  # Print information about the data
# print(df.to_html)



# Series
# a = [ 1, 2, 7]
# myvar = pd.Series(a)
# print(myvar)
# print(myvar[0])

# # Create Labels
# myvar = pd.Series(a, index=["x","y","z"])
# print(myvar)
# print(myvar['y'])

# # Key/Value Objects as Series
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

# Data Frames
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# df = pd.DataFrame(mydataset)
# print(df)
# print(df.loc[0]) # retrun row 0
# print(df.loc[[0, 1]]) # retrun row 0 and 1

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":None,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":None,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}

df = pd.DataFrame(data)
print(df) 

#Replace NULL values with the number 130:
df.fillna(130, inplace = True)

#Replace NULL values in the "Calories" columns with the number 130:
df['Calories'].fillna(130, inplace=True)

# Remove rows with a NULL value in the 'Calories' Column
df.dropna(subset=['Calories'], inplace = True)  # inplace = true, replace the old df, do not gereate a new df
print(df)

#Replace a given cell
for x in df.index:
    if df.loc[x, 'Duration'] > 50:
        df.loc[x, 'Duration'] = 50  # replace the cell value
        # df.drop(x, inplace=True)  # Delete the row
print(df)  

#Returns True for every row that is a duplicate, otherwise False
print(df.duplicated())
#Remove all duplicates
df.drop_duplicates(inplace=True)