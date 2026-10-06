"""
# Python Datatypes

## What is a Data Type?

In Python, a **data type** tells us what kind of value a variable stores.

Example:

```python
age = 20
name = "Faruk"
price = 3.14
is_active = True
```

Here:

```text
20       → int
"Faruk"  → str
3.14     → float
True     → bool
```

### Python is Dynamically Typed

Python is a **dynamically typed language**.

This means we do not need to declare the data type of a variable manually. Python automatically determines the type from the assigned value.

```python
x = 10
print(type(x))
```

Output:

```text
<class 'int'>
```

The same variable can later store another type:

```python
x = "Python"
print(type(x))
```

Output:

```text
<class 'str'>
```

---

# 1. Primitive Datatypes

Primitive datatypes are basic/simple data types used to represent individual values.

In this note, we will keep the following types under Primitive Datatypes:

```text
int
float
complex
bool
NoneType
bytes
bytearray
memoryview
```

---

## 1.1 Integer (`int`)

`int` is used for **whole numbers**.

Examples:

```python
num_int = 10
num_int = -5
num_int = 1000
```

Python integers can be very large. Their size is mainly limited by available memory.

```python
big_number = 123456789012345678901234567890

print(big_number)
print(type(big_number))
```

Output:

```text
123456789012345678901234567890
<class 'int'>
```

### Binary Number

A binary number also belongs to the `int` type.

Use `0b` before a binary number:

```python
a = 0b1101

print(a)
print(type(a))
```

Output:

```text
13
<class 'int'>
```

Because:

```text
1101₂ = 13₁₀
```

---

## 1.2 Float (`float`)

`float` is used for **decimal numbers**.

Examples:

```python
num_float = 3.14
num_float = -0.5
num_float = 1.0
```

Example:

```python
num_float = 3.14

print(type(num_float))
```

Output:

```text
<class 'float'>
```

### Scientific Notation

Python also supports scientific notation.

```python
x = 1e10
print(x)
```

Output:

```text
10000000000.0
```

Another example:

```python
x = 1e-10
print(x)
```

Output:

```text
1e-10
```

### Float Precision

Python's normal `float` usually uses 64-bit floating-point representation.

It provides approximately **15–17 significant decimal digits** of precision.

Its approximate range is:

```text
±1.8 × 10^308
```

Example:

```python
x = 3.14

print(type(x))
print(x)
```

Output:

```text
<class 'float'>
3.14
```

---

## 1.3 Complex (`complex`)

A complex number has:

```text
real part + imaginary part
```

Python uses `j` for the imaginary part.

Syntax:

```text
a + bj
```

Example:

```python
complex_num = 1 + 2j

print(type(complex_num))
print(complex_num)
```

Output:

```text
<class 'complex'>
(1+2j)
```

Other examples:

```python
complex_num = 1 - 2j
print(complex_num)

complex_num = 1j
print(complex_num)

complex_num = 5 + 10j
print(complex_num)
```

### Real and Imaginary Parts

```python
num = 3 + 4j

print(num.real)
print(num.imag)
```

Output:

```text
3.0
4.0
```

So:

```text
3 + 4j

3 → real part
4 → imaginary part
```

---

# 1.4 Boolean (`bool`)

Boolean is a logical data type.

It has only two values:

```text
True
False
```

Example:

```python
is_active = True

print(type(is_active))
print(is_active)
```

Output:

```text
<class 'bool'>
True
```

Another example:

```python
is_active = False

print(type(is_active))
print(is_active)
```

Output:

```text
<class 'bool'>
False
```

### True and False

In Python:

```text
True  → behaves like 1
False → behaves like 0
```

Example:

```python
print(True == 1)
print(False == 0)
```

Output:

```text
True
True
```

But:

```python
print(type(True))
print(type(1))
```

Output:

```text
<class 'bool'>
<class 'int'>
```

So `True` is `bool`, while `1` is `int`.

---

# 1.5 Truthy and Falsy Values

Python values can behave like `True` or `False` in conditions.

Common **Falsy** values are:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

Example:

```python
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
```

Output:

```text
False
False
False
False
False
False
False
```

Most other values are **Truthy**.

```python
print(bool(1))
print(bool(2))
print(bool("Python"))
print(bool([1, 2, 3]))
```

Output:

```text
True
True
True
True
```

### Important

```text
0        → False
1        → True
2        → True
-1       → True
""       → False
"Python" → True
```

---

# 1.6 NoneType (`None`)

`NoneType` represents the **absence of a value**.

It has only one value:

```text
None
```

Example:

```python
name = None

print(type(name))
print(name)
```

Output:

```text
<class 'NoneType'>
None
```

`None` is commonly used when:

* a value is not available
* a value has not been assigned yet
* a function does not return a useful value

Example:

```python
name = None

if name is None:
    print("Name is not available")
```

Output:

```text
Name is not available
```

### Important

`None` is different from:

```text
0
""
False
```

For example:

```python
print(None == 0)
print(None == "")
print(None == False)
```

Output:

```text
False
False
False
```

---

# 1.7 Bytes (`bytes`)

`bytes` represents an **immutable sequence of bytes**.

Example:

```python
data_bytes = b"hello"

print(type(data_bytes))
print(data_bytes)
```

Output:

```text
<class 'bytes'>
b'hello'
```

Bytes are commonly used for:

* files
* network communication
* images
* binary data
* encoded text

### Important

`bytes` is **immutable**.

That means its contents cannot be changed after creation.

---

# 1.8 Bytearray (`bytearray`)

`bytearray` represents a **mutable sequence of bytes**.

Example:

```python
data_bytearray = bytearray([65, 66, 67])

print(type(data_bytearray))
print(data_bytearray)
```

Output:

```text
<class 'bytearray'>
bytearray(b'ABC')
```

Unlike `bytes`, a `bytearray` can be changed.

```python
data = bytearray([65, 66, 67])

data[0] = 90

print(data)
```

Output:

```text
bytearray(b'ZBC')
```

### Difference

```text
bytes      → immutable
bytearray  → mutable
```

---

# 1.9 Memoryview (`memoryview`)

`memoryview` provides a view of a bytes-like object.

It can be useful when working with binary data without unnecessarily copying the data.

Example:

```python
data_memoryview = memoryview(b"hello")

print(type(data_memoryview))
print(data_memoryview)
```

Output:

```text
<class 'memoryview'>
<memory at ...>
```

Simple idea:

```text
bytes-like object
       ↓
   memoryview
       ↓
view/access the data
```

---

# Primitive Datatypes Example

```python
num_int = 10
num_float = 3.14
is_active = True
num_complex = 2 + 3j
nothing = None

data_bytes = b"hello"
data_bytearray = bytearray([65, 66, 67])
data_memoryview = memoryview(b"hello")

print(type(num_int))
print(type(num_float))
print(type(is_active))
print(type(num_complex))
print(type(nothing))
print(type(data_bytes))
print(type(data_bytearray))
print(type(data_memoryview))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'complex'>
<class 'NoneType'>
<class 'bytes'>
<class 'bytearray'>
<class 'memoryview'>
```

---

# 2. Non-Primitive Datatypes

Non-primitive datatypes are used to store **multiple values or structured data**.

In this note, we will keep:

```text
str
list
tuple
set
dict
```

---

# 2.1 String (`str`)

A string represents **text data**.

A string is a sequence of characters.

Example:

```python
single_quoted = 'Hello'
double_quoted = "Hello"
triple_quoted = """Hello"""
```

All are strings.

```python
print(type(single_quoted))
print(type(double_quoted))
print(type(triple_quoted))
```

Output:

```text
<class 'str'>
<class 'str'>
<class 'str'>
```

### Triple-Quoted String

Triple quotes can also be used for multiline text:

```python
text = """Hello
Python
World"""
```

---

# String Length

Use `len()` to find the length of a string.

```python
text = "Hello"

print(len(text))
```

Output:

```text
5
```

Because:

```text
H e l l o
```

There are 5 characters.

---

# String Positive Indexing

Python uses **zero-based indexing**.

```text
H   e   l   l   o
0   1   2   3   4
```

Example:

```python
text = "Hello"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
```

Output:

```text
H
e
l
l
o
```

---

# String Negative Indexing

Python also supports negative indexing.

```text
H   e   l   l   o
-5  -4  -3  -2  -1
```

Example:

```python
text = "Hello"

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-4])
print(text[-5])
```

Output:

```text
o
l
l
e
H
```

---

# String Slicing

Slicing is used to get a part of a string.

Syntax:

```python
string[start:end]
```

The `start` index is included.

The `end` index is excluded.

Example:

```python
text = "Hello"

substring = text[0:2]

print(substring)
```

Output:

```text
He
```

Because:

```text
H   e   l   l   o
0   1   2   3   4
↑       ↑
start   end
```

Index `0` is included.

Index `2` is excluded.

---

## More String Slicing Examples

```python
text = "Hello"

print(text[0:1])  # H
print(text[1:2])  # e
print(text[2:3])  # l
print(text[3:4])  # l
print(text[4:5])  # o
```

---

# 2.2 List (`list`)

A list is an **ordered and mutable collection**.

Example:

```python
lst = [1, 2, 3]

print(type(lst))
```

Output:

```text
<class 'list'>
```

A list can store different types of values:

```python
data = [10, "Python", 3.14, True]
```

### List is Mutable

We can change list elements.

```python
lst = [1, 2, 3]

lst[0] = 100

print(lst)
```

Output:

```text
[100, 2, 3]
```

---

# 2.3 Tuple (`tuple`)

A tuple is an **ordered and immutable collection**.

Example:

```python
tpl = (1, 2, 3)

print(type(tpl))
```

Output:

```text
<class 'tuple'>
```

Tuple values cannot normally be changed after creation.

```python
tpl = (1, 2, 3)

# tpl[0] = 100
```

This would produce an error because tuples are immutable.

### Tuple

```text
Ordered   → Yes
Mutable   → No
Duplicates → Allowed
```

---

# 2.4 Set (`set`)

A set is a collection of **unique elements**.

Example:

```python
st = {1, 2, 3}

print(type(st))
```

Output:

```text
<class 'set'>
```

A set automatically removes duplicate values.

```python
st = {1, 2, 2, 3, 3}

print(st)
```

Result:

```text
{1, 2, 3}
```

### Important

A set does not support normal index-based access like a list.

```python
st = {10, 20, 30}

# st[0]  ❌
```

Do not depend on a set's iteration order.

---

# 2.5 Dictionary (`dict`)

A dictionary stores data as **key-value pairs**.

Example:

```python
dct = {
    "name": "Faruk",
    "age": 20
}
```

Here:

```text
"name" → key
"Faruk" → value

"age" → key
20 → value
```

Access a value using its key:

```python
print(dct["name"])
```

Output:

```text
Faruk
```

Check the type:

```python
print(type(dct))
```

Output:

```text
<class 'dict'>
```

---

# Non-Primitive Datatypes Example

```python
str_data = "Python"

lst = [1, 2, 3]

tpl = (1, 2, 3)

st = {"x", "y"}

dct = {
    "name": "Faruk",
    "age": 20
}

print(type(str_data))
print(type(lst))
print(type(tpl))
print(type(st))
print(type(dct))
```

Output:

```text
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
```

---

# Primitive vs Non-Primitive

| Primitive    | Non-Primitive |
| ------------ | ------------- |
| `int`        | `str`         |
| `float`      | `list`        |
| `complex`    | `tuple`       |
| `bool`       | `set`         |
| `NoneType`   | `dict`        |
| `bytes`      |               |
| `bytearray`  |               |
| `memoryview` |               |

---

# Mutable vs Immutable

Another important classification is **mutable** and **immutable**.

## Immutable

These objects cannot be changed after creation.

Common examples:

```text
int
float
complex
bool
NoneType
str
tuple
bytes
```

## Mutable

These objects can be changed.

Common examples:

```text
list
set
dict
bytearray
```

---

# Checking Data Type

Use `type()`:

```python
x = 10

print(type(x))
```

Output:

```text
<class 'int'>
```

Another example:

```python
x = "Python"

print(type(x))
```

Output:

```text
<class 'str'>
```

---

# Type Conversion

Python allows us to convert values from one type to another when possible.

### String to Integer

```python
x = int("10")

print(x)
print(type(x))
```

Output:

```text
10
<class 'int'>
```

### String to Float

```python
x = float("3.14")

print(x)
```

Output:

```text
3.14
```

### Number to String

```python
x = str(100)

print(x)
print(type(x))
```

Output:

```text
100
<class 'str'>
```

### Convert to Boolean

```python
print(bool(0))
print(bool(1))
```

Output:

```text
False
True
```

---

# `type()` vs `isinstance()`

### `type()`

Checks the exact type.

```python
x = True

print(type(x))
```

Output:

```text
<class 'bool'>
```

### `isinstance()`

Checks whether an object is an instance of a type, including subclasses.

```python
x = True

print(isinstance(x, bool))
print(isinstance(x, int))
```

Output:

```text
True
True
```

This happens because `bool` is a subclass of `int`.

---

# Important Note About Variable Names

Do not use built-in type names as variable names.

Avoid:

```python
str = "Python"
int = 10
float = 3.14
list = [1, 2, 3]
```

These names already have special meanings in Python.

Better:

```python
text = "Python"
number = 10
price = 3.14
numbers = [1, 2, 3]
```

---

# Quick Revision

## Primitive Datatypes

```text
int
float
complex
bool
NoneType
bytes
bytearray
memoryview
```

### `int`

```text
Whole numbers
Example: 10, -5, 1000
```

### `float`

```text
Decimal numbers
Example: 3.14, -0.5
```

### `complex`

```text
Real + imaginary
Example: 2 + 3j
```

### `bool`

```text
True / False
```

### `NoneType`

```text
None
```

### `bytes`

```text
Immutable binary data
```

### `bytearray`

```text
Mutable binary data
```

### `memoryview`

```text
View of a bytes-like object
```

---

# Non-Primitive Datatypes

```text
str
list
tuple
set
dict
```

### `str`

```text
Text
Example: "Python"
```

### `list`

```text
Ordered + Mutable
Example: [1, 2, 3]
```

### `tuple`

```text
Ordered + Immutable
Example: (1, 2, 3)
```

### `set`

```text
Unique elements
Example: {1, 2, 3}
```

### `dict`

```text
Key-value pairs
Example: {"name": "Faruk"}
```

---

# Interview Questions

### 1. What is a data type?

A data type tells us what kind of value an object contains.

### 2. Is Python dynamically typed?

Yes. Python is dynamically typed.

### 3. What are the Primitive Datatypes in this classification?

```text
int
float
complex
bool
NoneType
bytes
bytearray
memoryview
```

### 4. What are the Non-Primitive Datatypes in this classification?

```text
str
list
tuple
set
dict
```

### 5. What is the difference between list and tuple?

```text
list  → mutable
tuple → immutable
```

### 6. What is the difference between bytes and bytearray?

```text
bytes     → immutable
bytearray → mutable
```

### 7. What is `None`?

`None` represents the absence of a value.

### 8. What is a set?

A set is a collection of unique elements.

### 9. What is a dictionary?

A dictionary stores data as key-value pairs.

### 10. How do you check the type of a variable?

Use:

```python
type(variable)
```

### 11. Can a variable change its type in Python?

Yes.

```python
x = 10
x = "Python"
```

### 12. What is the difference between mutable and immutable?

```text
Mutable   → can be changed
Immutable → cannot be changed
```

---

# Final Summary

```text
                  Python Datatypes
                         |
          ┌──────────────┴──────────────┐
          |                             |
     Primitive                    Non-Primitive
          |                             |
   ┌──────┼──────┐              ┌───────┼───────┐
   |      |      |              |       |       |
  int   float  complex         str     list    tuple
   |      |      |                       |       |
  bool  NoneType bytes                  set     dict
                 |
          bytearray
                 |
          memoryview
```

### Easy Memory Trick

```text
Primitive:

int
float
complex
bool
NoneType
bytes
bytearray
memoryview
```

```text
Non-Primitive:

str
list
tuple
set
dict
```

The most important concepts are:

```text
Python → Dynamically Typed

int       → Whole number
float     → Decimal number
complex   → Complex number
bool      → True / False
None      → No value

str       → Text
list      → Ordered + Mutable
tuple     → Ordered + Immutable
set       → Unique values
dict      → Key-value pairs

bytes     → Immutable bytes
bytearray → Mutable bytes
```

"""