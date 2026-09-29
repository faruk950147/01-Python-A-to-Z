"""
# Python Intermediate — Interview Questions & Answers

# 01. Built-in Data Structures

Python-এর প্রধান built-in data structures:

1. List
2. Tuple
3. Set
4. Dictionary

---

## 1. List

### Q1. What is a List?

**Answer:**
A list is an ordered, mutable collection that can store multiple values of different data types.

```python
numbers = [10, 20, 30, 40]
```

### Important Properties

* Ordered
* Mutable
* Allows duplicate values
* Supports indexing
* Can contain different data types

```python
data = [10, "Python", 3.14, True]
```

### Common List Methods

```python
append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()
```

---

## 2. Tuple

### Q2. What is a Tuple?

**Answer:**
A tuple is an ordered and immutable collection of values.

```python
numbers = (10, 20, 30)
```

### List vs Tuple

| List                    | Tuple                         |
| ----------------------- | ----------------------------- |
| Mutable                 | Immutable                     |
| `[]`                    | `()`                          |
| Generally more flexible | Generally used for fixed data |
| More methods            | Fewer methods                 |

---

## 3. Set

### Q3. What is a Set?

**Answer:**
A set is an unordered collection of unique elements.

```python
numbers = {1, 2, 3, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

### Important Properties

* Unique elements
* Mutable
* No duplicate elements
* Does not support indexing

Common methods:

```python
add()
remove()
discard()
pop()
union()
intersection()
difference()
```

---

## 4. Dictionary

### Q4. What is a Dictionary?

**Answer:**
A dictionary is a mutable collection of key-value pairs.

```python
student = {
    "name": "Faruk",
    "age": 25,
    "department": "CSE"
}
```

Access:

```python
print(student["name"])
```

### Important Properties

* Key-value based
* Mutable
* Keys must be hashable
* Keys must be unique

Common methods:

```python
keys()
values()
items()
get()
update()
pop()
popitem()
setdefault()
```

---

## Q5. List vs Tuple vs Set vs Dictionary

| Data Structure | Ordered | Mutable | Duplicate | Access      |
| -------------- | ------- | ------- | --------- | ----------- |
| List           | Yes     | Yes     | Yes       | Index       |
| Tuple          | Yes     | No      | Yes       | Index       |
| Set            | No      | Yes     | No        | No indexing |
| Dictionary     | Yes*    | Yes     | Keys: No  | Key         |

`*` Modern Python dictionaries preserve insertion order.

---

# 02. Functions

## Q1. What is a Function?

**Answer:**
A function is a reusable block of code designed to perform a specific task.

Example:

```python
def greet():
    print("Hello")

greet()
```

---

# Custom Function

### Q2. What is a Custom Function?

**Answer:**
A function created by the programmer to perform a specific task is called a custom/user-defined function.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

---

# Parameters and Arguments

### Q3. What is a Parameter?

**Answer:**
A parameter is a variable defined in a function declaration.

```python
def add(a, b):
    return a + b
```

Here `a` and `b` are parameters.

### Q4. What is an Argument?

**Answer:**
An argument is the actual value passed to a function when calling it.

```python
add(10, 20)
```

Here `10` and `20` are arguments.

---

# Types of Arguments

## 1. Positional Arguments

```python
def greet(name, age):
    print(name, age)

greet("Faruk", 25)
```

Arguments are matched according to their position.

---

## 2. Keyword Arguments

```python
def greet(name, age):
    print(name, age)

greet(age=25, name="Faruk")
```

---

## 3. Default Arguments

```python
def greet(name="User"):
    print("Hello", name)

greet()
```

Output:

```text
Hello User
```

---

## 4. Variable-Length Arguments

### `*args`

Used to receive multiple positional arguments.

```python
def add(*args):
    return sum(args)

print(add(10, 20, 30))
```

### `**kwargs`

Used to receive multiple keyword arguments.

```python
def display(**kwargs):
    print(kwargs)

display(name="Faruk", age=25)
```

---

# Return Statement

### Q5. What is `return`?

**Answer:**
`return` sends a value back from a function and terminates that function's execution.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

### Q6. What happens if a function has no `return` statement?

**Answer:**
It implicitly returns `None`.

```python
def test():
    print("Hello")

result = test()

print(result)
```

Output:

```text
Hello
None
```

---

# Callback Function

### Q7. What is a Callback Function?

**Answer:**
A callback is a function that is passed to another function as an argument and is called by that function.

```python
def greet(name):
    return f"Hello {name}"

def process(callback):
    print(callback("Faruk"))

process(greet)
```

---

# Higher-Order Function

### Q8. What is a Higher-Order Function?

**Answer:**
A higher-order function is a function that takes another function as an argument, returns a function, or both.

Example:

```python
def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

print(apply_function(square, 5))
```

Output:

```text
25
```

---

# Lambda Function

### Q9. What is a Lambda Function?

**Answer:**
A lambda function is a small anonymous function defined using the `lambda` keyword.

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

### Lambda with `sorted()`

```python
students = [
    ("Faruk", 80),
    ("Ahmed", 90),
    ("Karim", 70)
]

students.sort(key=lambda x: x[1])

print(students)
```

---

# IIFE

### Q10. What is IIFE?

**Answer:**
IIFE means **Immediately Invoked Function Expression**.

Python does not have a special IIFE syntax like JavaScript, but a function can be defined and immediately called.

Example:

```python
(lambda: print("Hello"))()
```

Output:

```text
Hello
```

---

# Decorators

### Q11. What is a Decorator?

**Answer:**
A decorator is a function that modifies or extends the behavior of another function without changing its source code.

Example:

```python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello")

greet()
```

Output:

```text
Before function
Hello
After function
```

### Q12. What does `@decorator` mean?

```python
@decorator
def greet():
    pass
```

It is approximately equivalent to:

```python
def greet():
    pass

greet = decorator(greet)
```

---

# Generator

### Q13. What is a Generator?

**Answer:**
A generator is a special type of iterator that produces values lazily using the `yield` statement.

```python
def numbers():
    yield 1
    yield 2
    yield 3

for number in numbers():
    print(number)
```

### Q14. What is `yield`?

**Answer:**
`yield` produces a value from a generator and pauses its execution. The function can continue from that point when the next value is requested.

### Q15. Generator vs Normal Function

| Normal Function                           | Generator                            |
| ----------------------------------------- | ------------------------------------ |
| Uses `return`                             | Uses `yield`                         |
| Returns result                            | Produces values one at a time        |
| Usually executes to return                | Execution can pause/resume           |
| Can require more memory for large results | Memory efficient for large sequences |

---

# Iterator

### Q16. What is an Iterator?

**Answer:**
An iterator is an object that implements the iterator protocol using `__iter__()` and `__next__()`.

Example:

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
1
2
3
```

### Q17. What happens when there are no more elements?

**Answer:**
`next()` raises `StopIteration`.

---

# Iterable vs Iterator

### Iterable

An iterable is an object that can return an iterator.

Examples:

```python
list
tuple
string
set
dictionary
```

### Iterator

An iterator keeps track of the current position and provides values using `next()`.

---

# Recursion

### Q18. What is Recursion?

**Answer:**
Recursion is a technique where a function calls itself to solve a problem.

Example:

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

### Q19. What is a Base Case?

**Answer:**
The base case is the condition that stops recursive calls.

```python
if n == 0:
    return 1
```

Without an appropriate base case, recursion may continue until Python raises a `RecursionError`.

---

# Scope and Closure

## Scope

### Q20. What is Scope?

**Answer:**
Scope determines where a variable can be accessed in a program.

Python follows the **LEGB** rule:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

---

## Local Scope

```python
def test():
    x = 10
    print(x)

test()
```

`x` is local to the function.

---

## Global Scope

```python
x = 10

def test():
    print(x)

test()
```

Here `x` is a global variable.

---

## `global` Keyword

Used when you want to modify a global variable inside a function.

```python
count = 0

def increment():
    global count
    count += 1

increment()

print(count)
```

Output:

```text
1
```

---

# Closure

### Q21. What is a Closure?

**Answer:**
A closure occurs when an inner function remembers and accesses variables from its enclosing function even after the enclosing function has finished execution.

Example:

```python
def outer(message):

    def inner():
        print(message)

    return inner


func = outer("Hello Python")

func()
```

Output:

```text
Hello Python
```

Here `inner()` remembers the `message` variable from `outer()`.

### Q22. Why are closures useful?

Closures can be useful for:

* Data encapsulation
* Maintaining state
* Creating decorators
* Creating function factories

---

# 03. Modules and Packages

## Module

### Q1. What is a Module?

**Answer:**
A module is a Python file containing Python code such as functions, classes, and variables.

Example:

```text
math_utils.py
```

```python
def add(a, b):
    return a + b
```

Import:

```python
import math_utils

print(math_utils.add(10, 20))
```

---

## Package

### Q2. What is a Package?

**Answer:**
A package is a way of organizing related Python modules into a directory structure.

Example:

```text
myproject/
│
├── package/
│   ├── __init__.py
│   ├── math.py
│   └── string.py
```

---

## Module vs Package

| Module                   | Package                     |
| ------------------------ | --------------------------- |
| Usually a `.py` file     | Directory/package structure |
| Contains Python code     | Organizes multiple modules  |
| Example: `math_utils.py` | Example: `utils/`           |

---

# Import

### Q3. What are common ways to import a module?

```python
import math
```

```python
from math import sqrt
```

```python
import math as m
```

```python
from math import *
```

Using `from module import *` is generally discouraged because it can make names unclear and cause namespace conflicts.

---

# `__name__ == "__main__"`

### Q4. What is `if __name__ == "__main__"`?

**Answer:**
It checks whether the Python file is being run directly rather than imported as a module.

```python
def main():
    print("Program started")

if __name__ == "__main__":
    main()
```

---

# 04. Exception Handling

### Q1. What is an Exception?

**Answer:**
An exception is an error condition that occurs during program execution and can be handled by the program.

Example:

```python
x = 10 / 0
```

This raises:

```text
ZeroDivisionError
```

---

# try-except

### Q2. What is `try-except`?

**Answer:**
`try-except` is used to handle exceptions without abruptly terminating the program.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# else

### Q3. What is `else` in exception handling?

**Answer:**
The `else` block executes when no exception occurs in the `try` block.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print(result)
```

---

# finally

### Q4. What is `finally`?

**Answer:**
The `finally` block executes whether an exception occurs or not.

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")
```

---

# raise

### Q5. What is `raise`?

**Answer:**
`raise` is used to explicitly raise an exception.

```python
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

# Custom Exception

### Q6. How do you create a custom exception?

```python
class InvalidAgeError(Exception):
    pass


age = -1

if age < 0:
    raise InvalidAgeError("Invalid age")
```

---

# Common Exceptions

```text
ValueError
TypeError
IndexError
KeyError
NameError
ZeroDivisionError
FileNotFoundError
AttributeError
ImportError
ModuleNotFoundError
```

---

# Exception Handling Structure

```python
try:
    # risky code

except SomeException:
    # handle exception

else:
    # runs if no exception

finally:
    # always executes
```

---

# 05. File Handling

### Q1. What is File Handling?

**Answer:**
File handling is the process of creating, reading, writing, updating, and managing files using Python.

---

# Opening a File

Python uses `open()` to open a file.

```python
file = open("data.txt", "r")
```

### Common Modes

| Mode | Meaning |
| ---- | ------- |
| `r`  | Read    |
| `w`  | Write   |
| `a`  | Append  |
| `x`  | Create  |
| `b`  | Binary  |
| `t`  | Text    |

---

# Reading a File

### `read()`

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### `readline()`

Reads one line.

```python
with open("data.txt", "r") as file:
    print(file.readline())
```

### `readlines()`

Reads lines and returns them as a list.

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
```

---

# Writing to a File

```python
with open("data.txt", "w") as file:
    file.write("Hello Python")
```

`w` mode creates a file if it does not exist and overwrites existing content.

---

# Append

```python
with open("data.txt", "a") as file:
    file.write("\nHello again")
```

`a` mode adds content at the end of the file.

---

# `with` Statement

### Q2. Why do we use `with open()`?

**Answer:**
The `with` statement automatically manages the file resource and closes the file when the block is exited.

Example:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

This is preferred over manually doing:

```python
file = open("data.txt", "r")

data = file.read()

file.close()
```

---

# Q3. What is `close()`?

**Answer:**
`close()` closes an opened file and releases the associated resource.

```python
file = open("data.txt", "r")

data = file.read()

file.close()
```

---

# File Handling with Exception Handling

```python
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File does not exist")
```

---

# 🔥 Most Important Interview Questions

## Data Structures

1. What are Python's built-in data structures?
2. What is a list?
3. What is a tuple?
4. What is a set?
5. What is a dictionary?
6. List vs Tuple?
7. List vs Set?
8. Tuple vs Set?
9. Why are dictionary keys unique?
10. Can a list contain different data types?

## Functions

11. What is a function?
12. What is a custom/user-defined function?
13. Parameter vs Argument?
14. What are positional arguments?
15. What are keyword arguments?
16. What are default arguments?
17. What are `*args` and `**kwargs`?
18. What is `return`?
19. What happens if a function has no return statement?
20. What is a callback function?
21. What is a higher-order function?
22. What is a lambda function?
23. What is IIFE?
24. What is a decorator?
25. What does `@decorator` mean?
26. What is a generator?
27. What is `yield`?
28. Generator vs normal function?
29. What is an iterator?
30. Iterable vs Iterator?
31. What is recursion?
32. What is a base case?

## Scope & Closure

33. What is scope?
34. What is LEGB?
35. What is local scope?
36. What is global scope?
37. What does the `global` keyword do?
38. What is a closure?
39. Why are closures useful?

## Modules & Packages

40. What is a module?
41. What is a package?
42. Module vs Package?
43. How do you import a module?
44. What is `from module import ...`?
45. What is `import ... as ...`?
46. What is `__name__ == "__main__"`?

## Exception Handling

47. What is an exception?
48. What is `try-except`?
49. What is `else` in exception handling?
50. What is `finally`?
51. What is `raise`?
52. What is a custom exception?
53. Name some common Python exceptions.
54. What is the difference between `ValueError` and `TypeError`?

## File Handling

55. What is file handling?
56. What does `open()` do?
57. What are file modes?
58. Difference between `r`, `w`, and `a`?
59. Difference between `read()`, `readline()`, and `readlines()`?
60. Why should we use `with open()`?
61. What does `close()` do?
62. How do you handle `FileNotFoundError`?

# ⭐ Quick Revision

```text
Built-in Data Structures
    ↓
List → Mutable + Ordered
Tuple → Immutable + Ordered
Set → Unique Elements
Dictionary → Key-Value Pairs

Functions
    ↓
Custom Function
    ↓
Arguments / Parameters
    ↓
*args / **kwargs
    ↓
Lambda
    ↓
Callback
    ↓
Higher-Order Function
    ↓
Decorator
    ↓
Generator / yield
    ↓
Iterator
    ↓
Recursion
    ↓
Scope / LEGB
    ↓
Closure

Modules & Packages
    ↓
Module
    ↓
Package
    ↓
import
    ↓
__name__ == "__main__"

Exception Handling
    ↓
try
    ↓
except
    ↓
else
    ↓
finally
    ↓
raise
    ↓
Custom Exception

File Handling
    ↓
open()
    ↓
read()
    ↓
write()
    ↓
append()
    ↓
with open()
    ↓
close()
```
  
"""