# ============================= What is nested function ==============================

# def outer():
#     print("outer")
#     def inner():
#         print("inner")
#     inner() # calling inner function inside outer function
# outer() # calling outer function

# fun = outer # assign outer function to a variable
# fun() # calling outer function


def add(a, b):
    def subtract(a, b):
        return a - b
    # here calling subtract function inside add function
    # that's why it can access subtract function 
    # because it is scope of add function
    print("Subtract:", subtract(a, b)) # here calling subtract function inside add function 
    return a + b

print('Add:', add(9,6))
d = add
print('Subtract:', d(9,7)) # here calling add function

# def greet(lang, name):
#     def english(word):
#         return word + ", " + name
#     def bangla(word):
#         return word + ", " + name

#     if lang == "english":
#         return english("Hello")
#     elif lang == "bangla":
#         return bangla("Hello")

# print(greet("english", "Faruk"))
# print(greet("bangla", "Faruk"))
