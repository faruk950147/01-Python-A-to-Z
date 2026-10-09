"""
# Python Command Line Arguments

## 1. What Are Command Line Arguments?

**Command Line Arguments** are values passed to a Python program when we run it from the terminal or command prompt.

### Example

```bash
python main.py 10 20 hello
```

Here:

```text
python   → Python interpreter
main.py  → Python script
10       → First argument
20       → Second argument
hello    → Third argument
```

Python can access these values inside the program.

### Why Do We Use Command Line Arguments?

* To provide input when running a program.
* To pass filenames, numbers, and text.
* To run the same program with different inputs.
* To build command-line tools and automation scripts.

---

## 2. The `sys` Module

Python provides the built-in `sys` module to work with command-line arguments.

```python
import sys

print(sys.argv)
```

Run:

```bash
python main.py 10 20 hello
```

Output:

```python
['main.py', '10', '20', 'hello']
```

The most important variable is:

```python
sys.argv
```

---

## 3. What Is `sys.argv`?

`sys.argv` is a list containing the script invocation name or path, followed by the command-line arguments.

### Example

```python
import sys

print(sys.argv)
print(type(sys.argv))
```

Run:

```bash
python main.py 10 20 hello
```

Output:

```text
['main.py', '10', '20', 'hello']
<class 'list'>
```

### Index Meaning

```text
sys.argv[0] → Script name or path
sys.argv[1] → First user argument
sys.argv[2] → Second user argument
sys.argv[3] → Third user argument
```

**Important:** The first user-provided argument starts at index `1`, not index `0`.

---

## 4. Basic `sys.argv` Example

File: `main.py`

```python
import sys

print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
```

Run:

```bash
python main.py 10 20
```

Output:

```text
['main.py', '10', '20']
main.py
10
20
```

---

## 5. Command Line Arguments Are Strings

All command-line arguments are initially received as strings.

Example:

```bash
python main.py 10 20
```

Python receives:

```python
['main.py', '10', '20']
```

Therefore:

```python
sys.argv[1]
```

contains the string `"10"`, not the integer `10`.

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

Output:

```text
10
<class 'str'>
20
<class 'str'>
```

---

## 6. Convert Command Line Arguments

We often need to convert strings into numbers before performing calculations.

### Convert to Integer

Use `int()`.

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

### Convert to Float

Use `float()`.

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

### Conversion Flow

```text
Command Line Input
        |
        v
     "10" (str)
        |
        v
  int("10") or float("10")
        |
        v
      10 or 10.0
```

---

## 7. Loop Through Command Line Arguments

We can use a `for` loop to access all arguments.

```python
import sys

args = sys.argv

print(args)
print(type(args))

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
20
hello
```

To print only user-provided arguments, use list slicing:

```python
import sys

for arg in sys.argv[1:]:
    print(arg)
```

Output:

```text
10
20
hello
```

Here, `sys.argv[1:]` excludes the script name.

---

## 8. `len(sys.argv)`

`len(sys.argv)` returns the total number of elements in the list, including the script name or path.

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

There are four elements:

```text
sys.argv[0] → main.py
sys.argv[1] → 10
sys.argv[2] → 20
sys.argv[3] → hello
```

### Quick Reference

```text
len(sys.argv)       → Total number of elements
len(sys.argv) - 1   → Number of user arguments
```

---

## 9. Check the Number of Arguments

Before accessing `sys.argv[1]` or `sys.argv[2]`, check whether enough arguments were provided.

```python
import sys

if len(sys.argv) != 3:
    print("Usage: python main.py <num1> <num2>")
    sys.exit(1)

num1 = sys.argv[1]
num2 = sys.argv[2]

print(num1)
print(num2)
```

Run:

```bash
python main.py 10
```

Output:

```text
Usage: python main.py <num1> <num2>
```

This prevents an error such as:

```text
IndexError: list index out of range
```

We use `len(sys.argv) != 3` because the list contains one script entry and two user arguments.

---

## 10. What Is `sys.exit()`?

`sys.exit()` terminates the program.

Example:

```python
import sys

print("Program started")

sys.exit(1)

print("This line will not execute")
```

Output:

```text
Program started
```

### Common Exit Codes

```text
sys.exit(0) → Successful termination
sys.exit(1) → Error or unsuccessful termination
```

Conventionally, `0` means success, while a nonzero exit code indicates failure.

---

## 11. Handle Invalid Input with `try-except`

Converting an invalid string into a number raises `ValueError`.

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
    print("Error: Please provide valid numbers.")
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
Error: Please provide valid numbers.
```

We use `try-except` to handle invalid numeric input gracefully.

---

## 12. Write a File Using Command Line Arguments

We can pass a filename and text from the terminal.

File: `write_file.py`

```python
import sys

if len(sys.argv) != 3:
    print('Usage: python write_file.py <filename> "<text>"')
    sys.exit(1)

filename = sys.argv[1]
content = sys.argv[2]

with open(filename, "w", encoding="utf-8") as file:
    file.write(content)

print("File written successfully.")
```

Run:

```bash
python write_file.py message.txt "Hello World Python"
```

This creates `message.txt` and writes the following text:

```text
Hello World Python
```

**Important:** Opening a file in `"w"` mode overwrites its existing contents.

---

## 13. Read a File Using Command Line Arguments

We can pass a filename and read its contents.

File: `read_file.py`

```python
import sys

if len(sys.argv) != 2:
    print("Usage: python read_file.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print(f"Error: File '{filename}' was not found.")
    sys.exit(1)
```

Run:

```bash
python read_file.py message.txt
```

The program reads and prints the file contents. If the file does not exist, it handles the `FileNotFoundError`.

---

## 14. Handle Text Containing Spaces

Use quotation marks when an argument contains spaces.

### Correct

```bash
python main.py "Hello World Python"
```

Python receives:

```python
['main.py', 'Hello World Python']
```

The text is treated as one argument.

### Without Quotes

```bash
python main.py Hello World Python
```

Python receives:

```python
['main.py', 'Hello', 'World', 'Python']
```

The three words become separate arguments.

---

## 15. Simple Calculator Using Command Line Arguments

File: `calculator.py`

```python
import sys

if len(sys.argv) != 3:
    print("Usage: python calculator.py <num1> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

except ValueError:
    print("Error: Please provide valid numbers.")
    sys.exit(1)

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

## 16. Calculator with Operators

This calculator supports addition, subtraction, multiplication, and division.

File: `calculator.py`

```python
import sys

# Step 1: Check argument count
if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <operator> <num2>")
    print('Example: python calculator.py 10 "+" 20')
    sys.exit(1)

# Step 2: Get arguments
num1 = sys.argv[1]
operator = sys.argv[2]
num2 = sys.argv[3]

# Step 3: Convert strings to numbers
try:
    num1 = float(num1)
    num2 = float(num2)

except ValueError:
    print("Error: Please provide valid numbers.")
    sys.exit(1)

# Step 4: Perform calculation
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

# Step 5: Display result
print(f"{num1} {operator} {num2} = {result}")
```

### Run the Calculator

**Addition**

```bash
python calculator.py 10 + 20
```

Output:

```text
10.0 + 20.0 = 30.0
```

**Subtraction**

```bash
python calculator.py 20 - 10
```

Output:

```text
20.0 - 10.0 = 10.0
```

**Multiplication**

```bash
python calculator.py 10 "*" 20
```

Output:

```text
10.0 * 20.0 = 200.0
```

**Division**

```bash
python calculator.py 20 / 5
```

Output:

```text
20.0 / 5.0 = 4.0
```

**Division by Zero**

```bash
python calculator.py 20 / 0
```

Output:

```text
Error: Division by zero is not allowed.
```

### Why Do We Quote `*`?

In many shells, `*` is a wildcard that can match filenames in the current directory.

Therefore, use:

```bash
python calculator.py 10 "*" 20
```

This is shell behavior, not a Python-specific problem.

---

## 17. Command Line Argument Execution Flow

Suppose we run:

```bash
python calculator.py 10 + 20
```

### Step 1: Python Starts the Script

```text
calculator.py
```

### Step 2: Python Receives the Arguments

```python
['calculator.py', '10', '+', '20']
```

### Step 3: Access the Arguments

```text
sys.argv[1] → '10'
sys.argv[2] → '+'
sys.argv[3] → '20'
```

### Step 4: Convert the Numbers

```text
'10' → 10.0
'20' → 20.0
```

### Step 5: Check the Operator

```text
+
```

### Step 6: Perform the Calculation

```text
10.0 + 20.0
```

### Step 7: Display the Result

```text
10.0 + 20.0 = 30.0
```

### Complete Flow

```text
Terminal
   |
   v
python calculator.py 10 + 20
   |
   v
sys.argv
   |
   v
['calculator.py', '10', '+', '20']
   |
   v
Extract arguments
   |
   v
Convert numeric strings
   |
   v
Check operator
   |
   v
Calculate result
   |
   v
Print output
```

---

## 18. Important Rules

### Rule 1: Import the `sys` Module

```python
import sys
```

### Rule 2: Use `sys.argv`

```python
sys.argv
```

### Rule 3: Script Name Is Usually at Index 0

```python
sys.argv[0]
```

### Rule 4: The First User Argument Starts at Index 1

```python
sys.argv[1]
```

### Rule 5: Arguments Are Strings

```python
int(sys.argv[1])
float(sys.argv[1])
```

### Rule 6: Check the Argument Count

```python
len(sys.argv)
```

### Rule 7: Handle Invalid Input

```python
try:
    number = float(sys.argv[1])
except ValueError:
    print("Invalid number")
```

### Rule 8: Stop the Program When Necessary

```python
sys.exit(1)
```

### Rule 9: Use Quotes for Text Containing Spaces

```bash
python main.py "Hello World"
```

---

## 19. Quick Reference

### Command

```bash
python script.py arg1 arg2 arg3
```

### `sys.argv`

```python
['script.py', 'arg1', 'arg2', 'arg3']
```

### Index

```text
sys.argv[0] → script.py
sys.argv[1] → arg1
sys.argv[2] → arg2
sys.argv[3] → arg3
```

### Number of Elements

```python
len(sys.argv)
```

### Number of User Arguments

```python
len(sys.argv) - 1
```

### Convert to Integer

```python
int(sys.argv[1])
```

### Convert to Float

```python
float(sys.argv[1])
```

### Stop the Program

```python
sys.exit(1)
```

---

## 20. Important Interview Questions

### Q1. What are command line arguments?

Command-line arguments are values passed to a program when it is executed from the terminal.

### Q2. Which module is used to access basic command-line arguments?

The built-in `sys` module.

```python
import sys
```

### Q3. What is `sys.argv`?

`sys.argv` is a list containing the script invocation name or path and the command-line arguments.

### Q4. What does `sys.argv[0]` contain?

Normally, it contains the script name or path used to invoke the program.

### Q5. Where does the first user argument start?

At index `1`.

```python
sys.argv[1]
```

### Q6. What is the type of command-line arguments?

They are initially strings.

For example:

```python
sys.argv[1]
```

To convert a value into a number:

```python
int(sys.argv[1])
```

### Q7. What does `len(sys.argv)` return?

It returns the total number of elements, including the script invocation name or path.

### Q8. Why should we check the argument count?

To ensure the required arguments are provided before accessing list indexes and to prevent `IndexError`.

### Q9. What is `sys.exit()`?

It terminates the program and can return an exit status to the operating system.

### Q10. Why do we use `try-except`?

To handle errors such as `ValueError` when converting invalid strings to numbers.

### Q11. What is the difference between `sys.argv` and `argparse`?

`sys.argv` provides raw command-line arguments as a list of strings. `argparse` provides a more convenient way to define options, flags, type conversion, validation, and help messages.

---

## 21. Final Summary

Command-line arguments allow us to pass values to a Python program from the terminal.

Python provides the built-in `sys` module to access these values.

```python
import sys
```

The main variable is:

```python
sys.argv
```

Example command:

```bash
python main.py 10 20 hello
```

The resulting list is normally:

```python
['main.py', '10', '20', 'hello']
```

Remember these six points:

1. Import `sys`.
2. Use `sys.argv` to access command-line arguments.
3. `sys.argv[0]` usually contains the script name or path.
4. The first user argument starts at `sys.argv[1]`.
5. Arguments are strings, so use `int()` or `float()` when needed.
6. Validate the argument count and handle errors with `try-except` and `sys.exit()`.

### One-Line Definition

**Command Line Arguments are values passed to a Python program from the terminal, and Python provides `sys.argv` to access them.**

### Next Topic

After learning `sys.argv`, learn Python's `argparse` module for building more professional command-line applications.

"""