# ============================================================
#             PYTHON COMMAND LINE ARGUMENTS
# ============================================================


# ============================================================
# 1. WHAT ARE COMMAND LINE ARGUMENTS?
# ============================================================

# Command Line Arguments are values/arguments that are passed
# to a Python program when the program is executed from
# the command line.

# Example:
#
# python main.py 10 20 hello
#
# Here:
# main.py  -> script name
# 10       -> first argument
# 20       -> second argument
# hello    -> third argument


# ============================================================
# 2. sys MODULE
# ============================================================

# Python provides the 'sys' module to work with command line
# arguments.

import sys


# ============================================================
# 3. sys.argv
# ============================================================

# sys.argv is a list that contains command line arguments.
#
# Structure:
#
# sys.argv[0] -> name of the Python script
# sys.argv[1] -> first command line argument
# sys.argv[2] -> second command line argument
# sys.argv[3] -> third command line argument
# ...


# Example:

# File: main.py

import sys

print(sys.argv)


# Run:
#
# python main.py 10 20 hello
#
# Output:
#
# ['main.py', '10', '20', 'hello']


# ============================================================
# 4. IMPORTANT: sys.argv VALUES ARE STRINGS
# ============================================================

# Command line arguments are received as strings.

# Example:
#
# python main.py 10 20
#
# sys.argv will be:
#
# ['main.py', '10', '20']

# Therefore:
#
# sys.argv[1] -> "10"
# sys.argv[2] -> "20"
#
# They are strings, NOT integers.


# Example:

import sys

num1 = sys.argv[1]
num2 = sys.argv[2]

print(num1)
print(type(num1))

print(num2)
print(type(num2))


# Run:
#
# python main.py 10 20
#
# Output:
#
# 10
# <class 'str'>
# 20
# <class 'str'>


# ============================================================
# 5. CONVERT COMMAND LINE ARGUMENTS
# ============================================================

# We can convert command line arguments to int or float.

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(num1 + num2)


# Run:
#
# python main.py 10 20
#
# Output:
#
# 30


# Using float:

import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print(num1 + num2)


# Run:
#
# python main.py 10 20
#
# Output:
#
# 30.0


# ============================================================
# 6. BASIC sys.argv EXAMPLE
# ============================================================

# File: main.py

import sys

args = sys.argv

print(args)
print(type(args))

print(args[0])
print(args[1])

for arg in args:
    print(arg)


# Run:
#
# python main.py 10 20 hello
#
# Output:
#
# ['main.py', '10', '20', 'hello']
# <class 'list'>
# main.py
# 10
# 10
# 20
# hello


# ============================================================
# 7. len(sys.argv)
# ============================================================

# len(sys.argv) tells us how many items are inside sys.argv.

import sys

print(sys.argv)
print(len(sys.argv))


# Run:
#
# python main.py 10 20 hello
#
# Output:
#
# ['main.py', '10', '20', 'hello']
# 4


# Why 4?
#
# sys.argv[0] -> main.py
# sys.argv[1] -> 10
# sys.argv[2] -> 20
# sys.argv[3] -> hello


# ============================================================
# 8. CHECKING NUMBER OF ARGUMENTS
# ============================================================

# Before accessing sys.argv[index], it is good practice
# to check whether enough arguments were provided.

import sys

if len(sys.argv) < 3:
    print("Usage: python main.py <num1> <num2>")
    sys.exit(1)

num1 = sys.argv[1]
num2 = sys.argv[2]

print(num1)
print(num2)


# ============================================================
# 9. sys.exit()
# ============================================================

# sys.exit() is used to stop/terminate the program.

import sys

if len(sys.argv) < 3:
    print("Not enough arguments!")
    sys.exit(1)

print("Program continues...")


# sys.exit(0)
# Usually means successful termination.

# sys.exit(1)
# Usually means the program terminated because of an error.


# ============================================================
# 10. FILE WRITE USING COMMAND LINE ARGUMENTS
# ============================================================

# File: file.py

import sys

if len(sys.argv) < 3:
    print("Usage: python file.py <filename> <text>")
    sys.exit(1)

filename = sys.argv[1]
text = sys.argv[2]

with open(filename, "w") as f:
    f.write(text)

print("File written successfully.")


# Run:
#
# python file.py filename.txt "Hello World"
#
# This will create:
#
# filename.txt
#
# And write:
#
# Hello World


# ============================================================
# 11. FILE READ USING COMMAND LINE ARGUMENT
# ============================================================

import sys

