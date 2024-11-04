# 1. Mofify Strings
a = " Hello, World! "

print(a.strip())
print(a.upper())
print(a.lower())

# 2. Format strings
age = 36
txt = f"My name is John, I am {age}"  #F-Strings with placeholders
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars" # Placeholder with modifier
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# 3. Escape characters with backslash \
# Code	Result	
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "We are the so-called \"Vikings\" from the north."
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
txt = "Hello\tWorld!"
print(txt) 
txt = "This will insert one \\ (backslash)."
print(txt) 
txt = "Hello\nWorld!"
print(txt) 
txt = 'It\'s alright.'
print(txt) 

# 4. String join() method
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

# 5. split method: string.split(separator, maxsplit)
txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

#The rsplit() method splits a string into a list, starting from the right
# Syntax: string.rsplit(separator, maxsplit)
txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)
