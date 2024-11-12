#author:Alvin Austin
#date:10-11-24
str=input("Enter a string")
vowels="AaEeIiOoUu"
vowels_count=0
for i in str:
    if i in vowels:
        vowels_count+=1
 
if vowels_count>=1:
    print("vowels present")
        


