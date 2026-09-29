'''
1. What is Programming Language?
     A Programming Language is a formal language with a set of rules, syntax, and keywords that allows programmers to write instructions for a computer to perform specific tasks.

     Alternative Simple Definition:

     A Programming Language is a set of rules and syntax that allows humans to communicate instructions to computers.

     Examples
     Python
     C
     C++
     Java
     JavaScript
     Go
     Rust

2. What is Machine Language?
     Machine Language is the lowest-level programming language that consists only of 0s and 1s (binary digits). It is directly understood and executed by the CPU.

     Example
     10101100
     11001010
     00011111
     Advantages
     Fastest execution
     No translator required
     Disadvantages
     Very difficult to write
     Very difficult to debug
     Hardware dependent

3. What is Binary Number System?
     Binary is a number system that uses only two digits:

     0
     1
     Base
     Base = 2
     Example
     Binary = 1010
     Decimal = 10

4. What is Decimal Number System?
     Decimal is the number system we use every day.

     Digits
     0-9
     Base
     Base = 10

     Example
     254

5. What is Octal Number System?
     Octal uses digits from

     0–7
     Base
     Base = 8

     Example
     725

6. What is Hexadecimal Number System?
     Hexadecimal uses

     0–9
     A–F
     Base
     Base = 16

     Example
     3AF

7. What is Assembly Language?
     Assembly Language is a low-level programming language that uses mnemonic instructions instead of binary.

     Example
     MOV AX,5
     ADD AX,2
     MOV
     ADD
     SUB
     JMP

8. What is High-Level Programming Language?
     Assembly Language is a low-level programming language that uses mnemonic instructions instead of binary.

     Example
     MOV AX,5
     ADD AX,2
     MOV
     ADD
     SUB
     JMP

9. What is High-Level Programming Language?
     A High-Level Programming Language is designed to be easy for humans to read, write, and understand.

     Examples
     Python
     Java
     C
     C++
     JavaScript
     PHP
     print("Hello World")

10. What is Source Code?
     Source Code is the original code written by a programmer using a programming language.

     Example
     a = 10
     b = 20
     print(a+b)

     10. What is Compiler?
     Definition

     A Compiler is a program that translates the entire source code into machine code before execution.

     Features
     Entire program at once
     Generates executable file
     Faster execution
     Errors shown after compilation
     Examples
     GCC
     Clang
     MSVC

11. What is Interpreter?
     An Interpreter translates and executes source code one line at a time.

     Interpreter Source Code-কে এক লাইন করে অনুবাদ এবং Execute করে।

     Features
     Line-by-line execution
     No executable file
     Easier debugging
     Slower execution
     Examples
     Python
     JavaScript
     Ruby

12. Compiler vs Interpreter
     Compiler	Interpreter
     Translates entire program	Translates line by line
     Faster execution	Slower execution
     Creates executable file	No executable file
     Errors after compilation	Errors immediately
     Example: C, C++	Example: Python, JavaScript

13. What is Object Code?
     Object Code is the machine-level code produced by a compiler or assembler before final linking.

     Usually
     main.o
     main.obj

14. What is Machine Code?
     Machine Code is the final binary code that the CPU directly executes.

     Example
     10110011
     00101010
     11000001

14. Program Translation Process
     Programmer
          │
          ▼
     Source Code
          │
          ▼
     Compiler / Interpreter
          │
          ▼
     Object Code
          │
          ▼
     Linker
          │
          ▼
     Executable File
          │
          ▼
     Machine Code
          │
          ▼
     CPU Executes
     
     
# Python Basic Concepts — Interview Questions & Answers

## 01. Flowchart

### Q1. What is a Flowchart?

**Answer:**
A flowchart is a graphical representation of an algorithm or process using standard symbols.

### Q2. Why is a flowchart used?

**Answer:**

* To understand program logic
* To analyze a problem
* To design an algorithm
* To identify logical errors
* To document a process

### Q3. What are the common flowchart symbols?

| Symbol        | Purpose        |
| ------------- | -------------- |
| Oval          | Start / End    |
| Rectangle     | Process        |
| Diamond       | Decision       |
| Parallelogram | Input / Output |
| Arrow         | Flow direction |

### Q4. What is the difference between an algorithm and a flowchart?

**Answer:**
An algorithm represents the solution in step-by-step instructions, while a flowchart represents the same logic graphically.

---

# 02. Hello World

### Q1. How do you print "Hello World" in Python?

```python
print("Hello World")
```

### Q2. What is `print()`?

**Answer:**
`print()` is a built-in Python function used to display output on the screen.

### Q3. Is `print` a keyword?

**Answer:**
No. `print` is a built-in function, not a keyword.

---

# 03. Input and Output

### Q1. How do you take input from the user in Python?

```python
name = input("Enter your name: ")
```

### Q2. What does `input()` return?

**Answer:**
The `input()` function always returns a string (`str`).

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

### Q3. How do you take an integer input?

```python
age = int(input("Enter your age: "))
```

### Q4. How do you display output in Python?

```python
print("Hello")
```

---

# 04. Literals

### Q1. What is a Literal?

**Answer:**
A literal is a fixed value written directly in a Python program.

Examples:

```python
10
3.14
"Python"
True
False
None
3 + 4j
```

### Q2. What are the common types of literals?

**Answer:**

1. Integer literal
2. Float literal
3. String literal
4. Boolean literal
5. None literal
6. Complex literal

### Examples:

```python
10          # Integer
3.14        # Float
"Python"    # String
True        # Boolean
None        # None
3 + 4j      # Complex
```

### Q3. Is `10` the same as `"10"`?

**Answer:**
No.

```python
10      # int
"10"    # str
```

---

# 05. Operators

### Q1. What is an Operator?

**Answer:**
An operator is a symbol or keyword used to perform an operation on values or variables.

## Arithmetic Operators

```python
+
-
*
/
//
%
**
```

Example:

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### Q2. What is the difference between `/` and `//`?

**Answer:**

`/` performs normal division and returns a float.

```python
10 / 3
# 3.3333333333333335
```

`//` performs floor division.

```python
10 // 3
# 3
```

### Q3. What does `%` do?

**Answer:**
The `%` operator returns the remainder.

```python
10 % 3
# 1
```

### Q4. What does `**` do?

**Answer:**
It performs exponentiation.

```python
2 ** 3
# 8
```

---

## Comparison Operators

```python
==
!=
>
<
>=
<=
```

Example:

```python
10 > 5
# True
```

---

## Logical Operators

```python
and
or
not
```

Example:

```python
age = 25

print(age > 18 and age < 60)
# True
```

---

## Assignment Operators

```python
=
+=
-=
*=
/=
%=
**=
//=
```

Example:

```python
x = 10
x += 5

print(x)
# 15
```

---

## Membership Operators

```python
in
not in
```

Example:

```python
languages = ["Python", "Java", "C"]

print("Python" in languages)
# True
```

---

## Identity Operators

```python
is
is not
```

Example:

```python
a = [1, 2, 3]
b = a

print(a is b)
# True
```

### Q5. What is the difference between `==` and `is`?

**Answer:**

`==` checks whether two objects have equal values.

`is` checks whether two variables refer to the same object.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
```

---

# 06. Python Keywords

### Q1. What is a Keyword?

**Answer:**
A keyword is a reserved word in Python that has a predefined meaning.

Examples:

```python
if
else
elif
for
while
def
class
return
import
from
try
except
finally
True
False
None
and
or
not
in
is
```

### Q2. How can you see Python keywords?

```python
import keyword

print(keyword.kwlist)
```

### Q3. Can we use a keyword as a variable name?

**Answer:**
No.

Invalid:

```python
class = "Python"
```

### Q4. Is `print` a keyword?

**Answer:**
No. `print()` is a built-in function.

---

# 07. Swap

### Q1. What is swapping?

**Answer:**
Swapping means exchanging the values of two variables.

### Q2. How do you swap two variables using a temporary variable?

```python
a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)
```

Output:

```text
20 10
```

### Q3. How do you swap two variables in Python without a third variable?

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

Output:

```text
20 10
```

---

# 08. Types of Errors

### Q1. What are the common types of errors in Python?

**Answer:**

1. Syntax Error
2. Runtime Error / Exception
3. Logical Error

---

## Syntax Error

### Q2. What is a Syntax Error?

**Answer:**
A syntax error occurs when Python code does not follow the correct syntax.

Example:

```python
if x > 10
    print(x)
```

The colon `:` is missing.

---

## Runtime Error / Exception

### Q3. What is a Runtime Error?

**Answer:**
A runtime error occurs while the program is executing.

Example:

```python
a = 10
b = 0

print(a / b)
```

This produces:

```text
ZeroDivisionError
```

Another example:

```python
print(10 + "5")
```

This produces:

```text
TypeError
```

---

## Logical Error

### Q4. What is a Logical Error?

**Answer:**
A logical error occurs when the program runs successfully but produces an incorrect result.

Example:

```python
a = 10
b = 20

result = a - b
```

If the expected operation was addition, the program runs but gives the wrong result.

### Q5. What is the difference between Syntax Error and Logical Error?

**Answer:**

**Syntax Error:** The code violates Python syntax and cannot execute normally.

**Logical Error:** The code executes but produces an incorrect result.

---

# 09. Type Casting

### Q1. What is Type Casting?

**Answer:**
Type casting is the process of converting a value from one data type to another.

Common functions:

```python
int()
float()
str()
bool()
list()
tuple()
set()
```

### Q2. How do you convert a string to an integer?

```python
x = "100"

y = int(x)

print(y)
print(type(y))
```

### Q3. How do you convert an integer to a string?

```python
age = 25

age = str(age)

print(type(age))
```

### Q4. How do you convert an integer to a float?

```python
x = 10

y = float(x)

print(y)
# 10.0
```

### Q5. What is Explicit Type Conversion?

**Answer:**
When the programmer manually converts one data type to another, it is called explicit type conversion.

Example:

```python
x = "100"

y = int(x)
```

### Q6. What is Implicit Type Conversion?

**Answer:**
When Python automatically converts a value from one compatible type to another, it is called implicit type conversion.

Example:

```python
x = 10
y = 2.5

result = x + y

print(type(result))
# <class 'float'>
```

---

# 10. Variable

### Q1. What is a Variable?

**Answer:**
A variable is a name that refers to an object/value in Python.

Example:

```python
name = "Faruk"
age = 25
```

### Q2. Is Python statically typed or dynamically typed?

**Answer:**
Python is a dynamically typed language.

Example:

```python
x = 10

x = "Python"
```

The same variable can refer to objects of different types at different times.

### Q3. What are the rules for naming a variable?

**Answer:**

1. It can contain letters, digits, and underscore.
2. It cannot start with a digit.
3. It cannot contain spaces.
4. It cannot be a Python keyword.
5. Variable names are case-sensitive.

Valid:

```python
name = "Faruk"
age_1 = 25
user_name = "admin"
```

Invalid:

```python
1name = "Faruk"
user-name = "Faruk"
class = "Python"
```

### Q4. Is Python case-sensitive?

**Answer:**
Yes, Python is case-sensitive.

```python
name = "Faruk"
Name = "Ahmed"
```

Here `name` and `Name` are two different variables.

---

# 🔥 Most Important Interview Questions

1. What is Python?
2. What is a flowchart?
3. What is an algorithm?
4. What is the difference between an algorithm and a flowchart?
5. What is a variable?
6. Is Python dynamically typed?
7. What is a literal?
8. What are Python keywords?
9. Is `print()` a keyword?
10. What does `input()` return?
11. How do you take integer input in Python?
12. What is type casting?
13. What is implicit type conversion?
14. What is explicit type conversion?
15. What are arithmetic operators?
16. Difference between `/` and `//`.
17. What does `%` do?
18. What does `**` do?
19. Difference between `=` and `==`.
20. Difference between `==` and `is`.
21. What are logical operators?
22. What are membership operators?
23. What are identity operators?
24. What is swapping?
25. How do you swap two variables without a third variable?
26. What is a syntax error?
27. What is a runtime error?
28. What is a logical error?
29. What is `TypeError`?
30. What is `ZeroDivisionError`?
31. What are the rules for naming variables?
32. Is Python case-sensitive?

# Quick Revision

```text
Flowchart
    ↓
Hello World
    ↓
Input / Output
    ↓
Literals
    ↓
Variables
    ↓
Operators
    ↓
Keywords
    ↓
Type Casting
    ↓
Swap
    ↓
Types of Errors
```

# ⭐ Must Remember

```python
input()       → Always returns str
print()       → Built-in function
if            → Keyword
==            → Value equality
is            → Object identity
/             → Division
//            → Floor division
%             → Remainder
**            → Power
int()         → Integer conversion
float()       → Float conversion
str()         → String conversion
a, b = b, a   → Pythonic swapping
```

'''