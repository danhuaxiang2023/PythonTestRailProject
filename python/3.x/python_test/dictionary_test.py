# Dictionary: Ordered, Changeable, Duplicates Not Allowed
# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# 1. Access items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#Get the value of the "model" key:
x = thisdict["model"]
x = thisdict.get("model")
print(x)

#Get a list of the keys:
x = thisdict.keys()
print(x)  #before the change
thisdict["color"] = "whilte"
print(x)  #after the change

# 2. Change items
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)

# 3. Add items
thisdict["color"] = "red"
thisdict.update({"color": "red"})

# 4. Remove items
thisdict.pop("model")
thisdict.popitem()  # remove the last inserted item
print(thisdict)
# del thisdict["model"]
# del thisdict  # delete the dic completely
# thisdict.clear()  # empty the dictionary
# print(thisdict)

# 5. Loop dictionary
for x in thisdict:  #Print all key names in the dictionary, one by one:
    print(x)

for x in thisdict.keys():  #Print all key names in the dictionary, one by one:
    print(x)    

for x in thisdict.values():
    print(x)    #Print all values in the dictionary, one by one:

for x, y in thisdict.items():
    print(x, y)    