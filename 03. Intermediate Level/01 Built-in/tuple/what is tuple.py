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

## 2. Main Characteristics of Tuple

### 1. Ordered Collection

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

### 2. Indexed

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
```

---

### 3. Immutable

A tuple cannot be modified after it is created.

```python
t = (10, 20, 30)

# t[0] = 100   # TypeError
```

You cannot directly:

* Change an element
* Add an element
* Remove an element

---

### 4. Iterable

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

### 5. Duplicates Allowed

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

### 6. Heterogeneous Data

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
* other objects

---

### 7. Fixed Data

Tuples are useful for storing data that should remain unchanged.

Example:

```python
student = ("Faruk", 101, "CSE")
```

If the data represents a fixed record, a tuple can be appropriate.

---

### 8. Hashable

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

However, a tuple containing a mutable object such as a list is not hashable:

```python
t = ([1, 2], 3)

# hash(t)   # TypeError
```

So, the correct rule is:

> A tuple is hashable only when all of its elements are hashable.

---

### 9. Reference Type

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

### 10. Dynamic Type

Python is dynamically typed, so a variable does not have to be declared as a tuple beforehand.

```python
x = (10, 20)
print(type(x))
```

Output:

```text
<class 'tuple'>
```

The variable can later refer to an object of another type:

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

## 3. Tuple vs List

| Feature                 | Tuple                             | List        |
| ----------------------- | --------------------------------- | ----------- |
| Syntax                  | `()`                              | `[]`        |
| Ordered                 | Yes                               | Yes         |
| Indexed                 | Yes                               | Yes         |
| Mutable                 | No                                | Yes         |
| Duplicates              | Allowed                           | Allowed     |
| Heterogeneous           | Yes                               | Yes         |
| Iterable                | Yes                               | Yes         |
| Can be dictionary key   | Yes, if all elements are hashable | No          |
| Suitable for fixed data | Yes                               | Usually not |

---

## 4. Important Note About Speed

Tuples can have **lower memory overhead** than lists and can sometimes be slightly faster for iteration/access.

However, saying simply:

> "Tuples are always faster than lists"

is not correct.

The main reason to choose a tuple is usually **immutability and representing fixed data**, not just speed.

---

## 5. Summary

A **tuple** is:

* **Ordered**
* **Indexed**
* **Immutable**
* **Iterable**
* **Allows duplicates**
* **Supports heterogeneous data**
* **Useful for fixed data**
* **Potentially hashable**
* **Written using `()`**

### One-Line Definition

> **A tuple is an ordered, immutable, iterable collection in Python that can store duplicate and heterogeneous values.**

"""
