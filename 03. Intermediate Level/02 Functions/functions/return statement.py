# What is a return statement?

# The return statement:

# Returns a value from a function to where it was called.

# Exits the function immediately—any code after return inside the function won’t run.

# Allows us to store the result in a variable or use it in expressions.


# def function_name(parameters):
#     # do some work
#     return value


# If a function has no return, Python returns None by default.

# 2. Difference Between print and return

# Feature	print	return
# Purpose	Displays output to the console	Sends value back to the caller
# Scope	Only prints, value not usable outside	Value can be stored in a variable
# Function exit	Function continues after print	Function stops immediately after return

# Example 1: Using print
def simple_interest(p, r, t):
    total = (p * r * t) / 100
    print("Inside function:", total)  # just prints
    # No return statement

result = simple_interest(100, 10, 1)
print("Outside function:", result)


# Output:

# Inside function: 10.0
# Outside function: None


# Explanation: print shows the value, but result is None because the function didn't return anything.

# Example 2: Using return
def simple_interest(p, r, t):
    total = (p * r * t) / 100
    return total  # sends value outside

result = simple_interest(100, 10, 1)
print("Outside function:", result)


# Output:

# Outside function: 10.0


# Explanation: return sends the value 10.0 to result, which we can use anywhere.

# Example 3: Using returned value in calculation
def simple_interest(p, r, t):
    return (p * r * t) / 100

calculated = simple_interest(100, 10, 1)
total = 50 - calculated
print(total)


# Output:

# 40.0


# Here, the returned value is stored in calculated, and we can do further calculations.

# Example 4: Returning multiple values
def math_operations(a, b):
    return a + b, a * b, a - b

sum_val, mul_val, sub_val = math_operations(5, 3)
print(sum_val, mul_val, sub_val)


# Output:

# 8 15 2


# Python allows returning multiple values as a tuple, which can be unpacked.

# 3. Visual Analogy

# Think of a function as a machine:

# print: Shows the product inside the machine window, but you can’t take it out.

# return: Lets you take the product out of the machine to use it elsewhere.

# Function Machine
# +----------------+
# |  Calculation   |
# |  result = 10   |
# +----------------+
#       |
#       v
# print → shows "10" (inside window only)
# return → sends 10 outside (usable anywhere)

# 4. Key Points to Remember

# return ends the function immediately.

# return can be used to pass data outside.

# print is just for showing values, not for further use.

# Variables inside a function are local; you can only access them outside via return.