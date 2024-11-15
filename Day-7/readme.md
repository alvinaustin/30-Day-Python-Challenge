# Day 7
# Conditional Statements in Python
## **Task**: Learn how to use if, elif, and else statements to control the flow of your program.

**Description**:
Conditional statements allow you to make decisions in your code. You can execute certain parts of code based on whether a condition is `True` or `False`. In Python, the main conditional statements are `if`, `elif`, and `else`.

### Example:

```python
# Using if, elif, and else for decision making

# Getting user input
age = int(input("Enter your age: "))

# Using if-elif-else to check different conditions
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```
### Output
```python
Enter your age: 20
You are an adult.
```
### Explaination:
The if statement is used to check a condition. If the condition evaluates to True, the code inside the if block is executed.
The elif (short for "else if") allows you to check additional conditions if the first if condition is False. You can have multiple elif statements in a chain.
The else statement is executed if none of the previous conditions were True. You can think of it as a "catch-all" for when all other conditions fail.

### Example with multiple conditions:
``` python
# Check if a number is positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```
### Output:
```python
Enter a number: -5
The number is negative.
```
### Explanation:
The program checks if the number is greater than, less than, or equal to 0.
If the condition number > 0 is True, it prints "The number is positive".
If that condition is False, it checks if number < 0 is True and prints "The number is negative".
If neither condition is True, the else block executes, printing "The number is zero".

### Logical Operators:
You can combine multiple conditions using logical operators such as and, or, and not.
```python
# Example using logical operators
x = 10
y = 20

if x > 5 and y < 30:
    print("Both conditions are True!")
```
### Output:
```python
Both conditions are True!
```
->The and operator checks if both conditions are True. If so, the code inside the if block runs.
->Similarly, the or operator checks if either condition is True.
->The not operator is used to reverse the condition (i.e., it returns True if the condition is False).
### Conclusion:
Conditional statements are essential for controlling the flow of a program. They let you make decisions based on specific conditions and respond accordingly.
With if, elif, and else, you can handle a wide variety of scenarios in your code.



