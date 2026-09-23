# ============================= What is a Function ==============================
# A function is a block of reusable code that performs a specific task.
# In functional programming, there are four types of identifiers:
# 1 local identifier
# 2 nonlocal identifier
# 3 global identifier
# 4 built-in identifier


# ============================= 🧩 Local Identifier or Variable ==============================
# A local identifier (or local variable) is a variable that is defined inside a function.
# It is created when the function starts executing and destroyed when the function ends.

def display(name):
    # 'age' is a local identifier because it is defined inside the function
    # 'name' is also a local identifier because it is defined as a parameter
    age = 21
    print(f"Name: {name} has age {age}")
    print(locals())

display("John")  # Function call


# =============================  Working Flow of a Function =============================

# STEP 1: FUNCTION DEFINITION  
# In this step, the function is defined but the code inside it is not executed.  
# Python just registers the function name in the namespace and skips its body.  
# The namespace is like a dictionary that maps names to objects, e.g.:
#     { function_name : function_object }
# Function objects are stored in the namespace until they are called.
# Python executes other code unless the function is explicitly called.

def greet():
    print("Hello, World!")


# STEP 2: FUNCTION CALL  
# When the function is called, Python allocates memory for it and jumps to its body.  
# Example: calling `greet()` executes the code inside that function.

greet()


# STEP 3: FUNCTION EXECUTION  
# The code inside the function executes **line by line**.
# Example: Here, `print("Hello, World!")` runs and prints text to the console.


# STEP 4: FUNCTION RETURN  
# After the function finishes executing, control returns to the caller.  
# If no `return` statement is used, Python automatically returns None.
