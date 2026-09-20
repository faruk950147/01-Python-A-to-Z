"""
# =================== Python Datatypes ===================
What is a Datatype?
-------------------
In Python, a datatype defines what kind of value a variable holds.

Python is a dynamically typed language, meaning you don’t need to explicitly declare the datatype — it is decided automatically based on the assigned value.


1. Primitive Datatypes
   It has unlimited length of digits, only limited by memory.
   But in other programming languages, numbers have a fixed size.

   - int        → 10, -5, 1000
     # it has unlimited length of digits only limited by memory

   - float      → 3.14, -0.5
     # it has limited length of digits (approximately 15–17 decimal digits)
     # and a value range of about ±1.8 × 10^308

   - complex    → 2+3j
     # consists of a real and an imaginary part
     # both parts are stored as float values

   - bool       → True, False
     # represents Boolean values (True = 1, False = 0)

   - NoneType   → None
     # represents the absence of a value or null

   - bytes      → b"hello"
     # represents an immutable sequence of bytes

   - bytearray  → bytearray([65, 66, 67])
     # represents a mutable sequence of bytes

   - memoryview → memoryview(b"hello")
     # provides a memory view of a bytes-like object


2. Non-Primitive Datatypes
   # These are built from primitive datatypes and can hold multiple values.

   - str        → "Hello", 'Python'
     # represents text data (sequence of characters)

   - list       → [1, 2, 3]
     # ordered, mutable (can be changed) collection

   - tuple      → (1, 2, 3)
     # ordered, immutable (cannot be changed) collection

   - set        → {1, 2, 3}
     # unordered collection of unique elements

   - dict       → {"name": "Faruk", "age": 20}
     # key-value pairs used for mapping data
"""

# =================== Primitive Datatypes Example ===================

num_int = 10            # int → 10, -5, 1000
num_float = 3.14        # float → 3.14, -0.5
is_active = True         # bool → True, False
num_complex = 2 + 3j    # complex → 2+3j
nothing = None          # NoneType → None
data_bytes = b"hello"   # bytes → b"hello"
data_bytearray = bytearray([65, 66, 67])  # bytearray → bytearray([65, 66, 67])
data_memoryview = memoryview(b"hello")    # memoryview → memoryview(b"hello")

print(type(num_int))         # <class 'int'>
print(type(num_float))       # <class 'float'>
print(type(is_active))       # <class 'bool'>
print(type(num_complex))     # <class 'complex'>
print(type(nothing))         # <class 'NoneType'>
print(type(data_bytes))      # <class 'bytes'>
print(type(data_bytearray))  # <class 'bytearray'>
print(type(data_memoryview)) # <class 'memoryview'>


# =================== non-primitive datatypes ===================
# string
str = "Python" # str      → "Hello", 'Python'
# list
lst = [1, 2, 3] # list     → [1, 2, 3]
# tuple
tpl = (1, 2, 3) # tuple    → (1, 2, 3)
# set
st = {"x", "y"} # set      → {1, 2, 3}
# dictionary
dct = {"name": "Faruk", "age": 20} # dict     → {"name": "Faruk", "age": 20}

print(type(str))  # <class 'str'>
print(type(lst))  # <class 'list'>
print(type(tpl))  # <class 'tuple'>
print(type(st))  # <class 'set'>
print(type(dct))  # <class 'dict'>

