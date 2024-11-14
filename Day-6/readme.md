# Day-6
# Python String Functions with Examples

In Python, strings are sequences of characters, and Python provides a wide range of built-in string methods to manipulate and perform operations on strings. Below are common string functions along with examples.

---

## 1. **String Creation**
```python
# Create a string
s = "Hello, World!"
s_single = 'Hello, World!'  # Single quotes
s_triple = '''Hello, 
World!'''  # Triple quotes (for multi-line strings)
```
## 2.String Length (len()):
```python
# Get the length of a string
s = "Hello, World!"
print(len(s))  # Output: 13
```
## 3.String Case Conversion:
-> lower() – Converts all characters to lowercase.
```python
s = "Hello, World!"
print(s.lower())  # Output: "hello, world!"
```
-> upper() – Converts all characters to uppercase.
```python
s = "Hello, World!"
print(s.upper())  # Output: "HELLO, WORLD!"
```
-> title() – Converts the first character of each word to uppercase.
```python
s = "hello, world!"
print(s.title())  # Output: "Hello, World!"
```
->swapcase() – Swaps uppercase characters to lowercase and vice versa.
```python
s = "Hello, World!"
print(s.swapcase())  # Output: "hELLO, wORLD!"
```
->capitalize() – Capitalizes the first character of the string.
```python
s = "hello, world!"
print(s.capitalize())  # Output: "Hello, world!"
```
## 4.String Trimming:
->strip() – Removes leading and trailing whitespace.
```python
s = "  Hello, World!  "
print(s.strip())  # Output: "Hello, World!"
```
## 5.String Replacement replace():
replaces one word with another, the first word in the bracket is the word you wanna replace and the second word is the new word.
```python
# Replace substring with another substring
s = "Hello, World!"
print(s.replace("World", "Python"))  # Output: "Hello, Python!"
```
## 6.String Splitting and Joining:
-> split() – Splits a string into a list of substrings.
```python
s = "Hello, World!"
print(s.split(","))  # Output: ['Hello', ' World!']
```
-> join() – Joins a list of strings into a single string, separated by a specified delimiter.
```python
words = ['Hello', 'World']
print(" ".join(words))  # Output: "Hello World"
```
## Conclusion
These are some of the most commonly used string functions in Python. Understanding and using these functions can significantly improve your ability to manipulate and work with text in Python.



