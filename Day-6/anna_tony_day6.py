#author name:Anna Tony
#date:12-11-24
#Python String Function
str_triple = '''Python is a high-level, general-purpose programming language.
Python is commonly used for developing websites and software, task automation, data analysis, and data visualisation. '''  # multi-line string
print(str_triple)
str=input("Enter a string (use both upper case and lower case) : ")
print("The length of the string is : ",len(str))
print('All the characters of the string converted to lower case : ',str.lower())
print('All the characters of the string converted to upper case : ',str.upper())
print('First character of each word to uppercase : ',str.title())
print('Swap uppercase characters to lowercase and vice versa : ',str.swapcase())
print('The first character of the string is capitalized : ',str.capitalize())
str="  Hello, World!  "
print(str.strip())
print(str.replace("World","Python"))# Replace substring with another substring
print(str.split(","))#Splits a string into a list of substrings
words = ['Hello', 'World']
print(" ".join(words)) #Joins a list of strings into a single string, separated by a specified delimiter