""""
 Author: anna mariya shibu
 created on :10/11/24
 
 """



string_input=input("Enter a string: ")
vowels="a","e","i","o","u","A","E","I","O","U"
vowel_count=0
for char in string_input:
   if char in vowels:
       vowel_count+=1
   if vowel_count>=1:
       print("there is a vowel in the string")
else:
     print("there is not a vowel in the string")









