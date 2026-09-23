# DRY (Don't Repeat Yourself)
# It is a principle of software development that states that every piece of knowledge or logic should be in one place only.

# Example
# 1. You can pass a function as an argument

def greet(name):
    return f"Hello, {name}!"

def call_func(func, value):
    return func(value)



print(call_func(greet, "Ahmed"))