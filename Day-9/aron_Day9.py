"""
Author:Aron Bobby Daniel
Date:18-11-2024
"""

# Defining a simple function to greet the user

def input(name,place):
    print("My name is " +name+ "! I am from " +place+ "!")
input("Austin","Kollam")


# Defining a function that adds two numbers
def multiply_numbers(a,b):
    return a*b
result=multiply_numbers(3,9)
print("The product of the numbers is",result)

# Defining a function with a default parameter
def names(name="Austin"):
    print("My name is " +name+ " ")
names("allen")
names()
