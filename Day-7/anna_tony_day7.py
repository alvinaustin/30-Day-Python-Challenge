#author name:Anna Tony
#date:15-11-24
#Conditional Statements in Python
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if (side1==side2 and side2==side3):
    print('It is an Equilateral Triangle')
elif(side1 == side2 or side2 == side3 or side1 == side3):
    print("It is an Isosceles Triangle")
else:
    print("It is a Scalene Triangle")