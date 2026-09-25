# ==========================================
# Python return Statement
# ==========================================

# What is a return statement?
#
# The return statement:
#
# 1. Returns a value from a function to where it was called.
# 2. Exits the function immediately.
# 3. Allows us to store the result in a variable.
# 4. Allows us to use the returned value in expressions.


# Basic Syntax:
#
# def function_name(parameters):
#     # do some work
#     return value


# If a function has no return statement,
# Python returns None by default.


# ==========================================
# 1. Difference Between print() and return
# ==========================================

# Feature       print()                    return
# Purpose       Displays output            Sends value back to caller
# Usage         Mainly for displaying      Used to produce a result
# Value         Cannot be directly reused  Can be stored and reused
# Function      Function continues         Function stops immediately


# ==========================================
# Example 1: Using print()
# ==========================================

def simple_interest(p, r, t):
    total = (p * r * t) / 100
    print("Inside function:", total)
    # No return statement


result = simple_interest(100, 10, 1)

print("Outside function:", result)


# Output:
#
# Inside function: 10.0
# Outside function: None


# Explanation:
# print() only displays the value.
# The function does not return anything.
# Therefore, Python returns None by default.


# ==========================================
# Example 2: Using return
# ==========================================

def simple_interest(p, r, t):
    total = (p * r * t) / 100
    return total


result = simple_interest(100, 10, 1)

print("Outside function:", result)


# Output:
#
# Outside function: 10.0


# Explanation:
# return sends the value 10.0 back to the caller.
# The returned value is stored in result.


# ==========================================
# Example 3: Using Returned Value in Calculation
# ==========================================

def simple_interest(p, r, t):
    return (p * r * t) / 100


calculated = simple_interest(100, 10, 1)

total = 50 - calculated

print(total)


# Output:
#
# 40.0


# Explanation:
# The function returns 10.0.
#
# calculated = 10.0
#
# Then:
#
# total = 50 - calculated
# total = 50 - 10.0
# total = 40.0


# ==========================================
# Example 4: Returning Multiple Values
# ==========================================

def math_operations(a, b):
    return a + b, a * b, a - b


sum_val, mul_val, sub_val = math_operations(5, 3)

print(sum_val)
print(mul_val)
print(sub_val)


# Output:
#
# 8
# 15
# 2


# Explanation:
# Python returns multiple values as a tuple.
#
# return a + b, a * b, a - b
#
# is equivalent to:
#
# return (a + b, a * b, a - b)
#
# The returned tuple:
#
# (8, 15, 2)
#
# is then unpacked into:
#
# sum_val = 8
# mul_val = 15
# sub_val = 2


# ==========================================
# Example 5: return Stops the Function
# ==========================================

def test():
    print("Hello")

    return 10

    print("World")


result = test()

print(result)


# Output:
#
# Hello
# 10


# Explanation:
# When Python reaches return,
# the function stops immediately.
#
# Therefore, "World" is never printed.


# ==========================================
# Example 6: return Without a Value
# ==========================================

def check_number(num):

    if num > 0:
        print("Positive")
        return

    print("Zero or negative")


check_number(10)


# Output:
#
# Positive


# return without a value is equivalent to:
#
# return None


# ==========================================
# Example 7: Function Without return
# ==========================================

def hello():
    print("Hello")


result = hello()

print(result)


# Output:
#
# Hello
# None


# Explanation:
# If a function does not have a return statement,
# Python automatically returns None.


# ==========================================
# Example 8: Local Variable and return
# ==========================================

def calculate():
    result = 100
    return result


x = calculate()

print(x)


# Output:
#
# 100


# The variable result is local to the function.
# We cannot directly access it outside the function.
#
# return allows us to send its value outside.


# ==========================================
# Example 9: print() vs return
# ==========================================

def square_print(n):
    print(n * n)


def square_return(n):
    return n * n


# Using print()
x = square_print(5)

print("x =", x)


# Output:
#
# 25
# x = None


# Using return()
x = square_return(5)

print("x =", x)


# Output:
#
# x = 25


# ==========================================
# Example 10: Reusing Returned Value
# ==========================================

def square(n):
    return n * n


x = square(5)

y = x + 10

print(y)


# Output:
#
# 35


# Explanation:
#
# square(5) returns 25
#
# x = 25
#
# y = x + 10
# y = 25 + 10
# y = 35


# ==========================================
# Visual Analogy
# ==========================================

# Think of a function as a machine:
#
#
#              FUNCTION
#          +---------------+
# Input -> |  Calculation  |
#          |               |
#          |  result = 10  |
#          +---------------+
#                  |
#                  v
#               return
#                  |
#                  v
#              Outside
#
#
# print():
#
# Function
#    |
#    +---- print(10)
#              |
#              v
#          Shows 10
#
#
# return:
#
# Function
#    |
#    +---- return 10
#              |
#              v
#          10 comes outside
#              |
#              v
#          result = 10


# ==========================================
# Key Points to Remember
# ==========================================

# 1. return sends a value back to the caller.

# 2. return immediately stops the function.

# 3. print() only displays a value.

# 4. A returned value can be stored in a variable.

# 5. A returned value can be used in calculations.

# 6. A function without return returns None.

# 7. return without a value is the same as return None.

# 8. Python can return multiple values as a tuple.


# ==========================================
# Golden Rule
# ==========================================

# print()  -> For showing a value
#
# return   -> For giving a value back


# Most Important:
#
# return value
#     -> sends the value back
#
# return
#     -> stops the function and returns None
#
# no return
#     -> Python returns None automatically