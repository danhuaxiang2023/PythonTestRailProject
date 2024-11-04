#List: ordered, changeble, allow duplicates
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

thislist = ["apple", "banana", "cherry", "apple", "cherry","orange", "kiwi", "melon", "mango"]
print(thislist)

# 1. List Index 
print(thislist[0])
print(thislist[-1])
#The search will start at index 2 (included) and end at index 5 (not included)
print(thislist[2:5])
print(thislist[:4])

# 2. Change list item
thislist[1:2] = ["blackcurrant", "watermelon"]  #Change the second value by replacing it with two new values
print(thislist)

# 3. Add list item
thislist.append("orange")
print(thislist)

thislist.insert(1, "orange")
print(thislist)

# 4. Remove list item
thislist.remove("orange")
print(thislist)

thislist.pop(1)   #remove 2nd item
print(thislist)

thislist.pop()   #remove last item
print(thislist)

del thislist[0] #remove 1st item
print(thislist)
# del thislist   #delet the list completely
# print(thislist)

# 5. Loop Lists
# for x in thislist:
#   print(x)

# for i in range(len(thislist)):
#   print(thislist[i])  

# [print(x) for x in thislist]

# 6. List Comprehension
newlist = [x for x in thislist if "a" in x]
print(newlist)


# 7. Join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

# 8. Sort list
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

# 9. Copy List
mylist = thislist  # not copy, mylist only be a reference to thislist
mylist1 = thislist.copy()
print(mylist1)

mylist2 = list(mylist1)
mylist2.pop(0)
print(mylist1)
print(mylist2)


