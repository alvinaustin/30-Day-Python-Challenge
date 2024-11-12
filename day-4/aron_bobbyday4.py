

number1=int(input("Enter First Number:"))
number2=int(input("Enter Second Number:"))


user=0

print("Select Operation")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Floor division")
print("6.Modulas")
print("7.Exponential")


select=int(input("Select operations from 1,2,3,4,5,6,7:"))
if select==1:
    sum= number1+number2
    print("The sum of the digits is",sum)
elif select==2:
    diff=number1-number2
    print("The difference of the digits is",diff)
elif select==3:
    product=number1*number2
    print("The product of the digits is",product)
elif select==4:
    division=number1/number2
    print("The answer is",division)
elif select==5:
    floor=number1//number2
    print("The answer is",floor)
elif select==6:
    mod=number1%number2
    print("The answer is ",mod)
elif select==7:
    exp=number1**number2
    print("The answer is",exp)