if len(sys.argv) < 2:
    print("Usage: python file.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    content = f.read()

print(content)


# Run:
#
# python file.py filename.txt


# ============================================================
# 12. WRITE AND READ FILE
# ============================================================

# File: file.py

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


# Run:
#
# python file.py filename.txt "Hello World"
#
# Output:
#
# Hello World


# ============================================================
# 13. HANDLE MULTI-WORD TEXT
# ============================================================

# If text contains spaces, use quotes.

# Correct:
#
# python file.py message.txt "Hello World Python"
#
# Here:
#
# sys.argv[1] -> message.txt
# sys.argv[2] -> Hello World Python


# Without quotes:
#
# python file.py message.txt Hello World Python
#
# Arguments become:
#
# sys.argv[1] -> message.txt
# sys.argv[2] -> Hello
# sys.argv[3] -> World
# sys.argv[4] -> Python


# ============================================================
# 14. SIMPLE CALCULATOR
# ============================================================

# File: calculator.py

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


# Run:
#
# python calculator.py 10 20
#
# Output:
#
# The sum of 10.0 and 20.0 is 30.0


# ============================================================
# 15. CALCULATOR WITH OPERATORS
# ============================================================

# File: calculator.py

import sys

# Check number of arguments
if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <operator> <num2>")
    print("Operators: +, -, *, /")
    sys.exit(1)

# Get command line arguments
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

# Print result
print(f"{num1} {operator} {num2} = {result}")


# ============================================================
# 16. RUN CALCULATOR
# ============================================================

# Addition:
#
# python calculator.py 10 + 20
#
# Output:
#
# 10.0 + 20.0 = 30.0


# Subtraction:
#
# python calculator.py 20 - 10
#
# Output:
#
# 20.0 - 10.0 = 10.0


# Multiplication:
#
# python calculator.py 10 "*" 20
#
# Output:
#
# 10.0 * 20.0 = 200.0


# Division:
#
# python calculator.py 20 / 5
#
# Output:
#
# 20.0 / 5.0 = 4.0


# Division by zero:
#
# python calculator.py 20 / 0
#
# Output:
#
# Error: Division by zero is not allowed.


# ============================================================
# 17. WHY QUOTE "*"?
# ============================================================

# In many shells, '*' has a special meaning.
#
# For example:
#
# python calculator.py 10 * 20
#
# The shell may expand '*' into filenames.
#
# Therefore, it is safer to write:
#
# python calculator.py 10 "*" 20
#
# or:
#
# python calculator.py 10 '*' 20


# ============================================================
# 18. try-except WITH COMMAND LINE ARGUMENTS
# ============================================================

# Command line arguments are strings.
# Invalid values can cause conversion errors.

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


# Run:
#
# python main.py 10 20
#
# Output:
#
# 30.0


# Invalid input:
#
# python main.py abc 20
#
# Output:
#
# Please provide valid numbers.


# ============================================================
# 19. COMPLETE CALCULATOR EXAMPLE
# ============================================================

# File: calculator.py

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


# ============================================================
# 20. COMMAND LINE ARGUMENT FLOW
# ============================================================

# Command:
#
# python calculator.py 10 + 20
#
#
# Step 1:
# Python starts calculator.py
#
# Step 2:
# sys.argv receives:
#
# ['calculator.py', '10', '+', '20']
#
# Step 3:
#
# sys.argv[1] -> '10'
# sys.argv[2] -> '+'
# sys.argv[3] -> '20'
#
# Step 4:
# Convert numbers:
#
# '10' -> 10.0
# '20' -> 20.0
#
# Step 5:
# Check operator:
#
# '+'
#
# Step 6:
# Calculate:
#
# 10.0 + 20.0
#
# Step 7:
# Output:
#
# 30.0


# ============================================================
# 21. IMPORTANT RULES
# ============================================================

# Rule 1:
# Import sys first.
#
# import sys


# Rule 2:
# Use sys.argv to access command line arguments.
#
# sys.argv


# Rule 3:
# sys.argv[0] is normally the script name.
#
# sys.argv[0]


# Rule 4:
# The first user-provided argument starts from index 1.
#
# sys.argv[1]


# Rule 5:
# All command line arguments initially come as strings.
#
# int() or float() can be used for conversion.


# Rule 6:
# Check len(sys.argv) before accessing indexes.


# Rule 7:
# Use sys.exit(1) when you want to stop the program
# because of invalid input.


# Rule 8:
# Use quotes for arguments containing spaces.
#
# python file.py "Hello World"


# ============================================================
# 22. QUICK REFERENCE
# ============================================================

# Command:
#
# python script.py arg1 arg2 arg3
#
#
# sys.argv:
#
# [
#     'script.py',
#     'arg1',
#     'arg2',
#     'arg3'
# ]
#
#
# Index:
#
# sys.argv[0] -> script.py
# sys.argv[1] -> arg1
# sys.argv[2] -> arg2
# sys.argv[3] -> arg3
#
#
# Number of items:
#
# len(sys.argv)
#
#
# Stop program:
#
# sys.exit(1)
#
#
# Convert:
#
# int(sys.argv[1])
# float(sys.argv[1])


# ============================================================
# 23. FINAL SUMMARY
# ============================================================

# Command Line Arguments:
#
# Command line arguments are values passed to a program
# when the program is executed from the command line.
#
# Python uses the sys module to access them.
#
# The main variable is:
#
# sys.argv
#
# sys.argv is a list of strings.
#
# Example:
#
# python main.py 10 20 hello
#
# sys.argv becomes:
#
# ['main.py', '10', '20', 'hello']
#
# Therefore:
#
# sys.argv[0] -> main.py
# sys.argv[1] -> 10
# sys.argv[2] -> 20
# sys.argv[3] -> hello
#
# Remember:
#
# 1. Import sys
# 2. Use sys.argv
# 3. Check len(sys.argv)
# 4. Convert strings when necessary
# 5. Use try-except for invalid input
# 6. Use sys.exit() to stop the program