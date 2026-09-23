# IIFE (Immediately Invoked Function Expression)
# It is a function that is executed as soon as it is defined.


# ================================= IIFE with lambda function =================================
# Example
# Function declare + call 
(lambda: print("IIFE in Python executed!"))()

(lambda name: print(f"Hello, {name}!"))("Faruk")

result = (lambda x, y: x + y)(5, 10)
print(result)

# ================================= IIFE with def function =================================
def iife():
    print("Hello")

iife()

