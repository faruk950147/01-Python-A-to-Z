# ============================= nested function return call =============================
# def outer_func():
#     x = 'local'
#     def inner_func():
#         print(x)
#     return inner_func() # here inner_func() is called

# outer_func()

# ============================= nested function return reference =============================
# def outer_func():
#     x = 'local'
#     def inner_func():
#         print(x)
#     return inner_func # here inner_func is returned

# a = outer_func()
# print(a())
# print(a.__name__)

# ============================= nested function return reference =============================
def outer_func():
    x = 5
    def inner_func():
        y = 6
        return x + y
    return inner_func # here inner_func is returned

a = outer_func()
print(a())
print(a.__name__)