num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
print('''Select Operation:->
1.Addition
2.Substraction
3.Multiplication
4.Division
5.Floor division
6.Modulus
7.Exponential''')
choice=int(input("Select operations from 1,2,3,4,5,6,7:"))
if choice==1:
    sum= num1+num2
    print(f"The sum of the digits {num1} and {num2} is {sum}")
elif choice==2:
    diff=num1-num2
    print(f"The difference of the digits {num1} and {num2} is {diff}")
elif choice==3:
    product=num1*num2
    print(f"The product of the digits {num1} and {num2} is {product}")
elif choice==4:
    division=num1/num2
    print(f"The Solution of dividing {num1} by {num2} is {division}")
elif choice==5:
    floor=num1//num2
    print(f"The Floor division of {num1} by {num2} is {floor}")
elif choice==6:
    mod=num1%num2
    print(f"The remainder when we divide {num1} by {num2} is {mod}")
elif choice==7:
    exp=num1**num2
    print(f"{num1} raised to the power of {num2} is {exp}")
