# Day 10
# Lists

## **Task**: Understand and use lists to store multiple items in a single variable.

**Description**:
In Python, a list is a collection of ordered items, which can be of different types (integers, strings, floats, etc.). Lists are mutable, meaning their contents can be changed after creation. Lists are created using square brackets `[]`, and items are separated by commas.

## Example 1: Creating a list

```python
# Creating a list of fruits
fruits = ["apple", "banana", "cherry", "date"]

# Printing the list
print(fruits)
```
## Expected Output:
```python
['apple', 'banana', 'cherry', 'date']
```
## Key Points:
Lists are ordered collections of items.
Lists can contain elements of different data types (e.g., strings, integers, floats).
Lists are indexed, starting at 0 (zero-based indexing).

## Example 2: Accessing list elements
```python
# Accessing elements of a list by index
fruits = ["apple", "banana", "cherry", "date"]

# Accessing the first element (index 0)
print(fruits[0])  # Output: apple

# Accessing the last element (index -1)
print(fruits[-1])  # Output: date
```

## Expected Output:
```python
apple
date
```
## Example 3: Modifying a list
```python
# Modifying a list item
fruits = ["apple", "banana", "cherry", "date"]

# Changing the second item (index 1) to "blueberry"
fruits[1] = "blueberry"

# Printing the modified list
print(fruits)
```
## Expected Output:
```python
['apple', 'blueberry', 'cherry', 'date']
```
## Key Points:
You can change items in a list by accessing them using their index and assigning a new value.
Lists are mutable, which means you can modify, add, or remove elements after the list is created.

## Example 4: Adding and Removing elements
```python
# Adding an item to the end of the list
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")  # Adds "elderberry" to the end

# Removing an item from the list
fruits.remove("banana")  # Removes "banana" from the list

# Printing the modified list
print(fruits)
```
## Expected Output:
```python
['apple', 'cherry', 'date', 'elderberry']
```
## Example 5: List Slicing
```python
# Slicing a list to get a subset of items
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Getting a slice of the list from index 1 to 3 (not including index 3)
slice_of_fruits = fruits[1:3]

# Printing the sliced list
print(slice_of_fruits)
```
## Expected Output:
```python
['banana', 'cherry']
```
## Key Points:
List slicing allows you to access a specific range of elements from a list.
Syntax: list[start:end] where start is the index where the slice begins and end is where the slice ends (excluding the end index).

## Syntax for common list operations:
```python
# Creating a list
my_list = [1, 2, 3, "apple", "banana"]

# Adding an element
my_list.append("cherry")

# Removing an element
my_list.remove("banana")

# Accessing an element by index
print(my_list[2])

# Slicing a list
subset = my_list[1:3]  # Gets a subset of elements
```
### Notes:
Lists can store multiple types of data and provide a flexible way to work with collections of items.
Lists are ordered, meaning the order in which items are added is preserved.
You can add items with append(), remove items with remove(), and access elements using indices or slicing.

### Conclusion:
Lists are a fundamental data structure in Python.They
providing an efficient way to store and manipulate ordered collections of items. By using lists, you can store multiple values in a single variable and perform various operations like accessing, modifying, and slicing data.

