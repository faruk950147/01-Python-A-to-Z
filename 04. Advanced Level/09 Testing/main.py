"""
# ============================================================
# Python Debugging Tools — Summary Note
# ============================================================


# What Are Debugging Tools?
# -------------------------
# Debugging tools are tools that help us find and fix errors
# (bugs) in our code.
#
# They allow us to:
# - Check variable values
# - Find where an error occurs
# - Pause program execution
# - Trace program flow
# - Test whether our code works correctly


# Common Python Debugging / Testing Tools
# ---------------------------------------
# 1. print()
# 2. breakpoint()
# 3. pdb
# 4. assert
# 5. PyCharm Debugger
# 6. VSCode Debugger
# 7. unittest
# 8. pytest


# ============================================================
# 1. print() Statement
# ============================================================

# print() is the simplest debugging tool.
# It helps us check variable values and understand
# what our code is doing.


# Example:

def add(a, b):
    print("a =", a)
    print("b =", b)
    print("Result =", a + b)

add(1, 2)


# Output:
# a = 1
# b = 2
# Result = 3


# When to use:
# - Small programs
# - Quick debugging
# - Checking variable values


# ============================================================
# 2. breakpoint()
# ============================================================

# breakpoint() pauses the program at a specific point.
#
# It allows us to inspect variables and execute debugging
# commands interactively.


# Example:

def add(a, b):
    breakpoint()
    print(a + b)

add(1, 2)


# When the program reaches breakpoint(),
# execution is paused.


# Useful for:
# - Checking variable values
# - Finding where a problem occurs
# - Step-by-step debugging


# ============================================================
# 3. pdb (Python Debugger)
# ============================================================

# pdb is Python's built-in debugger module.
#
# It allows us to stop program execution and debug
# the program line by line.


import pdb


def add(a, b):
    pdb.set_trace()
    print(a + b)


add(1, 2)


# Common pdb Commands:
#
# n  -> Go to the next line
# c  -> Continue execution
# p  -> Print a variable value
# q  -> Quit the debugger
# l  -> Show the current code
# s  -> Step into a function


# Example:
#
# p a
# p b
#
# These commands show the values of a and b.


# ============================================================
# 4. assert
# ============================================================

# assert is used to check whether a condition is True.
#
# If the condition is True:
#     The program continues.
#
# If the condition is False:
#     Python raises an AssertionError.


# Syntax:
#
# assert condition


# Example:

age = 20

assert age >= 18

print("You are an adult")


# Output:
# You are an adult


# Example with error:

age = 15

assert age >= 18

print("You are an adult")


# Output:
# AssertionError


# We can also provide a message:

age = 15

assert age >= 18, "Age must be 18 or above"


# Output:
# AssertionError: Age must be 18 or above


# When to use assert:
# - Check assumptions
# - Find bugs during development
# - Verify that a condition is correct
# - Check function results


# Example:

def square(n):
    result = n * n
    assert result >= 0
    return result


print(square(5))


# Important:
# assert is mainly useful for debugging and internal checks.
# Do not use assert for important user input validation,
# because Python can disable assertions with optimization.


# ============================================================
# 5. Logical Error
# ============================================================

# A logical error happens when the program runs successfully
# but produces the wrong result.
#
# There is no syntax error.
# There is usually no runtime error.
# The problem is in the logic of the program.


# Example:

def calculate_average(a, b):
    return a + b / 2


print(calculate_average(10, 20))


# Expected:
# 15


# But the actual result is:
# 20.0


# Why?
#
# Python follows operator precedence:
#
# a + b / 2
#
# is calculated as:
#
# a + (b / 2)
#
# Correct code:

def calculate_average(a, b):
    return (a + b) / 2


print(calculate_average(10, 20))


# Output:
# 15.0


# Types of common errors:
#
# 1. Syntax Error
#    -> Wrong Python syntax
#
# 2. Runtime Error
#    -> Error occurs while the program is running
#
# 3. Logical Error
#    -> Program runs but gives the wrong result


# ============================================================
# 6. PyCharm Debugger
# ============================================================

# PyCharm provides a powerful visual debugger.
#
# It allows us to:
# - Set breakpoints
# - Run code in Debug Mode
# - Check variables
# - Step through code
# - Watch expressions
# - Inspect the call stack


# Example:

def add(a, b):
    result = a + b
    return result


result = add(10, 20)
print(result)


# We can place a breakpoint on:
#
# result = a + b
#
# Then run the program using Debug Mode.


# ============================================================
# 7. VSCode Debugger
# ============================================================

# VSCode also provides a built-in visual debugger.
#
# It allows us to:
# - Set breakpoints
# - Start debugging
# - Step over code
# - Step into functions
# - Inspect variables
# - View the call stack


# Example:

def multiply(a, b):
    result = a * b
    return result


result = multiply(5, 4)
print(result)


# We can set a breakpoint inside multiply()
# and inspect the values of a, b, and result.


# ============================================================
# 8. unittest
# ============================================================

# unittest is a built-in Python testing framework.
#
# It is used to test individual parts of a program.
#
# A small test is called a test case.


# Example:

import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)


# Run the test:
#
# python filename.py


# Common unittest methods:
#
# assertEqual(a, b)
# -> Checks whether a == b
#
# assertNotEqual(a, b)
# -> Checks whether a != b
#
# assertTrue(condition)
# -> Checks whether condition is True
#
# assertFalse(condition)
# -> Checks whether condition is False
#
# assertIsNone(value)
# -> Checks whether value is None
#
# assertRaises(Error)
# -> Checks whether an error is raised


# Example:

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_not_equal(self):
        self.assertNotEqual(add(2, 3), 10)


# ============================================================
# 9. pytest
# ============================================================

# pytest is a popular Python testing framework.
#
# It is easier and simpler to write tests with pytest
# compared to unittest.


# First install pytest:
#
# pip install pytest


# Example:

def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5


# Save the file, for example:
#
# test_calculator.py
#
# Run:
#
# pytest


# pytest automatically finds test files and test functions.


# Example:

def multiply(a, b):
    return a * b


def test_multiply():
    assert multiply(3, 4) == 12


def test_add():
    assert add(10, 20) == 30


# Run:
#
# pytest


# ============================================================
# unittest vs pytest
# ============================================================

# unittest:
# - Built into Python
# - Uses classes
# - Uses unittest.TestCase
# - Uses methods like assertEqual()
#
# pytest:
# - External package
# - Simple syntax
# - Uses normal Python functions
# - Uses Python's assert statement
# - Very popular in real-world Python projects


# Example comparison:


# unittest:

import unittest


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2 + 3, 5)


# pytest:

def test_add():
    assert 2 + 3 == 5


# pytest is usually shorter and easier to read.


# ============================================================
# Debugging vs Testing
# ============================================================

# Debugging:
# -> Finding and fixing bugs.
#
# Testing:
# -> Checking whether the program works correctly.


# Example:
#
# A test fails:
#
#     assert add(2, 3) == 5
#
# Then we use debugging tools such as:
#
#     print()
#     breakpoint()
#     pdb
#     PyCharm Debugger
#     VSCode Debugger
#
# to find the problem.


# ============================================================
# Summary
# ============================================================

# Tool          Type             Purpose
# ------------------------------------------------------------
# print()       Built-in         Check values quickly
# breakpoint()  Built-in         Pause and inspect execution
# pdb           Module           CLI-based debugging
# assert        Built-in         Check conditions/assumptions
# PyCharm       IDE              Visual debugging
# VSCode        IDE              Visual debugging
# unittest      Framework        Unit testing
# pytest        Framework        Easy and powerful testing


# ============================================================
# Recommended Workflow
# ============================================================

# For a small problem:
#
#     print()
#         ↓
#     breakpoint()
#
#
# For deeper debugging:
#
#     pdb
#         ↓
#     PyCharm / VSCode Debugger
#
#
# For testing:
#
#     unittest
#         or
#     pytest
#
#
# For checking assumptions:
#
#     assert
#
#
# If the program runs but gives the wrong answer:
#
#     Check for Logical Error


# ============================================================
# Quick Revision
# ============================================================

# print()
# -> Shows values.

# breakpoint()
# -> Pauses the program.

# pdb
# -> Debugs code from the terminal.

# assert
# -> Checks a condition.

# Logical Error
# -> Code runs but gives the wrong result.

# PyCharm
# -> Visual debugging in PyCharm.

# VSCode
# -> Visual debugging in VSCode.

# unittest
# -> Built-in Python testing framework.

# pytest
# -> Simple and powerful testing framework.
"""