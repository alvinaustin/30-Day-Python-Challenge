# Day 11 
# Tuples

## Overview

Today, we will learn about:

- **What is a Tuple?**: Basic definition and characteristics.
- **Creating and Accessing Tuples**: How to create and access elements.
- **Tuple Operations**: Common operations like slicing, concatenation, and repetition.
- **Immutability**: Why tuples are immutable.
- **Tuple Methods**: Useful methods you can use with tuples.

---

## Topics

## 1. What is a Tuple?

A tuple is an ordered collection of elements, similar to a list, but **immutable** (cannot be modified after creation). Tuples are defined by enclosing elements in parentheses `()`.

#### Example:

```python
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4
```
## 2. Creating and Accessing Tuples
Tuples can contain any type of object, and they are accessed using indices, just like lists.

#### Creating a Tuple:
```python
# A tuple with integers
numbers = (1, 2, 3)

# A tuple with mixed data types
person = ("Alice", 30, "Engineer")

# A tuple with a single element (comma is important)
single_element_tuple = (5,)
```
## Accessing Elements:
You can access individual elements of a tuple by indexing (starting at 0) or by slicing.
```python
# Accessing individual elements
print(person[0])  # Output: Alice
print(person[1])  # Output: 30

# Slicing a tuple
print(person[1:])  # Output: (30, 'Engineer')
```
## 3. Tuple Operations
Tuples support several operations such as slicing, concatenation, and repetition.

Slicing:
You can slice a tuple to get a subset of elements.
```python
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])  # Output: (2, 3, 4)
```
Concatenation:
You can concatenate two tuples using the + operator.
```python
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4)
```
Repetition:
You can repeat a tuple multiple times using the * operator.
```python
numbers = (1, 2)
repeated = numbers * 3
print(repeated)  # Output: (1, 2, 1, 2, 1, 2)
```
4. Immutability of Tuples
Unlike lists, tuples are immutable, meaning their elements cannot be changed after the tuple is created.

Example of Immutability:
```python
my_tuple = (1, 2, 3)
# This will raise an error because tuples cannot be changed
my_tuple[1] = 10  # TypeError: 'tuple' object does not support item assignment
```
However, you can create a new tuple if you want to change its contents.
```python
# Create a new tuple by concatenating existing tuples
new_tuple = my_tuple[:2] + (10,) + my_tuple[2:]
print(new_tuple)  # Output: (1, 2, 10, 3)
```
5. Tuple Methods
Tuples have a few built-in methods that can be useful for certain operations.
-> count()
Counts how many times an element appears in the tuple.
```python
my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3
```
-> index()
Returns the index of the first occurrence of an element.
```python
my_tuple = (1, 2, 3, 4)
print(my_tuple.index(3))  # Output: 2
```
### Exercises
Create a Tuple: Create a tuple that contains the names of three cities you’d like to visit. Print the second city from the tuple.
Tuple Concatenation: Create two tuples with your favorite fruits and favorite vegetables, then concatenate them into a new tuple.
Immutability: Try to modify an element in a tuple and catch the error. Then create a new tuple with the modified values.
Tuple Methods: Create a tuple and use the count() method to find how many times a specific number appears in it. Then, use index() to find the index of an element.

### Summary
Today, you learned how to:
Create and access elements in a tuple.
Perform common operations like slicing, concatenation, and repetition.
Understand the immutability of tuples and how it differs from lists.
Use tuple methods such as count() and index() to work with elements.



