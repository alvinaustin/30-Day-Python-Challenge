'''
author name: Annu James
date:10-11-24
'''
str=input("enter a string:")
vowels=("aeiou,AEIOU")
vowels_count=0
consonants_count=0
for char in str:
    if char in vowels:
        vowels_count+=1
    else:
        consonants_count+=1
    if vowels_count>=1:
        print("vowels are present in the string.")
    else:
        print("vowels are not present in the string.")

