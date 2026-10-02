"""
# Python Type Hinting and Annotations

## 1. What is Type Hinting?

**Type hinting** is a feature in Python that allows us to specify the expected types of:

* Variables
* Function parameters
* Function return values
* Class attributes
* Objects

Type hints improve:

* Code readability
* IDE/editor support
* Static type checking
* Code maintainability
* Developer productivity

### Example

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here:

```text
a: int       → a should be an integer
b: int       → b should be an integer
-> int       → function is expected to return an integer
```

### Important

Python does **not normally enforce type hints at runtime**.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("10", "20"))
```

This can run and produce:

```text
1020
```

The type hints themselves do not prevent the call.

Static type checkers such as **mypy** or **pyright** can detect this kind of problem before runtime.

---

# 2. Type Annotation

A **type annotation** is the syntax used to associate a type with a variable, parameter, attribute, or return value.

### Basic Syntax

```python
variable: type
```

### Variable Annotation

```python
x: int = 10
y: str = "Hello"
z: float = 10.5
```

Here:

```text
x → int
y → str
z → float
```

---

# 3. Function Annotations

Function annotations specify the expected types of parameters and the return value.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Example:

```python
result: int = add(10, 20)

print(result)
```

Output:

```text
30
```

### Important

The syntax:

```python
a: int
```

is a parameter annotation.

The syntax:

```python
-> int
```

is a return annotation.

---

# 4. Type Annotation for Built-in Collections

Modern Python supports generic built-in collection types.

## List

```python
numbers: list[int] = [1, 2, 3, 4, 5]
```

This means:

```text
numbers should be a list of integers.
```

---

## Tuple

```python
point: tuple[int, int] = (10, 20)
```

This means:

```text
point contains exactly two integers.
```

Another example:

```python
data: tuple[str, int, float] = ("John", 25, 75.5)
```

---

## Set

```python
numbers: set[int] = {1, 2, 3, 4}
```

This means:

```text
numbers is expected to be a set of integers.
```

---

## Dictionary

```python
student: dict[str, int] = {
    "age": 25,
    "score": 90
}
```

This means:

```text
key   → str
value → int
```

---

# 5. Type Hinting with Classes

Type hints can also be used with classes.

```python
class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"
```

Creating an object:

```python
person: Person = Person("John", 30)

print(person)
```

Here:

```python
person: Person
```

means that `person` is expected to refer to a `Person` object.

---

# 6. `-> None` in Type Hints

When a function does not return a meaningful value, we can annotate it with:

```python
-> None
```

Example:

```python
def greet(name: str) -> None:
    print(f"Hello, {name}")
```

The function performs an action but does not return a value.

---

# 7. Type Alias

A **type alias** gives another name to an existing type or type expression.

It is useful when a type expression is long or used repeatedly.

## Simple Type Alias

```python
UserId = int
```

Now we can use:

```python
user_id: UserId = 1001
```

However, note that:

```python
UserId = int
```

is simply an alias for `int`.

It does **not** create a new type.

---

# 8. Explicit Type Alias with `TypeAlias`

For clarity, Python provides `TypeAlias`.

```python
from typing import TypeAlias

UserId: TypeAlias = int
```

Example:

```python
user_id: UserId = 123
```

Another example:

```python
Server: TypeAlias = dict[str, str | int]
```

Then:

```python
server: Server = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8000
}
```

---

# 9. Type Alias for Complex Types

Suppose we repeatedly use:

```python
dict[str, str | int]
```

Instead of writing it repeatedly, we can create an alias.

```python
from typing import TypeAlias

Server: TypeAlias = dict[str, str | int]
Network: TypeAlias = list[Server]
```

Now:

```python
server: Server = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8000
}

network: Network = [
    {
        "hostName": "localhost",
        "address": "127.0.0.1",
        "port": 8000
    },
    {
        "hostName": "MyServer",
        "address": "192.168.0.10",
        "port": 8000
    }
]
```

This makes the code easier to read.

---

# 10. `TypedDict`

`TypedDict` is used when we want to describe the expected structure of a dictionary.

```python
from typing import TypedDict
```

Example:

```python
class Server(TypedDict):
    hostName: str
    address: str
    port: int
```

Now we can write:

```python
server: Server = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8080
}
```

A list of servers:

```python
servers: list[Server] = [
    {
        "hostName": "localhost",
        "address": "127.0.0.1",
        "port": 8080
    },
    {
        "hostName": "MyServer",
        "address": "192.168.0.10",
        "port": 8000
    }
]
```

### Why use `TypedDict`?

Without `TypedDict`:

```python
server: dict[str, str | int]
```

This only tells us:

```text
keys   → strings
values → strings or integers
```

It does not tell us that the dictionary should contain:

```text
hostName
address
port
```

`TypedDict` allows us to describe that structure more precisely.

---

# 11. `TypedDict` vs Type Alias

### Type Alias

```python
Server: TypeAlias = dict[str, str | int]
```

This describes the general type:

```text
Dictionary
    key   → str
    value → str | int
```

### TypedDict

```python
class Server(TypedDict):
    hostName: str
    address: str
    port: int
```

This describes the expected dictionary structure:

```text
Server
├── hostName → str
├── address  → str
└── port     → int
```

---

# 12. `NewType`

`NewType` is used to create a **distinct type for static type checking** while having very little runtime overhead.

```python
from typing import NewType

UserId = NewType("UserId", int)
```

Now:

```python
user_id = UserId(123456)

print(user_id)
```

Output:

```text
123456
```

### Important Runtime Behavior

```python
print(type(user_id))
```

Output:

```text
<class 'int'>
```

At runtime, the resulting value behaves like an `int`.

But static type checkers can distinguish:

```python
UserId = NewType("UserId", int)
ProductId = NewType("ProductId", int)
```

Conceptually:

```text
UserId     → int-based distinct static type
ProductId  → int-based distinct static type
```

This can help prevent accidentally passing one kind of ID where another is expected.

---

# 13. Important `NewType` Correction

Consider:

```python
UserId = NewType("UserId", int)

user_id = UserId("123456")
```

This does **not** perform runtime validation or conversion from string to integer.

The value is still a string at runtime.

Therefore, do not think of `NewType` as a runtime validator or converter.

Use:

```python
user_id = UserId(123456)
```

not:

```python
user_id = UserId("123456")
```

when the base type is `int`.

---

# 14. `ClassVar`

`ClassVar` is used to indicate that an attribute is intended to be a **class variable**, not an instance variable.

```python
from typing import ClassVar

class Person:

    species: ClassVar[str] = "Human"

    def __init__(self, name: str):
        self.name: str = name
```

Now:

```python
person = Person("John")

print(Person.species)
print(person.name)
```

Here:

```text
species → class-level attribute
name    → instance-level attribute
```

### Another Example

```python
class Company:

    company_name: ClassVar[str] = "ABC Ltd"

    def __init__(self, employee_name: str):
        self.employee_name: str = employee_name
```

`company_name` belongs to the class conceptually, while `employee_name` belongs to each object.

---

# 15. `Final`

`Final` indicates that a name is intended not to be reassigned.

```python
from typing import Final

COUNTRY: Final[str] = "Bangladesh"
```

A static type checker can warn if you later try:

```python
COUNTRY = "India"
```

### Important

`Final` is primarily for **static type checking**.

It does not make the value immutable at runtime.

For example, Python itself does not automatically raise an error simply because a variable was annotated with `Final`.

---

# 16. Class Attribute vs Instance Attribute

Consider:

```python
class Person:

    species: ClassVar[str] = "Human"

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
```

Here:

```text
Person
│
├── species → ClassVar[str]
│
├── name → str
│
└── age → int
```

`species` is intended to be shared at the class level.

`name` and `age` belong to individual objects.

---

# 17. Type Annotation for an Object

We can annotate an object using the class name.

```python
class Calculator:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def add(self) -> int:
        return self.x + self.y
```

Now:

```python
calculator: Calculator = Calculator(10, 20)

print(calculator.add())
```

Output:

```text
30
```

---

# 18. Instance Attribute Annotation

Instance attributes can be annotated directly.

```python
class Person:

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
```

Here:

```python
self.name: str
self.age: int
```

are instance attribute annotations.

---

# 19. Attribute Annotation Without Assignment

We can also annotate attributes at class scope.

```python
class Person:

    name: str
    age: int
```

This tells type checkers that instances are expected to have:

```text
name → str
age  → int
```

But this syntax alone does not automatically create instance attributes with values.

Usually, we initialize them in `__init__`:

```python
class Person:

    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

---

# 20. Type Hints with Union Types

Modern Python supports the `|` syntax for union types.

```python
value: int | str
```

This means:

```text
value can be an int or a str.
```

Example:

```python
def process(value: int | str) -> None:
    print(value)
```

Both are valid:

```python
process(100)
process("Hello")
```

---

# 21. Type Alias with Union

```python
from typing import TypeAlias

ServerValue: TypeAlias = str | int
```

Then:

```python
server: dict[str, ServerValue] = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8000
}
```

---

# 22. Generic Collections

Modern Python allows us to write:

```python
list[int]
dict[str, int]
set[str]
tuple[int, str]
```

instead of older forms such as:

```python
List[int]
Dict[str, int]
Set[str]
Tuple[int, str]
```

For modern Python code, built-in generic syntax is generally preferred when supported by the Python version being used.

---

# 23. Old vs Modern Syntax

### Older Style

```python
from typing import List, Dict, Tuple, Set

numbers: List[int] = [1, 2, 3]

student: Dict[str, int] = {
    "age": 25
}

point: Tuple[int, int] = (10, 20)

names: Set[str] = {"John", "Bob"}
```

### Modern Style

```python
numbers: list[int] = [1, 2, 3]

student: dict[str, int] = {
    "age": 25
}

point: tuple[int, int] = (10, 20)

names: set[str] = {"John", "Bob"}
```

---

# 24. `__annotations__`

Python stores annotations and makes them available through `__annotations__`.

Example:

```python
x: int = 10
name: str = "John"
```

We can inspect them:

```python
print(__annotations__)
```

Example output:

```python
{'x': <class 'int'>, 'name': <class 'str'>}
```

For a class:

```python
class Person:

    name: str
    age: int
```

We can inspect:

```python
print(Person.__annotations__)
```

---

# 25. Complete Example

```python
from typing import ClassVar, Final, NewType, TypeAlias, TypedDict


# NewType
UserId = NewType("UserId", int)


# Type aliases
HostName: TypeAlias = str
Address: TypeAlias = str
Port: TypeAlias = int


# TypedDict
class Server(TypedDict):
    hostName: HostName
    address: Address
    port: Port


# Type alias for a network
Network: TypeAlias = list[Server]


class User:

    company: ClassVar[str] = "ABC Ltd"
    country: Final[str] = "Bangladesh"

    def __init__(self, user_id: UserId, name: str, age: int):
        self.user_id: UserId = user_id
        self.name: str = name
        self.age: int = age

    def __str__(self) -> str:
        return (
            f"User(id={self.user_id}, "
            f"name={self.name}, "
            f"age={self.age})"
        )


user: User = User(
    UserId(101),
    "John",
    25
)

server: Server = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8000
}

network: Network = [
    server,
    {
        "hostName": "MyServer",
        "address": "192.168.0.10",
        "port": 8080
    }
]

print(user)
print(server)
print(network)
print(User.company)
print(User.country)
```

---

# 26. Type Hinting vs Type Annotation

These terms are often used interchangeably, but there is a useful distinction.

### Type Annotation

The actual syntax used to annotate something:

```python
name: str
```

### Type Hinting

The broader practice of using type information throughout code:

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

So:

```text
Type Annotation → syntax
Type Hinting    → practice/use of type information
```

---

# 27. Type Hinting Does Not Mean Runtime Validation

This is one of the most important concepts.

```python
def square(number: int) -> int:
    return number * number
```

The annotation says:

```text
number is expected to be int
```

But Python does not automatically enforce it.

For example:

```python
square("5")
```

may result in:

```text
"55"
```

because Python's runtime behavior is still based on the actual object and operation.

If runtime validation is required, use explicit checks or appropriate validation libraries.

---

# 28. Type Hints and Static Type Checkers

Type hints become especially useful with tools such as:

```text
mypy
pyright
Pylance
```

For example:

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("10", "20")
```

A static type checker can report that strings were supplied where integers were expected.

---

# 29. Common Mistakes

## Mistake 1: Thinking Type Hints Enforce Types

Incorrect assumption:

```text
a: int
```

means Python will automatically reject strings.

Correct:

```text
Type hints provide type information.
Static type checkers can analyze that information.
They do not normally perform runtime validation by themselves.
```

---

## Mistake 2: Confusing Type Alias with `NewType`

### Type Alias

```python
UserId: TypeAlias = int
```

This is simply another name for `int`.

### NewType

```python
UserId = NewType("UserId", int)
```

This creates a distinct type for static type checking based on `int`.

---

## Mistake 3: Thinking `Final` Makes a Value Immutable

```python
name: Final[str] = "John"
```

`Final` does not make the object immutable at runtime.

It communicates an intended no-reassignment rule to static type checkers.

---

## Mistake 4: Thinking `ClassVar` Creates a Class Variable

`ClassVar` is primarily a typing annotation that tells type checkers the attribute is intended to be class-level.

Example:

```python
class Person:
    species: ClassVar[str] = "Human"
```

The assignment creates the class attribute; `ClassVar` describes its intended typing role.

---

# 30. Quick Comparison

| Feature          | Purpose                                                    |
| ---------------- | ---------------------------------------------------------- |
| Type Annotation  | Annotate a variable, parameter, attribute, or return value |
| Type Hinting     | General practice of adding type information                |
| Type Alias       | Give another name to a type/type expression                |
| `TypeAlias`      | Explicitly declare a type alias                            |
| `TypedDict`      | Describe the expected structure of a dictionary            |
| `NewType`        | Create a distinct static type based on another type        |
| `ClassVar`       | Indicate an attribute is intended to be class-level        |
| `Final`          | Indicate a name should not be reassigned                   |
| `list[int]`      | List containing integers                                   |
| `dict[str, int]` | Dictionary with string keys and integer values             |
| `int \| str`     | Value can be `int` or `str`                                |

---

# 31. Mental Model

Remember the concepts like this:

```text
                    Python Type System
                           │
            ┌──────────────┴──────────────┐
            │                             │
       Type Annotation               Type Aliases
            │                             │
      ┌─────┼─────┐                 ┌────┴────┐
      │     │     │                 │         │
   Variable Function Class       TypeAlias  NewType
      │
      ├── list[int]
      ├── tuple[int, int]
      ├── set[str]
      └── dict[str, int]

Special Typing Tools
        │
        ├── TypedDict
        ├── ClassVar
        └── Final
```

---

# 32. Easy Memory Rules

```text
Annotation
    ↓
Adds type information

Type Hinting
    ↓
Uses type information throughout the code

Type Alias
    ↓
Another name for a type

TypedDict
    ↓
Describes dictionary structure

NewType
    ↓
Creates a distinct static type

ClassVar
    ↓
Intended class-level attribute

Final
    ↓
Intended no-reassignment name
```

---

# 33. Interview Questions

### 1. What is type hinting in Python?

Type hinting is the practice of specifying expected types for variables, parameters, return values, and other program elements.

---

### 2. Does Python enforce type hints at runtime?

No. Type hints normally do not perform runtime type checking automatically.

---

### 3. What is the difference between type annotation and type hinting?

A type annotation is the syntax used to specify type information, while type hinting is the broader practice of using such type information in code.

---

### 4. What is a type alias?

A type alias gives another name to an existing type or type expression.

Example:

```python
from typing import TypeAlias

UserId: TypeAlias = int
```

---

### 5. What is `TypedDict`?

`TypedDict` is used to describe the expected keys and value types of a dictionary.

---

### 6. What is `NewType`?

`NewType` creates a distinct type for static type checking based on an existing type.

```python
UserId = NewType("UserId", int)
```

---

### 7. What is `ClassVar`?

`ClassVar` indicates that an attribute is intended to be a class variable rather than an instance variable.

---

### 8. What is `Final`?

`Final` indicates that a name is intended not to be reassigned, primarily for static type checking.

---

### 9. What does `-> None` mean?

It indicates that a function is expected not to return a value.

---

### 10. What is the difference between `TypedDict` and `dict`?

```python
dict[str, str | int]
```

describes general key/value types.

```python
class Server(TypedDict):
    hostName: str
    address: str
    port: int
```

describes a specific dictionary structure.

---

# 34. Final Summary

Python type hints help developers communicate the expected structure and types of data.

The most important concepts are:

```text
Variable Annotation
        ↓
x: int

Function Annotation
        ↓
def add(a: int, b: int) -> int

Class Annotation
        ↓
person: Person

Collection Annotation
        ↓
list[int]
dict[str, int]
tuple[int, str]

Type Alias
        ↓
TypeAlias

Structured Dictionary
        ↓
TypedDict

Distinct Static Type
        ↓
NewType

Class-Level Attribute
        ↓
ClassVar

No-Reassignment Intent
        ↓
Final
```

The key idea is:

> **Type hints describe how your code is expected to be used; they do not normally enforce those types at runtime.**

"""