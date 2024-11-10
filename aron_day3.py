"""
Author:Aron Bobby Daniel
Date:10-11-2024
"""


str=(input("Enter a String:"))
vowels=("aeiouAeiou")
vowels_count=0
consonants=0
for char in str:
    if char in vowels:
        vowels_count+=1
    else:
        consonants+=1
if vowels_count>=1:
    print("Vowels are present in the string"',',"Number of vowels=",(vowels_count))
else:
    print("There is no vowels but has consonants",','"Number of consonants=",consonants)

