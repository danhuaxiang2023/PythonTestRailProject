import re

# URI: https://www.w3schools.com/python/python_regex.asp

# Character	Description	                                                                Example	
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word   
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"   r"ain\b"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"

# 1. findall() function returns a list containing all matches
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)

#Search for a sequence that starts with "he", followed by 0 or 1 (any) characters, and an "o":
x = re.findall("he.?o", txt)   #==> []
print(x)


#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)


txt = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)


# 2. search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

#Make a search that returns no match:
txt = "The rain in Spain"
x = re.search("Porgul", txt)
print(x)

x = re.search("ai", txt)
print(x)

# Search for the first white-space character in the string:
x = re.search("\s", txt)
print(type(x))
print("The first white-space character is located in position:", x.start())


# 3. split() function
x = re.split("\s", txt)  # Split the string only at the first occurrence:
print(x)
x = re.split("\s", txt, 1)  # Split the string only at the first occurrence:
print(x)

# 4. sub() function
# Replace every white-space character with the number 9:
x = re.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrences:
x = re.sub("\s", "#", txt, 2)
print(x)

# 5. 
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

x = re.search(r"\bS\w+", txt)
#Search for an upper case "S" character in the beginning of a word, and print its position:
print(x.span())
#The string property returns the search string:
print(x.string)
#Search for an upper case "S" character in the beginning of a word, and print the word:
print(x.group())
