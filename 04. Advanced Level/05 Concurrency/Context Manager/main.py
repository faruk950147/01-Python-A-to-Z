"""
# Python Context Manager

## 1. What is a Context Manager?

A **Context Manager** is a Python feature used to **manage resources safely and automatically**.

It makes sure that a resource is:

1. Opened or acquired before use.
2. Used inside a specific block.
3. Properly closed or released after use.

A Context Manager is usually used with the **`with` statement**.

### Basic Syntax

```python
with expression as variable:
    # use the resource
```

### Example

```python
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
```

Here:

```text
open() → opens the file
with   → manages the file
read() → reads the file
exit   → file is automatically closed
```

We do not need to manually write:

```python
file.close()
```

---

# 2. Why Do We Use Context Managers?

Without a Context Manager:

```python
file = open("file.txt", "r")

data = file.read()

file.close()
```

The problem is that if an error happens before `file.close()`, the file may remain open.

With a Context Manager:

```python
with open("file.txt", "r") as file:
    data = file.read()
```

Python automatically handles the cleanup.

### Main Benefits

```text
Context Manager
      │
      ├── Setup / acquire resource
      ├── Use resource
      ├── Automatic cleanup
      └── Cleanup even if an exception occurs
```

### Common Resources

Context Managers can manage:

```text
File
Database Connection
Network Connection
Lock
Socket
Temporary Resource
```

---

# 3. Python `open()` and File Modes

The `open()` function is used to open a file.

```python
open("file.txt", mode)
```

Common file modes:

| Mode | Meaning              |
| ---- | -------------------- |
| `r`  | Read                 |
| `w`  | Write / overwrite    |
| `a`  | Append               |
| `x`  | Create a new file    |
| `r+` | Read and write       |
| `b`  | Binary mode modifier |
| `t`  | Text mode modifier   |

### Important

`b` and `t` are normally used together with another mode.

Examples:

```text
rb → read binary
wb → write binary
rt → read text
wt → write text
```

---

# 4. Read Mode — `r`

`r` means **read**.

It opens an existing file for reading.

```python
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
```

If the file does not exist, Python raises:

```python
FileNotFoundError
```

### Remember

```text
r → Read
```

---

# 5. Write Mode — `w`

`w` means **write**.

It creates the file if it does not exist.

If the file already exists, its old content is **removed and replaced**.

```python
with open("file.txt", "w") as file:
    file.write("Hello, World!")
```

### Example

Before:

```text
Hello
Python
```

After using `w`:

```text
Hello, World!
```

### Remember

```text
w → Write + Overwrite
```

---

# 6. Append Mode — `a`

`a` means **append**.

It adds new data at the **end of the file**.

Existing content is not removed.

```python
with open("file.txt", "a") as file:
    file.write("Hello, World!")
```

If the file contains:

```text
Hello
```

After appending:

```text
Hello
Hello, World!
```

If you want the new text on a new line, include `\n`:

```python
with open("file.txt", "a") as file:
    file.write("\nHello, World!")
```

### Remember

```text
a → Add at the end
```

---

# 7. Read and Write Mode — `r+`

`r+` allows both:

```text
Read
Write
```

The file must already exist.

```python
with open("file.txt", "r+") as file:
    data = file.read()
    print(data)

    file.write("Hello, World!")
```

### Important

`r+` does **not automatically mean append**.

Writing happens at the **current file position**.

For example, after:

```python
file.read()
```

the file position is normally at the end, so a following write will happen there.

If you want to clearly write at the end, you can use:

```python
with open("file.txt", "r+") as file:
    data = file.read()

    file.seek(0, 2)
    file.write("Hello, World!")
```

Here:

```python
file.seek(0, 2)
```

moves the file position to the end.

### Remember

```text
r  → Read
r+ → Read + Write
```

---

# 8. Create Mode — `x`

`x` means **exclusive creation**.

It creates a new file.

```python
with open("file.txt", "x") as file:
    file.write("Hello, World!")
```

If the file already exists, Python raises:

```python
FileExistsError
```

### Remember

```text
x → Create a new file only
```

---

# 9. Binary Mode — `b`

`b` means **binary mode**.

It is normally combined with another mode.

### Read Binary

```python
with open("image.jpg", "rb") as file:
    data = file.read()
```

Here:

```text
r → read
b → binary

rb → read binary
```

### Write Binary

```python
with open("image.jpg", "wb") as file:
    file.write(binary_data)
```

Common binary modes:

```text
rb
wb
ab
rb+
wb+
```

Usually, this is not used alone:

```python
open("file.txt", "b")
```

---

# 10. Text Mode — `t`

`t` means **text mode**.

Text mode is the default mode for normal text files.

You can write:

```python
with open("file.txt", "rt") as file:
    data = file.read()
```

But usually we simply write:

```python
with open("file.txt", "r") as file:
    data = file.read()
```

Both are text mode.

Common combinations:

```text
rt → Read text
wt → Write text
at → Append text
```

### Remember

```text
t → Text
b → Binary
```

---

# 11. Context Manager with File Reading

Example:

```python
with open("file.txt", "r") as file:
    data = file.read()

print(data)
```

After the `with` block ends, the file is automatically closed.

We can check:

```python
with open("file.txt", "r") as file:
    print(file.read())

print(file.closed)
```

Output:

```text
True
```

This means the file is closed.

---

# 12. How Does Automatic Cleanup Work?

Consider:

```python
with open("file.txt", "r") as file:
    data = file.read()
```

The general process is:

```text
Enter Context
      ↓
Open Resource
      ↓
Use Resource
      ↓
Leave Context
      ↓
Cleanup Resource
```

If an exception happens inside the `with` block, the context manager still gets a chance to perform cleanup.

That is one of the biggest advantages of Context Managers.

---

# 13. How Does a Context Manager Work?

A custom Context Manager can be created using two special methods:

```python
__enter__()
__exit__()
```

These methods are part of the **Context Manager Protocol**.

### Basic Example

```python
class MyContext:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContext() as obj:
    print("Inside context")
```

Output:

```text
Entering context
Inside context
Exiting context
```

### Flow

```text
with MyContext()
       ↓
__enter__()
       ↓
with block
       ↓
__exit__()
```

---

# 14. `__enter__()` Method

`__enter__()` is called when Python enters the `with` block.

Example:

```python
def __enter__(self):
    print("Entering context")
    return self
```

It is commonly used for:

```text
Opening a resource
Allocating a resource
Initializing something
Acquiring a lock
Opening a connection
```

The value returned by `__enter__()` is assigned to the variable after `as`.

Example:

```python
with MyContext() as obj:
    print(obj)
```

Here, `obj` receives the value returned by:

```python
__enter__()
```

---

# 15. `__exit__()` Method

`__exit__()` is called when Python leaves the `with` block.

```python
def __exit__(self, exc_type, exc_value, traceback):
    print("Exiting context")
```

It is commonly used for:

```text
Closing a resource
Releasing a lock
Closing a connection
Cleaning up resources
```

### `__exit__()` Parameters

```python
__exit__(self, exc_type, exc_value, traceback)
```

These provide information about an exception, if one occurred.

```text
exc_type    → type of exception
exc_value   → exception object/value
traceback   → traceback information
```

If no exception occurs, these values are normally:

```text
None
None
None
```

---

# 16. Custom Context Manager Example

```python
class MyContext:

    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")


with MyContext():
    print("Working with resource")
```

Output:

```text
Resource acquired
Working with resource
Resource released
```

### Simple Flow

```text
__enter__()
    ↓
Resource acquired
    ↓
with block
    ↓
__exit__()
    ↓
Resource released
```

---

# 17. Context Manager Using `contextlib`

Python provides the `contextlib` module.

It allows us to create Context Managers more easily.

We can use the `@contextmanager` decorator.

```python
from contextlib import contextmanager


@contextmanager
def my_context():

    print("Resource acquired")

    try:
        yield

    finally:
        print("Resource released")


with my_context():
    print("Working with resource")
```

Output:

```text
Resource acquired
Working with resource
Resource released
```

---

# 18. Context Manager with `yield`

When using `@contextmanager`, `yield` separates the **setup** and **cleanup** parts.

Example:

```python
from contextlib import contextmanager


@contextmanager
def my_context():

    # Setup
    print("Start")

    try:
        yield

    finally:
        # Cleanup
        print("End")
```

The flow is:

```text
Setup
  ↓
yield
  ↓
with block executes
  ↓
finally
  ↓
Cleanup
```

### Easy Way to Remember

```text
Before yield → Setup
After yield  → Cleanup
```

---

# 19. Context Manager and Exceptions

One major benefit of Context Managers is that cleanup happens even when an exception occurs.

Example:

```python
class MyContext:

    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")


with MyContext():
    print("Working")

    raise ValueError("Something went wrong")
```

Output before the exception is finally reported:

```text
Resource acquired
Working
Resource released
```

Why?

Because Python calls:

```python
__exit__()
```

when leaving the `with` block, including when an exception occurs.

### Important

`__exit__()` can also control whether an exception is suppressed.

If it returns:

```python
True
```

the exception can be suppressed.

If it returns:

```python
False
```

or `None`, the exception normally continues.

---

# 20. Important File Modes

Quick revision:

```text
r   → Read
w   → Write / Overwrite
a   → Append
x   → Create new file
r+  → Read + Write
b   → Binary mode
t   → Text mode
```

### Common Combinations

```text
rb   → Read binary
wb   → Write binary
ab   → Append binary

rt   → Read text
wt   → Write text
at   → Append text

rb+  → Read + Write binary
```

---

# 21. Easy Way to Remember Context Manager

```text
Context Manager
       ↓
      with
       ↓
Acquire Resource
       ↓
   Use Resource
       ↓
 Automatic Cleanup
```

For a file:

```text
with open(...)
       ↓
   Read / Write
       ↓
 File automatically
     closes
```

### One-Line Definition

> A Context Manager manages a resource and automatically performs cleanup when the `with` block ends.

---

# 22. Context Manager vs Manual Resource Management

### Without Context Manager

```python
file = open("file.txt", "r")

try:
    data = file.read()
finally:
    file.close()
```

Here, we have to manually close the file.

### With Context Manager

```python
with open("file.txt", "r") as file:
    data = file.read()
```

The second version is:

```text
Shorter
Cleaner
Safer
Easier to read
```

It is generally the preferred way to manage resources such as files.

---

# 23. Important Interview Questions

## Q1. What is a Context Manager?

A Context Manager is a Python mechanism used to manage resources safely and automatically, usually with the `with` statement.

---

## Q2. Which keyword is used with a Context Manager?

```python
with
```

Example:

```python
with open("file.txt") as file:
    data = file.read()
```

---

## Q3. Which methods implement the Context Manager Protocol?

```python
__enter__()
__exit__()
```

---

## Q4. Why do we use Context Managers?

To make sure resources are properly cleaned up, even if an exception occurs.

---

## Q5. What is `contextlib.contextmanager`?

`contextlib.contextmanager` is a decorator that allows us to create a Context Manager using a generator function.

Example:

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    # setup
    yield
    # cleanup
```

---

## Q6. What is the difference between `w` and `a`?

```text
w → writes and overwrites existing content
a → adds new content at the end
```

---

## Q7. What is the difference between `r` and `r+`?

```text
r  → Read only
r+ → Read + Write
```

---

## Q8. What does `x` do?

`x` creates a new file.

If the file already exists:

```python
FileExistsError
```

is raised.

---

## Q9. What is the difference between `__enter__()` and `__exit__()`?

```text
__enter__() → runs when entering the with block
__exit__()  → runs when leaving the with block
```

Easy memory trick:

```text
ENTER → Start / Setup
EXIT  → Cleanup
```

---

## Q10. What happens if an exception occurs inside a `with` block?

The Context Manager's `__exit__()` method is called, so it can perform cleanup.

---

# 24. Final Summary

The most important concepts are:

```text
Context Manager
│
├── with
│
├── Resource Management
│   ├── File
│   ├── Database
│   ├── Lock
│   └── Network Connection
│
├── Context Manager Protocol
│   ├── __enter__()
│   └── __exit__()
│
└── contextlib
    └── @contextmanager
```

### Most Important Example

```python
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
```

The main idea is:

```text
Acquire
   ↓
Use
   ↓
Cleanup
```

---

# Quick Revision Cheat Sheet

| Concept           | Meaning                             |
| ----------------- | ----------------------------------- |
| `with`            | Uses a Context Manager              |
| `__enter__()`     | Setup / acquire resource            |
| `__exit__()`      | Cleanup / release resource          |
| `@contextmanager` | Easy way to create Context Managers |
| `yield`           | Separates setup and cleanup         |
| `r`               | Read                                |
| `w`               | Write / overwrite                   |
| `a`               | Append                              |
| `x`               | Create new file                     |
| `r+`              | Read + write                        |
| `b`               | Binary                              |
| `t`               | Text                                |

### Final Mental Model

```text
          CONTEXT MANAGER
                 │
                 ▼
              with
                 │
                 ▼
        Acquire Resource
                 │
                 ▼
            Use Resource
                 │
          ┌──────┴──────┐
          │             │
       Success       Exception
          │             │
          └──────┬──────┘
                 ▼
          Cleanup Resource
                 │
                 ▼
              Finished
```

**Remember:** The main purpose of a Context Manager is:

> **Acquire → Use → Cleanup automatically**

"""