# ==========================================
# all.py
# Module: Example of __all__ usage and scope
# ==========================================

# Common variable definition

str1 = "I'm a string from all.py"


# Function: personal_info()
# Task: Returns a string with name and age
def personal_info(name, age):
    return "I'm from personal_info() function " + name + str(age)


# Function: private_info()
# Task: Returns a string with name and age
def private_info(name, age):
    return "I'm from private_info() function " + name + str(age)

# Function: protected_info()
# Task: Returns a string with name and age
def protected_info(name, age):
    return "I'm from protected_info() function " + name + str(age)


# Function: default_info()
# Task: Returns a string with name and age
def default_info(name, age):
    return "I'm from default_info() function " + name + str(age)


# Class: Test
# Task: A common class, with name and age attribute and __str__() overriden
class Test:
    def __init__(self):
        self.name = "John"  # Default name
        self.age = 30       # Default age

    def __str__(self):
        # When print(Test()) is called, this text will be returned
        return "I'm from Test() class"


# __all__ variable:
# It defines which names will be imported when * is used.
# Example: from all import *
# Only 'str1', 'personal_info' will be imported.
# Other functions or classes will not be imported.
# Here 'str1' and 'personal_info' are imported. only import 'str1' and 'personal_info' from all.py
# when you use * import all from all import *
# check this attribute __all__
__all__ = [
    'str1', 'personal_info'
]

# Example:
# from all import *
# print(str1)                # Will work
# print(personal_info())     # Will not work (__all__ does not contain it)
#
# import all
# print(all.personal_info("John", 30))   # Will work
# print(all.Test())                      # Will work


# print(default_info("John", 30))

# print(personal_info.__name__)
# print(private_info.__name__)
# print(protected_info.__name__)
# print(default_info.__name__)

# print(personal_info.__doc__)
# print(private_info.__doc__)
# print(protected_info.__doc__)
# print(default_info.__doc__)

# print(personal_info.__module__)
# print(private_info.__module__)
# print(protected_info.__module__)
# print(default_info.__module__)

# print(personal_info.__annotations__)
# print(private_info.__annotations__)
# print(protected_info.__annotations__)
# print(default_info.__annotations__)

# print(personal_info.__code__)
# print(private_info.__code__)
# print(protected_info.__code__)
# print(default_info.__code__)

# print(personal_info.__globals__)
# print(private_info.__globals__)
# print(protected_info.__globals__)
# print(default_info.__globals__)

# print(personal_info.__defaults__)
# print(private_info.__defaults__)
# print(protected_info.__defaults__)
# print(default_info.__defaults__)

# print(personal_info.__code__.co_varnames)
# print(private_info.__code__.co_varnames)
# print(protected_info.__code__.co_varnames)
# print(default_info.__code__.co_varnames)
