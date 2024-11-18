# Day 9
# Function Defining in Python

## **Task**: Learn how to define and use functions to organize your code.

**Description**:
Functions are blocks of reusable code that perform a specific task. By defining functions, you can avoid repeating code and make your programs more organized and easier to maintain. Functions in Python are defined using the `def` keyword.

### Example 1: Defining and calling a function

```python
# Defining a simple function to greet the user
def greet(name):
    print("Hello, " + name + "! Welcome to Python.")

# Calling the function with an argument
greet("Alice")
```
## Expected Output:
```python
Hello, Alice! Welcome to Python.
```
## Key Points:
Defining a function: Use the def keyword followed by the function name and parentheses.
Syntax: def function_name(parameters):
Parameters: Variables passed to the function inside the parentheses. They allow you to provide input to the function.
Return statement: Functions can return a value using the return keyword. If no return is specified, the function returns None by default.

## Example 2: Function with a return value
```python
# Defining a function that adds two numbers
def add_numbers(a, b):
    return a + b

# Calling the function and printing the result
result = add_numbers(3, 5)
print("The sum is:", result)
```
## Expected Output:
```python
The sum is: 8
```
## Example 3: Function with default parameter values
```python
# Defining a function with a default parameter
def greet(name="Guest"):
    print("Hello, " + name + "! Welcome to Python.")

# Calling the function with and without an argument
greet("Bob")
greet()  # This will use the default value for 'name'
```
## Expected Output:
```python
Hello, Bob! Welcome to Python.
Hello, Guest! Welcome to Python.
```
## Key Points:
Functions can take multiple parameters or just one. You can also set default values for parameters, which will be used if no argument is provided when the function is called.
Returning values: You can return values from a function, allowing the function to send data back to the caller.
Scope: Variables defined inside a function are local to that function. They are not accessible outside of it.

## Syntax:
```python
def function_name(parameter1, parameter2, ...):
    # Code to execute
    return value  # Optional
```
## Notes:
Functions help make your code more modular and easier to understand.
You can call a function as many times as you like, which allows for reuse of code.
Functions can take different types of parameters (integers, strings, lists, etc.) and return any type of value (or nothing at all).

## Conclusion:
Functions are an essential part of writing clean, organized, and reusable code. By using functions, you can break your program into smaller, manageable pieces and avoid redundancy. 
Functions also make your code more readable and maintainable.


