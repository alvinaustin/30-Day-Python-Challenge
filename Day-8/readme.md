# Day-8
# Loops in Python (For and While)

## **Task**: Learn how to use loops to repeat actions in your code.

**Description**:
Loops are used to execute a block of code multiple times. There are two main types of loops in Python: `for` and `while`. Loops are helpful when you need to perform repetitive tasks or iterate over a collection of items.

## Example 1: Using a "for" loop
```python
# Using a for loop to print numbers from 1 to 5
for i in range(1, 6):
    print(i)
```
### Expected Output:
```python
1
2
3
4
5
```
## Example 2: Using a "while" loop
```python
# Using a while loop to print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1  # Increment i by 1
```
### Expected Output:
```python
1
2
3
4
5
```
### Key Points:
->for loop: Iterates over a sequence (such as a list, tuple, string, or a range of numbers). It's typically used when the number of iterations is known.
  
  Syntax: for item in sequence:

->while loop: Repeats the block of code as long as a condition is true. It's typically used when the number of iterations is unknown and depends on a condition.
  
  Syntax: while condition:
### Syntax:
```python
# for loop example
for i in range(start, stop, step):
    # Code to execute for each iteration

# while loop example
while condition:
    # Code to execute as long as the condition is true
```
### Notes:
The range() function generates a sequence of numbers, which is commonly used with for loops to iterate a specific number of times.
Make sure that the condition in a while loop eventually becomes False, or the loop will run forever (infinite loop).
You can use break to exit a loop early, and continue to skip to the next iteration of the loop.

## Example 3: Using break and continue
```python
# Example of using break and continue
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop when i equals 5
    if i == 3:
        continue  # Skip the iteration when i equals 3
    print(i)
```
### Expected Output:
```python
1
2
4
```
## Conclusion:
Loops are powerful tools for automating repetitive tasks and iterating over data structures. By using for and while loops, you can efficiently handle a wide range of programming tasks.


