"""
Author:Aron Bobby Daniel
Date:15-11-2024
Python Programme of if,else if,else and conditional statements
"""

#Offer criteria for big billion day sale

amount=int(input("Enter Total Purchase Amount:"))
if amount <1000:
    print("15% Discount applied to your order")
elif amount>=1000 and amount<=5000:
    print("25% Discount applied to your order")
else:
    print("30% Discount applied to your order")

#Conditional Statements in python

num1=60
num2=93

if num1<num2 and num2>num1:
    print("Both Conditions are true",",60<93 and 93>60")
