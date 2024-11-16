import math

num=int(input("Enter  a Number"))
num1=int(input("Enter Another Number:"))

sqrt=math.sqrt(num)
print(f"Square Root of {num} is {sqrt}")

power=math.pow(num,num1)
print(f"Power of {num} raised to {num1} is {power}")

floor=math.floor(num)
print(f"Largest integer less than or equal to {num} is {floor}")

ceil=math.ceil(num)
print(f"Largest integer greater than or equal to {num} is {ceil}")

fact=math.factorial(num)
print(f"The factorial of {num} is {fact}")


#constants in math module
print("The Value of pi=",math.pi)
print("The value of e=",math.e)