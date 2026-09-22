# ======================= what is scope =======================

# Scope is the region of the code where a variable is accessible.

# There are 4 types of scope:
# 1. Local scope
# 2. Enclosing scope
# 3. Global scope
# 4. Built-in scope

# Local scope: Variables declared inside a function, accessible only within that function.
# Enclosing scope: Variables from the outer (enclosing) function accessible inside an inner function.
# Global scope: Variables declared at the top level of a module, accessible everywhere in that file.
# Built-in scope: Names that are preassigned in Python, like len(), print(), etc.


def outer_func():
    x = 'local'
    def inner_func():
        print(x)
    return inner_func() # here inner_func() is called
    # return inner_func # here inner_func is returned

a = outer_func()
print(a)

def outer_func():
    x = 5
    def inner_func():
        y = 6
        return x + y
    return inner_func # here inner_func is returned

a = outer_func()
print(a())