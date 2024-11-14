"""
Author:Aron Bobby Daniel
Date:14-11-2024
"""


#Double Quotation Mark
string_object="Hello World"
print(string_object)
#single quotation mark
str_1='hello python'
print(str_1)
#triple quotation for multiple line string
"""
hello world
this is a sample text
python
"""

# Get the length of a string

strlen="Alvin Joseph Austin"
print(len(strlen))

#String Case Conversion

st="HELLO PYTHON" #lower() – Converts all characters to lowercase.
print(st.lower())

st1="hello python" #upper() – Converts all characters to uppercase.
print(st1.upper())

str2="hello world" #title() – Converts the first character of each word to uppercase.
print(str2.title())

str3="IntroductioN tO PythoN" #swapcase() – Swaps uppercase characters to lowercase and vice versa.
print(str3.swapcase())

str4="alvin joseph austin" #capitalize() – Capitalizes the first character of the string.
print(str4.capitalize())
 #String Trimming
#strip() – Removes leading and trailing whitespace.

str5=("  hello  world!   " )
print(str5.strip())

#String Replacement replace():

str6="Hello,i am python"
print(str6.replace("i am python","world"))

str7="hello,guys.." #split() – Splits a string into a list of substrings.
print(str7.split(","))

str8=["Apple!,Orange!"]  #join() – Joins a list of strings into a single string, separated by a specified delimiter
print(" ".join(str8))
