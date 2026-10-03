# Python Debugging Tools — Summary Note


# What Are Debugging Tools?

# **Debugging tools** are tools that help you find and fix errors (bugs) in your code.  
# They allow you to check variable values, pause execution, and trace the program flow.


# How to Use Debugging Tools

# 1. **print statement**  
# 2. **breakpoint()**  
# 3. **pdb (Python Debugger)**  
# 4. **PyCharm IDE**  
# 5. **VSCode IDE**



#1. print() Statement

# The print() statement is the simplest debugging tool.  
# It helps you understand what your code is doing by printing variable values.

# Example:
def add(a, b):
    print(a, b)
    print(a + b)

add(1, 2)

# 2. breakpoint()

# The breakpoint() function pauses the program at a specific point.
# You can inspect variables or step through code interactively.

# Example:
def add(a, b):
    breakpoint()
    print(a + b)

add(1, 2)

# 3. pdb (Python Debugger)

# pdb is a built-in Python module for debugging.
# It lets you stop execution and inspect variables line by line.

# Example:
import pdb

def add(a, b):
    pdb.set_trace()
    print(a + b)

add(1, 2)

# Common pdb Commands:
# Command	Description
# n	Go to the next line
# c	Continue execution
# p variable	Print the value of a variable
# q	Quit the debugger
# 4. PyCharm Debugger

# PyCharm provides a powerful visual debugger.
# You can set breakpoints, run in Debug Mode, and inspect variables in real-time.

# Example:
def add(a, b):
    print(a + b)

add(1, 2)

# 5. VSCode Debugger

# VSCode also includes a built-in debugger.
# You can set breakpoints, step through code, and view variables.

# Example:
def add(a, b):
    print(a + b)

add(1, 2)

# Summary
# Tool	Type	Purpose
# print()	Built-in	Simple value checking
# breakpoint()	Built-in	Pause and inspect execution
# pdb	Module	Interactive CLI debugging
# PyCharm	IDE	GUI-based debugging
# VSCode	IDE	GUI-based debugging

# Tip: Start with print() and breakpoint() for small scripts.
# Use pdb, PyCharm, or VSCode for large projects.