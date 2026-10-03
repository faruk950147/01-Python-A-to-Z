"""
# Python Tuple

## 1. What is a Tuple?

A **tuple** is an **ordered, immutable collection** in Python.

Tuples are generally used to store a group of related values that should **not be changed** after creation.

### Basic Syntax

```python
my_tuple = (10, 20, 30, 40)
```

---

# 2. Main Characteristics of Tuple

## 1. Ordered Collection

Tuple elements maintain a specific order.

```python
t = (10, 20, 30)

print(t)
```

Output:

```text
(10, 20, 30)
```

The order of elements is preserved.

---

## 2. Indexed

Each element has a fixed index.

Indexing starts from `0`.

```python
t = (10, 20, 30)

print(t[0])  # 10
print(t[1])  # 20
print(t[2])  # 30
```

Negative indexing is also supported:

```python
print(t[-1])  # 30
print(t[-2])  # 20
```

Index structure:

```text
Tuple:   (10, 20, 30, 40)
Index:     0   1   2   3
Negative: -4  -3  -2  -1
```

---

## 3. Immutable

A tuple cannot be modified after it is created.

```python
t = (10, 20, 30)

# t[0] = 100
```

This produces:

```text
TypeError: 'tuple' object does not support item assignment
```

You cannot directly:

* Change an element
* Add an element
* Remove an element

However, you can create a **new tuple**:

```python
t = (10, 20, 30)

t = (100, 20, 30)

print(t)
```

Output:

```text
(100, 20, 30)
```

The original tuple was not modified; a new tuple was assigned to the variable.

---

## 4. Iterable

A tuple can be traversed using loops.

```python
t = (10, 20, 30)

for item in t:
    print(item)
```

Output:

```text
10
20
30
```

---

## 5. Duplicates Allowed

A tuple can contain duplicate values.

```python
t = (10, 20, 10, 30, 20)

print(t)
```

Output:

```text
(10, 20, 10, 30, 20)
```

---

## 6. Heterogeneous Data

A tuple can contain different data types.

```python
t = (10, "Python", 3.14, True)

print(t)
```

A tuple can contain:

* `int`
* `float`
* `str`
* `bool`
* `list`
* `dict`
* `set`
* other objects

Example:

```python
student = (
    101,
    "Faruk",
    3.75,
    ["Python", "Django"]
)
```

---

## 7. Fixed Data

Tuples are useful for storing data that should remain unchanged.

```python
student = ("Faruk", 101, "CSE")
```

Examples of suitable tuple data:

```python
coordinates = (23.8103, 90.4125)

rgb = (255, 255, 255)

date = (2026, 10, 3)

point = (10, 20)
```

---

## 8. Hashable

A tuple can be used as a dictionary key **if all of its elements are hashable**.

```python
point = (10, 20)

data = {
    point: "Coordinate"
}

print(data[point])
```

Output:

```text
Coordinate
```

However:

```python
t = ([1, 2], 3)

# hash(t)
```

This produces:

```text
TypeError: unhashable type: 'list'
```

Therefore:

> A tuple is hashable only when all of its elements are hashable.

---

## 9. Reference Type

In Python, a tuple variable holds a **reference to a tuple object**.

```python
a = (10, 20, 30)
b = a

print(a is b)
```

Output:

```text
True
```

Both variables refer to the same tuple object.

---

## 10. Dynamically Typed

Python is dynamically typed.

```python
x = (10, 20)

print(type(x))
```

Output:

```text
<class 'tuple'>
```

The variable can later refer to another type:

```python
x = (10, 20)

x = "Python"

print(x)
```

Output:

```text
Python
```

---

# 3. Creating Tuples

## 1. Using Parentheses

```python
t = (10, 20, 30)
```

---

## 2. Without Parentheses

Python also supports **tuple packing**.

```python
t = 10, 20, 30

print(t)
```

Output:

```text
(10, 20, 30)
```

The commas create the tuple; parentheses are often used for readability.

---

## 3. Empty Tuple

```python
t = ()

print(type(t))
```

Output:

```text
<class 'tuple'>
```

---

## 4. Using `tuple()`

The `tuple()` constructor can create a tuple from an iterable.

```python
t = tuple([10, 20, 30])

print(t)
```

Output:

```text
(10, 20, 30)
```

From a string:

```python
t = tuple("Python")

print(t)
```

Output:

```text
('P', 'y', 't', 'h', 'o', 'n')
```

From a set:

```python
t = tuple({10, 20, 30})

print(t)
```

The order should not be relied upon because sets are unordered collections.

---

# 4. Single-Element Tuple

This is one of the most important tuple rules.

```python
t = (10,)

print(type(t))
```

Output:

```text
<class 'tuple'>
```

The comma is important.

### Wrong

```python
t = (10)

print(type(t))
```

Output:

```text
<class 'int'>
```

Why?

```python
(10)
```

is just a parenthesized integer.

But:

```python
(10,)
```

is a tuple.

### Rule

> For a single-element tuple, a trailing comma is required.

```python
single = (10,)
```

---

# 5. Tuple Indexing

```python
t = ("Python", "Django", "FastAPI")

print(t[0])
print(t[1])
print(t[2])
```

Output:

```text
Python
Django
FastAPI
```

### Negative Indexing

```python
print(t[-1])
print(t[-2])
```

Output:

```text
FastAPI
Django
```

---

# 6. Tuple Slicing

Tuple slicing follows the same syntax as lists.

```python
t = (10, 20, 30, 40, 50)

print(t[1:4])
```

Output:

```text
(20, 30, 40)
```

### Syntax

```python
tuple[start:stop:step]
```

Examples:

```python
t = (10, 20, 30, 40, 50)

print(t[:3])
print(t[2:])
print(t[::2])
print(t[::-1])
```

Output:

```text
(10, 20, 30)
(30, 40, 50)
(10, 30, 50)
(50, 40, 30, 20, 10)
```

---

# 7. Tuple Length

Use `len()`:

```python
t = (10, 20, 30, 40)

print(len(t))
```

Output:

```text
4
```

---

# 8. Iterating Over a Tuple

## Simple Loop

```python
t = (10, 20, 30)

for value in t:
    print(value)
```

---

## Using Index

```python
t = ("A", "B", "C")

for i in range(len(t)):
    print(i, t[i])
```

Output:

```text
0 A
1 B
2 C
```

---

## Using `enumerate()`

Usually cleaner:

```python
t = ("A", "B", "C")

for index, value in enumerate(t):
    print(index, value)
```

Output:

```text
0 A
1 B
2 C
```

---

# 9. Membership Testing

Use `in` and `not in`.

```python
t = (10, 20, 30)

print(20 in t)
print(50 in t)
```

Output:

```text
True
False
```

```python
print(50 not in t)
```

Output:

```text
True
```

---

# 10. Tuple Concatenation

Tuples can be joined using `+`.

```python
a = (1, 2)
b = (3, 4)

c = a + b

print(c)
```

Output:

```text
(1, 2, 3, 4)
```

Remember:

> Because tuples are immutable, concatenation creates a new tuple.

---

# 11. Tuple Repetition

Use `*`.

```python
t = (1, 2)

print(t * 3)
```

Output:

```text
(1, 2, 1, 2, 1, 2)
```

---

# 12. Tuple Comparison

Tuples can be compared using:

```python
==
!=
<
>
<=
>=
```

Example:

```python
a = (1, 2, 3)
b = (1, 2, 3)

print(a == b)
```

Output:

```text
True
```

Tuple comparisons are generally performed **lexicographically**, meaning Python compares elements from left to right.

```python
a = (1, 5)
b = (2, 1)

print(a < b)
```

Output:

```text
True
```

Because Python first compares `1` and `2`.

---

# 13. Tuple Methods

Tuples have only two main built-in methods.

## 1. `count()`

Counts how many times a value occurs.

```python
t = (10, 20, 10, 30, 10)

print(t.count(10))
```

Output:

```text
3
```

---

## 2. `index()`

Returns the index of the first occurrence.

```python
t = (10, 20, 30, 20)

print(t.index(20))
```

Output:

```text
1
```

If the value does not exist:

```python
t = (10, 20, 30)

# t.index(50)
```

This raises:

```text
ValueError
```

---

# 14. Useful Built-in Functions

Tuples work with many Python built-in functions.

```python
t = (10, 20, 30, 40)
```

### `len()`

```python
len(t)
```

### `min()`

```python
min(t)
```

### `max()`

```python
max(t)
```

### `sum()`

```python
sum(t)
```

### `sorted()`

```python
t = (30, 10, 20)

result = sorted(t)

print(result)
```

Output:

```text
[10, 20, 30]
```

Important:

> `sorted()` returns a **list**, not a tuple.

If you need a tuple:

```python
result = tuple(sorted(t))

print(result)
```

Output:

```text
(10, 20, 30)
```

---

# 15. Tuple Packing

When multiple values are assigned to one variable, Python can pack them into a tuple.

```python
student = "Faruk", 101, "CSE"

print(student)
```

Output:

```text
('Faruk', 101, 'CSE')
```

This is called:

> **Tuple Packing**

---

# 16. Tuple Unpacking

Tuple unpacking extracts values into separate variables.

```python
student = ("Faruk", 101, "CSE")

name, student_id, department = student

print(name)
print(student_id)
print(department)
```

Output:

```text
Faruk
101
CSE
```

The number of variables must normally match the number of elements.

```python
t = (10, 20, 30)

# a, b = t
```

This raises:

```text
ValueError
```

because there are 3 values but only 2 variables.

---

# 17. Extended Tuple Unpacking

Python supports `*` during unpacking.

```python
t = (10, 20, 30, 40, 50)

a, *b = t

print(a)
print(b)
```

Output:

```text
10
[20, 30, 40, 50]
```

Notice that `b` becomes a **list**.

Another example:

```python
a, *middle, b = (10, 20, 30, 40, 50)

print(a)
print(middle)
print(b)
```

Output:

```text
10
[20, 30, 40]
50
```

---

# 18. Swapping Variables Using Tuple Unpacking

Python allows elegant variable swapping:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

This works through tuple packing and unpacking.

Conceptually:

```python
a, b = (b, a)
```

---

# 19. Nested Tuples

A tuple can contain another tuple.

```python
t = (
    (1, 2),
    (3, 4),
    (5, 6)
)

print(t[0])
print(t[0][1])
```

Output:

```text
(1, 2)
2
```

Nested tuples are useful for representing structured data.

Example:

```python
points = (
    (10, 20),
    (30, 40),
    (50, 60)
)
```

---

# 20. Tuple Containing Mutable Objects

A tuple itself is immutable, but it can contain mutable objects.

```python
t = ([1, 2], [3, 4])

t[0].append(5)

print(t)
```

Output:

```text
([1, 2, 5], [3, 4])
```

This is possible because the tuple's references cannot be changed, but the list object referenced by the tuple is mutable.

Important distinction:

```text
Tuple
 ├── reference → List 1
 └── reference → List 2
```

The tuple structure is immutable, but the referenced list can change.

### However

This is not allowed:

```python
# t[0] = [100, 200]
```

because that tries to replace the tuple element itself.

---

# 21. Immutability Does Not Mean Deeply Immutable

Consider:

```python
t = ([1, 2], 10)

t[0].append(3)

print(t)
```

Output:

```text
([1, 2, 3], 10)
```

Therefore:

> Tuple immutability applies to the tuple's own elements/references, not necessarily to the internal state of mutable objects stored inside it.

This is an important interview concept.

---

# 22. Tuple and `del`

You cannot delete an individual tuple element:

```python
t = (10, 20, 30)

# del t[0]
```

This raises an error.

But you can delete the entire tuple variable:

```python
t = (10, 20, 30)

del t
```

After that:

```python
# print(t)
```

would raise:

```text
NameError
```

---

# 23. Tuple Copying

Because tuples are immutable, copying is usually simpler than copying a mutable list.

```python
a = (10, 20, 30)
b = a

print(a is b)
```

Output:

```text
True
```

If you create another tuple with the same contents, identity is a separate concept from equality:

```python
a = (10, 20, 30)
b = tuple([10, 20, 30])

print(a == b)
```

Output:

```text
True
```

`==` checks value equality.

`is` checks object identity.

---

# 24. Tuple Comprehension?

Python does **not** have a dedicated tuple comprehension syntax.

For example:

```python
# This is NOT a tuple comprehension
result = (x * 2 for x in range(5))
```

This creates a **generator expression**, not a tuple.

```python
print(type(result))
```

Output:

```text
<class 'generator'>
```

To create a tuple:

```python
result = tuple(x * 2 for x in range(5))

print(result)
```

Output:

```text
(0, 2, 4, 6, 8)
```

---

# 25. Converting Between List and Tuple

## Tuple → List

```python
t = (10, 20, 30)

lst = list(t)

print(lst)
```

Output:

```text
[10, 20, 30]
```

---

## List → Tuple

```python
lst = [10, 20, 30]

t = tuple(lst)

print(t)
```

Output:

```text
(10, 20, 30)
```

This is useful when you need to temporarily modify data and then store it as an immutable sequence.

---

# 26. String → Tuple

```python
text = "Python"

t = tuple(text)

print(t)
```

Output:

```text
('P', 'y', 't', 'h', 'o', 'n')
```

---

# 27. Tuple → String

For a tuple of strings:

```python
t = ("Python", "Django", "API")

text = " ".join(t)

print(text)
```

Output:

```text
Python Django API
```

Another example:

```python
text = "-".join(t)

print(text)
```

Output:

```text
Python-Django-API
```

---

# 28. Tuple as Dictionary Key

A tuple is useful as a dictionary key when all its elements are hashable.

```python
locations = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}

print(locations[(10, 20)])
```

Output:

```text
Point A
```

This is especially useful for:

* Coordinates
* Graph nodes
* Grid positions
* Memoization keys
* State representation in algorithms

Example:

```python
visited = set()

visited.add((2, 3))
visited.add((4, 5))

print(visited)
```

A coordinate tuple can therefore represent a grid cell.

---

# 29. Tuple for Multiple Return Values

Python functions can return multiple values using a tuple.

```python
def get_student():
    return "Faruk", 101, "CSE"


student = get_student()

print(student)
```

Output:

```text
('Faruk', 101, 'CSE')
```

You can unpack the result:

```python
name, student_id, department = get_student()

print(name)
print(student_id)
print(department)
```

This is very common in Python.

---

# 30. Tuple vs List

| Feature                 | Tuple                        | List        |
| ----------------------- | ---------------------------- | ----------- |
| Syntax                  | `()`                         | `[]`        |
| Ordered                 | Yes                          | Yes         |
| Indexed                 | Yes                          | Yes         |
| Mutable                 | No                           | Yes         |
| Duplicates              | Allowed                      | Allowed     |
| Heterogeneous           | Yes                          | Yes         |
| Iterable                | Yes                          | Yes         |
| Hashable                | If all elements are hashable | No          |
| Methods                 | Few                          | Many        |
| Suitable for fixed data | Yes                          | Usually not |
| Can be dictionary key   | Sometimes                    | No          |

### When should you use a Tuple?

Use a tuple when:

* Data should not be changed.
* You are representing a fixed record.
* You need a hashable composite value.
* You want to return multiple values from a function.
* You are representing coordinates or states.

### When should you use a List?

Use a list when:

* Data needs to change.
* Elements need to be added or removed.
* You need methods such as `append()`, `extend()`, `insert()`, `remove()`, etc.

---

# 31. Tuple vs Set

| Feature      | Tuple          | Set                         |
| ------------ | -------------- | --------------------------- |
| Ordered      | Yes            | No indexing/order guarantee |
| Indexed      | Yes            | No                          |
| Mutable      | No             | Yes                         |
| Duplicates   | Allowed        | Not allowed                 |
| Hashable     | Sometimes      | No                          |
| Main purpose | Fixed sequence | Unique elements             |

Example:

```python
t = (1, 2, 2, 3)

s = {1, 2, 2, 3}

print(t)
print(s)
```

Output:

```text
(1, 2, 2, 3)
{1, 2, 3}
```

---

# 32. Tuple Performance

Tuples can have lower memory overhead than lists and can sometimes be slightly faster for iteration/access.

However, it is incorrect to say:

> "Tuples are always faster than lists."

The primary reason for choosing a tuple is usually:

**immutability + fixed structure**

rather than raw performance.

---

# 33. Time Complexity

For a tuple containing `n` elements:

| Operation           | Average Complexity |
| ------------------- | -----------------: |
| Index access `t[i]` |               O(1) |
| Update              |      Not supported |
| `len(t)`            |               O(1) |
| Membership `x in t` |               O(n) |
| `count(x)`          |               O(n) |
| `index(x)`          |               O(n) |
| Iteration           |               O(n) |
| Slicing             |               O(k) |
| Concatenation       |           O(n + m) |
| Repetition          |           O(n × k) |

Here:

* `n` = size of first tuple
* `m` = size of second tuple
* `k` = number of repeated copies
* `k` in slicing means the size of the resulting slice

---

# 34. Common Tuple Mistakes

## Mistake 1: Forgetting the comma

Wrong:

```python
x = (10)

print(type(x))
```

Output:

```text
<class 'int'>
```

Correct:

```python
x = (10,)

print(type(x))
```

Output:

```text
<class 'tuple'>
```

---

## Mistake 2: Trying to modify a tuple

```python
t = (10, 20, 30)

# t[0] = 100
```

Tuples are immutable.

---

## Mistake 3: Expecting `sorted()` to return a tuple

```python
t = (30, 10, 20)

result = sorted(t)

print(type(result))
```

Output:

```text
<class 'list'>
```

Convert it if necessary:

```python
result = tuple(sorted(t))
```

---

## Mistake 4: Confusing `is` and `==`

```python
a = (1, 2)
b = (1, 2)

print(a == b)
```

`==` checks values.

```python
print(a is b)
```

`is` checks object identity.

Do not use `is` when you simply want to compare values.

---

# 35. Tuple in DSA

Tuples are very useful in Data Structures and Algorithms.

## 1. Coordinate Representation

```python
point = (x, y)
```

Example:

```python
point = (3, 5)
```

---

## 2. Grid Problems

```python
visited = set()

visited.add((2, 3))
```

Here:

```text
(row, column)
```

represents a grid position.

---

## 3. Graph Problems

A tuple can represent an edge:

```python
edge = (u, v)
```

Weighted edge:

```python
edge = (u, v, weight)
```

---

## 4. Priority Queue

Tuples are commonly used with `heapq`.

```python
import heapq

heap = []

heapq.heappush(heap, (5, "Task A"))
heapq.heappush(heap, (1, "Task B"))
heapq.heappush(heap, (3, "Task C"))

print(heapq.heappop(heap))
```

Output:

```text
(1, 'Task B')
```

The first tuple element can represent priority.

---

## 5. Memoization

Tuples can be used as dictionary keys.

```python
memo = {}

state = (2, 5)

memo[state] = 100
```

This is useful for dynamic programming states when the state components are hashable.

---

# 36. Useful Tuple Patterns

## Pattern 1: First and Last Element

```python
t = (10, 20, 30, 40, 50)

first = t[0]
last = t[-1]
```

---

## Pattern 2: Reverse a Tuple

```python
t = (1, 2, 3, 4)

reverse = t[::-1]

print(reverse)
```

Output:

```text
(4, 3, 2, 1)
```

---

## Pattern 3: Remove Duplicates

A tuple itself allows duplicates.

To create a tuple containing unique values:

```python
t = (1, 2, 2, 3, 3, 4)

unique = tuple(set(t))

print(unique)
```

However, this does **not preserve the original order** reliably.

If order must be preserved:

```python
t = (1, 2, 2, 3, 3, 4)

unique = tuple(dict.fromkeys(t))

print(unique)
```

Output:

```text
(1, 2, 3, 4)
```

---

# 37. Nested Tuple Unpacking

```python
student = ("Faruk", (101, "CSE"))

name, (student_id, department) = student

print(name)
print(student_id)
print(department)
```

Output:

```text
Faruk
101
CSE
```

This is useful when working with structured data.

---

# 38. Tuple with `zip()`

`zip()` commonly produces tuples.

```python
names = ["Faruk", "Rahim", "Karim"]
marks = [90, 85, 80]

result = zip(names, marks)

print(list(result))
```

Output:

```text
[('Faruk', 90), ('Rahim', 85), ('Karim', 80)]
```

Each pair is represented as a tuple.

---

# 39. Tuple with `enumerate()`

`enumerate()` also produces pairs that can be unpacked like tuples.

```python
names = ("Faruk", "Rahim", "Karim")

for index, name in enumerate(names):
    print(index, name)
```

Output:

```text
0 Faruk
1 Rahim
2 Karim
```

---

# 40. Tuple Methods vs Common Functions

### Tuple methods

| Method    | Purpose               |
| --------- | --------------------- |
| `count()` | Count occurrences     |
| `index()` | Find first occurrence |

### Useful built-in functions

| Function   | Purpose                               |
| ---------- | ------------------------------------- |
| `len()`    | Number of elements                    |
| `min()`    | Minimum value                         |
| `max()`    | Maximum value                         |
| `sum()`    | Sum numeric values                    |
| `sorted()` | Return sorted list                    |
| `tuple()`  | Convert iterable to tuple             |
| `list()`   | Convert tuple to list                 |
| `any()`    | Check whether any element is truthy   |
| `all()`    | Check whether all elements are truthy |

Example:

```python
t = (True, True, False)

print(any(t))
print(all(t))
```

Output:

```text
True
False
```

---

# 41. Important Tuple Concepts for Interviews

### Q1. Is a tuple mutable?

No.

A tuple is immutable.

---

### Q2. Can a tuple contain a list?

Yes.

```python
t = ([1, 2], 10)
```

The list itself remains mutable.

---

### Q3. Can a tuple be a dictionary key?

Yes, if all tuple elements are hashable.

```python
d = {
    (1, 2): "value"
}
```

---

### Q4. Why does `(10)` not create a tuple?

Because parentheses alone do not create a tuple.

```python
(10)
```

is an integer expression.

A comma is required:

```python
(10,)
```

---

### Q5. How many methods does a tuple have?

Two main tuple-specific methods:

```python
count()
index()
```

---

### Q6. Can we change a tuple?

Not directly.

You can create a new tuple:

```python
t = (1, 2, 3)

t = (10, 2, 3)
```

---

### Q7. What is tuple unpacking?

Assigning tuple elements to multiple variables:

```python
a, b, c = (10, 20, 30)
```

---

### Q8. Can a tuple contain different data types?

Yes.

```python
t = (10, "Python", 3.14, True)
```

---

### Q9. What is tuple packing?

Combining multiple values into a tuple:

```python
t = 10, 20, 30
```

---

### Q10. What is the difference between `==` and `is`?

```python
==   → value equality
is   → object identity
```

---

# 42. Tuple Cheat Sheet

```python
# Create
t = (10, 20, 30)

# Empty tuple
t = ()

# Single-element tuple
t = (10,)

# Without parentheses
t = 10, 20, 30

# Constructor
t = tuple([10, 20, 30])

# Indexing
t[0]
t[-1]

# Slicing
t[1:3]
t[::-1]

# Length
len(t)

# Membership
10 in t
10 not in t

# Iteration
for x in t:
    print(x)

# Count
t.count(10)

# Index
t.index(20)

# Concatenation
a + b

# Repetition
t * 3

# Reverse
t[::-1]

# Tuple → List
list(t)

# List → Tuple
tuple([1, 2, 3])

# Packing
t = 10, 20, 30

# Unpacking
a, b, c = t

# Extended unpacking
a, *middle, b = t

# Swap
a, b = b, a

# Dictionary key
d = {(10, 20): "Point"}

# Set element
s = {(10, 20)}

# Multiple return values
def func():
    return 10, 20
```

---

# 43. Final Summary

A **tuple** is an:

* **Ordered** collection
* **Indexed** collection
* **Immutable** collection
* **Iterable** collection
* Collection that **allows duplicates**
* Collection that supports **heterogeneous data**
* Potentially **hashable** object
* Useful structure for **fixed data**
* Useful for **coordinates and DSA states**
* Useful for **multiple return values**
* Useful as a **dictionary key** when all elements are hashable

### One-Line Definition

> **A tuple is an ordered, immutable, iterable collection in Python that can store duplicate and heterogeneous values.**

### Most Important Tuple Rules

```text
Tuple → Ordered
Tuple → Indexed
Tuple → Immutable
Tuple → Duplicates allowed
Tuple → Heterogeneous
Tuple → Can be hashable
Tuple → () syntax
Single tuple → (10,)
Tuple methods → count(), index()
Packing → a = 10, 20
Unpacking → a, b = (10, 20)
```

### Tuple vs List — Remember

```text
Need modification?
        |
   +----+----+
   |         |
  Yes        No
   |         |
 List       Tuple
```

Use **List** for changing collections.

Use **Tuple** for fixed/immutable collections.

"""