"""
# Python Dictionary

## What is a Dictionary?

A **dictionary** is a collection of **key-value pairs** in Python.

Each key is used to access its corresponding value.

### Basic Syntax

```python
student = {
    "name": "Faruk",
    "age": 22,
    "department": "CSE"
}
```

Here:

```text
"name"       → key
"Faruk"      → value

"age"        → key
22           → value
```

---

## Main Characteristics of Dictionary

### 1. Key-Value Pair

A dictionary stores data in the form:

```text
key : value
```

Example:

```python
person = {
    "name": "Faruk",
    "age": 22
}
```

---

### 2. Ordered

Dictionaries preserve **insertion order** in modern Python.

```python
data = {
    "a": 10,
    "b": 20,
    "c": 30
}
```

The order of insertion is maintained.

---

### 3. Mutable / Changeable

A dictionary can be changed after creation.

```python
student = {
    "name": "Faruk",
    "age": 22
}

student["age"] = 23

print(student)
```

Output:

```text
{'name': 'Faruk', 'age': 23}
```

---

### 4. Keys Must Be Unique

A dictionary cannot have duplicate keys.

```python
data = {
    "name": "Faruk",
    "name": "Ahmed"
}

print(data)
```

Output:

```text
{'name': 'Ahmed'}
```

The later value replaces the earlier value.

---

### 5. Values Can Be Duplicated

Dictionary **values** can be duplicate.

```python
data = {
    "a": 10,
    "b": 10,
    "c": 20
}
```

---

### 6. Keys Must Be Hashable

Dictionary keys must be **hashable** objects.

Common valid keys:

```python
data = {
    "name": "Faruk",
    101: "Student",
    (10, 20): "Point"
}
```

Lists cannot be dictionary keys:

```python
# data = {
#     [10, 20]: "value"
# }
# TypeError
```

---

### 7. Values Can Be Any Data Type

Dictionary values can contain different types.

```python
data = {
    "name": "Faruk",
    "age": 22,
    "marks": 85.5,
    "passed": True,
    "subjects": ["Python", "C"]
}
```

---

### 8. Access Using Keys

Dictionary values are accessed using their keys.

```python
student = {
    "name": "Faruk",
    "age": 22
}

print(student["name"])
print(student["age"])
```

Output:

```text
Faruk
22
```

---

### 9. Iterable

A dictionary can be iterated using loops.

```python
student = {
    "name": "Faruk",
    "age": 22
}

for key in student:
    print(key)
```

Output:

```text
name
age
```

---

## One-Line Definition

> **A dictionary is a mutable collection of key-value pairs where keys are unique and hashable, while values can be of any data type.**

"""
