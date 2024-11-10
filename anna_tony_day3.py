# author Anna Tony
# date 10-11-2024
string_input=input('Enter the string : ')
vowel="aeiouAEIOU"
vowel_count=0
for char in string_input:
    if char in vowel:
        vowel_count+=1
if vowel_count>=1:
    print('There is a vowel present in the given string.')
else:
    print('There is no vowel present in the given string.')