"""
# Python Command Line Arguments

## 1. What Are Command Line Arguments?

**Command Line Arguments** are values that we give to a Python program when we run it from the command line or terminal.

### Example

```bash
python main.py 10 20 hello
```

Here:

```text
main.py  → Python file / script
10       → First argument
20       → Second argument
hello    → Third argument
```

Python can read these values inside the program.

---

# 2. The `sys` Module

Python provides the **`sys` module** to work with command line arguments.

First, import it:

```python
import sys
```

The most important variable for command line arguments is:

```python
sys.argv
```

---

# 3. What Is `sys.argv`?

`sys.argv` is a **list** that contains the command line arguments.

### Example

Suppose we run:

```bash
python main.py 10 20 hello
```

Then:

```python
sys.argv
```

will contain:

```python
['main.py', '10', '20', 'hello']
```

### Index Meaning

```text
sys.argv[0] → script name
sys.argv[1] → first user argument
sys.argv[2] → second user argument
sys.argv[3] → third user argument
```

### Important

The first user-provided argument starts from **index 1**, not index 0.

---

# 4. Basic `sys.argv` Example

### File: `main.py`

```python
import sys

print(sys.argv)
```

Run:

```bash
python main.py 10 20 hello
```

Output:

```text
['main.py', '10', '20', 'hello']
```

So:

```text
sys.argv[0] → main.py
sys.argv[1] → 10
sys.argv[2] → 20
sys.argv[3] → hello
```

---

# 5. Important: `sys.argv` Values Are Strings

This is one of the most important points.

All command line arguments initially come as **strings**.

Example:

```bash
python main.py 10 20
```

Python receives:

```python
['main.py', '10', '20']
```

So:

```python
sys.argv[1]
```

is:

```text
"10"
```

not:

```text
10
```

Its type is:

```python
<class 'str'>
```

### Example

```python
import sys

num1 = sys.argv[1]
num2 = sys.argv[2]

print(num1)
print(type(num1))

print(num2)
print(type(num2))
```

Run:

```bash
python main.py 10 20
```

Output:

```text
10
<class 'str'>

20
<class 'str'>
```

---

# 6. Convert Command Line Arguments

Because command line arguments are strings, we often need to convert them to numbers.

## Convert to Integer

Use:

```python
int()
```

Example:

```python
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(num1 + num2)
```

Run:

```bash
python main.py 10 20
```

Output:

```text
30
```

---

## Convert to Float

Use:

```python
float()
```

Example:

```python
import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print(num1 + num2)
```

Run:

```bash
python main.py 10 20
```

Output:

```text
30.0
```

### Remember

```text
Command line → String
                  ↓
              int() / float()
                  ↓
                Number
```

---

# 7. Basic `sys.argv` Example

```python
import sys

args = sys.argv

print(args)
print(type(args))

print(args[0])
print(args[1])

for arg in args:
    print(arg)
```

Run:

```bash
python main.py 10 20 hello
```

Output:

```text
['main.py', '10', '20', 'hello']
<class 'list'>
main.py
10
main.py
10
20
hello
```

### Why does `main.py` appear twice?

Because:

```python
print(args[0])
```

prints `main.py`.

Then:

```python
for arg in args:
```

loops through the entire list again.

---

# 8. `len(sys.argv)`

`len(sys.argv)` tells us how many items are inside the `sys.argv` list.

Example:

```python
import sys

print(sys.argv)
print(len(sys.argv))
```

Run:

```bash
python main.py 10 20 hello
```

Output:

```text
['main.py', '10', '20', 'hello']
4
```

Why `4`?

```text
sys.argv[0] → main.py
sys.argv[1] → 10
sys.argv[2] → 20
sys.argv[3] → hello
```

So there are **4 total items**.

### Important

`len(sys.argv)` includes the script name.

---

# 9. Check the Number of Arguments

Before accessing:

```python
sys.argv[1]
sys.argv[2]
```

it is a good idea to check whether the user provided enough arguments.

Example:

```python
import sys

if len(sys.argv) < 3:
    print("Usage: python main.py <num1> <num2>")
    sys.exit(1)

num1 = sys.argv[1]
num2 = sys.argv[2]

print(num1)
print(num2)
```

If the user runs:

```bash
python main.py 10
```

the program will show:

```text
Usage: python main.py <num1> <num2>
```

This prevents an error such as:

```text
IndexError: list index out of range
```

---

# 10. `sys.exit()`

`sys.exit()` is used to **stop the program**.

Example:

```python
import sys

if len(sys.argv) < 3:
    print("Not enough arguments!")
    sys.exit(1)

print("Program continues...")
```

If there are not enough arguments:

```python
sys.exit(1)
```

stops the program.

### Exit Codes

Commonly:

```text
sys.exit(0) → Successful termination
sys.exit(1) → Error / unsuccessful termination
```

The exact meaning of nonzero exit codes can be defined by the program, but `0` conventionally means success and nonzero usually indicates an error.

---

# 11. Write a File Using Command Line Arguments

We can pass a filename and text from the terminal.

### File: `file.py`

```python
import sys

if len(sys.argv) < 3:
    print("Usage: python file.py <filename> <text>")
    sys.exit(1)

filename = sys.argv[1]
text = sys.argv[2]

with open(filename, "w") as f:
    f.write(text)

print("File written successfully.")
```

Run:

```bash
python file.py filename.txt "Hello World"
```

This creates:

```text
filename.txt
```

and writes:

```text
Hello World
```

inside it.

---

# 12. Read a File Using Command Line Arguments

We can also pass the filename from the terminal.

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python file.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    content = f.read()

print(content)
```

Run:

```bash
python file.py filename.txt
```

The program reads and prints the file content.

---

# 13. Write and Read a File

We can combine both operations.

```python
import sys

if len(sys.argv) < 3:
    print("Usage: python file.py <filename> <text>")
    sys.exit(1)

filename = sys.argv[1]
text = sys.argv[2]

# Write to file
with open(filename, "w") as f:
    f.write(text)

# Read from file
with open(filename, "r") as f:
    print(f.read())
```

Run:

```bash
python file.py filename.txt "Hello World"
```

Output:

```text
Hello World
```

---

# 14. How to Handle Text with Spaces

If an argument contains spaces, use **quotes**.

### Correct

```bash
python file.py message.txt "Hello World Python"
```

Then:

```text
sys.argv[1] → message.txt
sys.argv[2] → Hello World Python
```

Without quotes:

```bash
python file.py message.txt Hello World Python
```

Python receives:

```text
sys.argv[1] → message.txt
sys.argv[2] → Hello
sys.argv[3] → World
sys.argv[4] → Python
```

### Remember

```text
"Hello World Python"
        ↓
One argument
```

Without quotes:

```text
Hello World Python
        ↓
Three arguments
```

---

# 15. Simple Calculator

We can create a calculator using command line arguments.

### File: `calculator.py`

```python
import sys

# Check arguments
if len(sys.argv) != 3:
    print("Usage: python calculator.py <num1> <num2>")
    sys.exit(1)

# Get arguments
num1 = sys.argv[1]
num2 = sys.argv[2]

# Convert to float
try:
    num1 = float(num1)
    num2 = float(num2)

except ValueError:
    print("Please provide valid numbers.")
    sys.exit(1)

# Addition
result = num1 + num2

print(f"The sum of {num1} and {num2} is {result}")
```

Run:

```bash
python calculator.py 10 20
```

Output:

```text
The sum of 10.0 and 20.0 is 30.0
```

---

# 16. Calculator with Operators

We can allow the user to choose an operator.

### File: `calculator.py`

```python
import sys

# Check number of arguments
if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <operator> <num2>")
    print("Operators: +, -, *, /")
    sys.exit(1)

# Get arguments
num1 = sys.argv[1]
operator = sys.argv[2]
num2 = sys.argv[3]

# Convert numbers
try:
    num1 = float(num1)
    num2 = float(num2)

except ValueError:
    print("Please provide valid numbers.")
    sys.exit(1)

# Perform calculation
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":

    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        sys.exit(1)

    result = num1 / num2

else:
    print("Invalid operator!")
    print("Use one of: +, -, *, /")
    sys.exit(1)

print(f"{num1} {operator} {num2} = {result}")
```

---

# 17. Run the Calculator

## Addition

```bash
python calculator.py 10 + 20
```

Output:

```text
10.0 + 20.0 = 30.0
```

## Subtraction

```bash
python calculator.py 20 - 10
```

Output:

```text
20.0 - 10.0 = 10.0
```

## Multiplication

On many shells, it is safer to quote `*`:

```bash
python calculator.py 10 "*" 20
```

Output:

```text
10.0 * 20.0 = 200.0
```

## Division

```bash
python calculator.py 20 / 5
```

Output:

```text
20.0 / 5.0 = 4.0
```

## Division by Zero

```bash
python calculator.py 20 / 0
```

Output:

```text
Error: Division by zero is not allowed.
```

---

# 18. Why Do We Quote `*`?

In many command-line shells, `*` has a special meaning.

For example:

```bash
python calculator.py 10 * 20
```

The shell may replace `*` with filenames from the current directory.

So it is safer to write:

```bash
python calculator.py 10 "*" 20
```

or:

```bash
python calculator.py 10 '*' 20
```

### Important

This is mainly a **shell behavior**, not a Python problem.

---

# 19. `try-except` with Command Line Arguments

Command line arguments are strings.

If we try to convert an invalid string to a number, Python raises `ValueError`.

Example:

```python
import sys

if len(sys.argv) != 3:
    print("Usage: python main.py <num1> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

except ValueError:
    print("Please provide valid numbers.")
    sys.exit(1)

print(num1 + num2)
```

### Valid Input

```bash
python main.py 10 20
```

Output:

```text
30.0
```

### Invalid Input

```bash
python main.py abc 20
```

Output:

```text
Please provide valid numbers.
```

### Why use `try-except`?

Because:

```python
float("abc")
```

causes:

```text
ValueError
```

`try-except` lets us handle the error gracefully.

---

# 20. Complete Calculator Example

```python
import sys

# Check number of arguments
if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <operator> <num2>")
    print("Example: python calculator.py 10 + 20")
    sys.exit(1)

# Get arguments
num1 = sys.argv[1]
operator = sys.argv[2]
num2 = sys.argv[3]

# Convert numbers
try:
    num1 = float(num1)
    num2 = float(num2)

except ValueError:
    print("Error: Please provide valid numbers.")
    sys.exit(1)

# Calculation
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":

    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        sys.exit(1)

    result = num1 / num2

else:
    print("Error: Invalid operator.")
    print("Valid operators: +, -, *, /")
    sys.exit(1)

# Output
print(f"{num1} {operator} {num2} = {result}")
```

---

# 21. Command Line Argument Flow

Suppose we run:

```bash
python calculator.py 10 + 20
```

### Step 1: Python starts the program

Python starts:

```text
calculator.py
```

### Step 2: `sys.argv` receives the values

```python
[
    'calculator.py',
    '10',
    '+',
    '20'
]
```

### Step 3: Access the arguments

```text
sys.argv[1] → '10'
sys.argv[2] → '+'
sys.argv[3] → '20'
```

### Step 4: Convert numbers

```text
'10' → 10.0
'20' → 20.0
```

### Step 5: Check the operator

```text
+
```

### Step 6: Calculate

```text
10.0 + 20.0
```

### Step 7: Show the result

```text
30.0
```

### Complete Flow

```text
Terminal
   ↓
python calculator.py 10 + 20
   ↓
sys.argv
   ↓
['calculator.py', '10', '+', '20']
   ↓
Get arguments
   ↓
Convert numbers
   ↓
Check operator
   ↓
Calculate
   ↓
Print result
```

---

# 22. Important Rules

## Rule 1: Import `sys`

```python
import sys
```

---

## Rule 2: Use `sys.argv`

```python
sys.argv
```

to access command line arguments.

---

## Rule 3: `sys.argv[0]` is normally the script name

```python
sys.argv[0]
```

Example:

```text
calculator.py
```

---

## Rule 4: First user argument starts at index 1

```python
sys.argv[1]
```

---

## Rule 5: Arguments are strings

For example:

```python
sys.argv[1]
```

may contain:

```text
"10"
```

not:

```text
10
```

Convert when necessary:

```python
int(sys.argv[1])
```

or:

```python
float(sys.argv[1])
```

---

## Rule 6: Check the argument count

Before using indexes, check:

```python
len(sys.argv)
```

This helps prevent:

```text
IndexError
```

---

## Rule 7: Use `sys.exit()` when necessary

Example:

```python
sys.exit(1)
```

This stops the program.

---

## Rule 8: Use quotes for arguments containing spaces

Example:

```bash
python file.py "Hello World"
```

Without quotes, `Hello` and `World` may become separate arguments.

---

# 23. Quick Reference

### Command

```bash
python script.py arg1 arg2 arg3
```

### `sys.argv`

```python
[
    'script.py',
    'arg1',
    'arg2',
    'arg3'
]
```

### Index

```text
sys.argv[0] → script.py
sys.argv[1] → arg1
sys.argv[2] → arg2
sys.argv[3] → arg3
```

### Number of Items

```python
len(sys.argv)
```

### Stop Program

```python
sys.exit(1)
```

### Convert to Integer

```python
int(sys.argv[1])
```

### Convert to Float

```python
float(sys.argv[1])
```

---

# 24. Important Interview Questions

## Q1. What are Command Line Arguments?

Command Line Arguments are values passed to a program when it is executed from the command line.

---

## Q2. Which module is used for basic command line arguments?

```python
sys
```

Example:

```python
import sys
```

---

## Q3. What is `sys.argv`?

`sys.argv` is a list containing the command line arguments passed to the Python program.

---

## Q4. What does `sys.argv[0]` contain?

Normally, it contains the name or path used to invoke the Python script.

---

## Q5. Where does the first user argument start?

At:

```python
sys.argv[1]
```

---

## Q6. What type are command line arguments?

They are initially **strings**.

Example:

```python
sys.argv[1]
```

may contain:

```text
"100"
```

To use it as a number:

```python
int(sys.argv[1])
```

---

## Q7. What is `len(sys.argv)` used for?

It tells us the total number of items in `sys.argv`, including the script name.

---

## Q8. Why should we check `len(sys.argv)`?

To make sure the required arguments were provided before accessing indexes.

It helps prevent:

```text
IndexError
```

---

## Q9. What is `sys.exit()`?

`sys.exit()` stops the Python program.

Example:

```python
sys.exit(1)
```

---

## Q10. Why do we use `try-except` with command line arguments?

Because converting an invalid string to a number can raise `ValueError`.

Example:

```python
float("abc")
```

causes:

```text
ValueError
```

---

# 25. Final Summary

### Command Line Arguments

Command Line Arguments are values passed to a Python program when it is run from the terminal.

Python provides the `sys` module to access them.

```python
import sys
```

The main variable is:

```python
sys.argv
```

`sys.argv` is a **list of strings**.

### Example

Command:

```bash
python main.py 10 20 hello
```

`sys.argv` becomes:

```python
['main.py', '10', '20', 'hello']
```

Therefore:

```text
sys.argv[0] → main.py
sys.argv[1] → 10
sys.argv[2] → 20
sys.argv[3] → hello
```

### Remember These 6 Points

```text
1. Import sys
       ↓
   import sys

2. Use sys.argv
       ↓
   sys.argv

3. Script name is usually argv[0]
       ↓
   sys.argv[0]

4. First user argument is argv[1]
       ↓
   sys.argv[1]

5. Arguments are strings
       ↓
   int() / float() when needed

6. Check and handle errors
       ↓
   len(sys.argv)
   try-except
   sys.exit()
```

# Final Mental Model

```text
             COMMAND LINE
                  │
                  ▼
     python main.py 10 20 hello
                  │
                  ▼
              sys.argv
                  │
                  ▼
   ['main.py', '10', '20', 'hello']
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      [1]       [2]       [3]
       10        20       hello
        │
        ▼
  Convert if needed
        │
        ▼
   int() / float()
        │
        ▼
   Process the data
        │
        ▼
      Output
```

### One-Line Definition

> **Command Line Arguments are values passed to a Python program from the terminal, and Python provides `sys.argv` to access them.**

"""