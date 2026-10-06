"""
# Python Type Hinting and Annotations

## 1. What is Type Hinting?

**Type hinting** means telling Python developers what type of data a variable, function parameter, or return value is expected to have.

It makes code:

* Easier to read
* Easier to understand
* Easier to maintain
* Easier for IDEs to analyze
* Easier for tools like `mypy` and `pyright` to check

### Example

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here:

```text
a: int  → a should be an integer
b: int  → b should be an integer
-> int  → function should return an integer
```

### Important

Python normally **does not force type hints at runtime**.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("10", "20"))
```

Output:

```text
1020
```

Why?

Because Python sees two strings and joins them.

Type hints only describe what we **expect**.

Tools like `mypy` and `pyright` can find these type problems.

---

# 2. What is Type Annotation?

A **type annotation** is the syntax we use to specify a type.

Basic syntax:

```python
variable: type
```

### Example

```python
x: int = 10
name: str = "John"
price: float = 10.5
```

Here:

```text
x     → int
name  → str
price → float
```

---

# 3. Function Annotations

We can specify the types of function parameters and return values.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here:

```text
a: int  → parameter type
b: int  → parameter type
-> int  → return type
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

---

# 4. Type Hints for Lists

Modern Python allows:

```python
numbers: list[int] = [1, 2, 3, 4]
```

This means:

```text
numbers is expected to be a list of integers.
```

Another example:

```python
names: list[str] = ["John", "Bob", "Alex"]
```

This means:

```text
names is expected to be a list of strings.
```

---

# 5. Type Hints for Tuple

Example:

```python
point: tuple[int, int] = (10, 20)
```

This means the tuple contains:

```text
integer
integer
```

Another example:

```python
data: tuple[str, int, float] = ("John", 25, 75.5)
```

Here:

```text
str
int
float
```

---

# 6. Type Hints for Set

```python
numbers: set[int] = {1, 2, 3, 4}
```

This means:

```text
numbers is expected to be a set of integers.
```

Example:

```python
names: set[str] = {"John", "Bob", "Alex"}
```

---

# 7. Type Hints for Dictionary

Example:

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

So:

```python
"age" → string
25    → integer
```

---

# 8. Type Hinting with Classes

We can also use type hints with classes.

```python
class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"
```

Create an object:

```python
person: Person = Person("John", 30)

print(person)
```

Here:

```python
person: Person
```

means:

```text
person is expected to be a Person object.
```

---

# 9. What does -> None mean?

If a function does not return a useful value, we can use:

```python
-> None
```

Example:

```python
def greet(name: str) -> None:
    print(f"Hello, {name}")
```

The function prints something but does not return a value.

---

# 10. Type Alias

A **type alias** gives another name to a type.

Example:

```python
UserId = int
```

Now:

```python
user_id: UserId = 1001
```

Here:

```text
UserId is another name for int.
```

It does **not** create a new type.

---

# 11. TypeAlias

Python provides `TypeAlias` to clearly show that something is a type alias.

```python
from typing import TypeAlias

UserId: TypeAlias = int
```

Now:

```python
user_id: UserId = 123
```

Another example:

```python
Server: TypeAlias = dict[str, str | int]
```

Now:

```python
server: Server = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8000
}
```

---

# 12. Complex Type Alias

Suppose we repeatedly use:

```python
dict[str, str | int]
```

This can make code difficult to read.

We can create an alias:

```python
from typing import TypeAlias

Server: TypeAlias = dict[str, str | int]

Network: TypeAlias = list[Server]
```

Now we can write:

```python
server: Server = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8000
}
```

And:

```python
network: Network = [
    {
        "hostName": "localhost",
        "address": "127.0.0.1",
        "port": 8000
    }
]
```

This makes code easier to understand.

---

# 13. TypedDict

`TypedDict` is used when we want to describe the **exact structure of a dictionary**.

Example:

```python
from typing import TypedDict

class Server(TypedDict):
    hostName: str
    address: str
    port: int
```

Now:

```python
server: Server = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8080
}
```

The expected structure is:

```text
Server
├── hostName → str
├── address  → str
└── port     → int
```

---

# 14. Why Use TypedDict?

Without `TypedDict`:

```python
server: dict[str, str | int]
```

This only tells us:

```text
key   → string
value → string or integer
```

It does not tell us the exact keys.

With `TypedDict`:

```python
class Server(TypedDict):
    hostName: str
    address: str
    port: int
```

Now we know exactly what the dictionary should contain.

---

# 15. Type Alias vs TypedDict

### Type Alias

```python
Server: TypeAlias = dict[str, str | int]
```

Means:

```text
Dictionary
    ↓
key   → str
value → str or int
```

### TypedDict

```python
class Server(TypedDict):
    hostName: str
    address: str
    port: int
```

Means:

```text
Server
├── hostName → str
├── address  → str
└── port     → int
```

### Easy Rule

```text
Type Alias
    ↓
Describes a general type

TypedDict
    ↓
Describes a specific dictionary structure
```

---

# 16. NewType

`NewType` creates a **different type for static type checking**.

Example:

```python
from typing import NewType

UserId = NewType("UserId", int)
```

Now:

```python
user_id = UserId(123)
```

At runtime:

```python
print(type(user_id))
```

Output:

```text
<class 'int'>
```

So at runtime, it behaves like an integer.

But type checkers can treat `UserId` and `int` as different concepts.

---

# 17. Why Use NewType?

Suppose we have:

```python
UserId = NewType("UserId", int)
ProductId = NewType("ProductId", int)
```

Both are based on `int`.

But conceptually:

```text
UserId
    ↓
ID of a user

ProductId
    ↓
ID of a product
```

This can help prevent accidentally using one ID instead of another.

---

# 18. Important NewType Rule

Do not think `NewType` converts or validates data at runtime.

For example:

```python
UserId = NewType("UserId", int)

user_id = UserId("123")
```

`NewType` does not convert `"123"` into `123`.

If you want an integer, convert it first:

```python
user_id = UserId(int("123"))
```

Or:

```python
user_id = UserId(123)
```

Easy rule:

```text
NewType
   ↓
Useful for static type checking

Not
   ↓
Runtime validation
```

---

# 19. ClassVar

`ClassVar` tells type checkers that an attribute is intended to belong to the **class**, not each individual object.

Example:

```python
from typing import ClassVar

class Person:

    species: ClassVar[str] = "Human"

    def __init__(self, name: str):
        self.name: str = name
```

Here:

```text
species → class variable
name    → instance variable
```

We can use:

```python
print(Person.species)
```

And:

```python
person = Person("John")

print(person.name)
```

---

# 20. Class Variable vs Instance Variable

Example:

```python
class Person:

    species: ClassVar[str] = "Human"

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
```

Structure:

```text
Person
│
├── species → ClassVar
│
├── name → instance attribute
│
└── age → instance attribute
```

Easy rule:

```text
ClassVar
   ↓
Shared/class-level information

self.name
self.age
   ↓
Information belonging to each object
```

---

# 21. Final

`Final` tells static type checkers that a value should **not be reassigned**.

Example:

```python
from typing import Final

COUNTRY: Final[str] = "Bangladesh"
```

This should not be changed:

```python
COUNTRY = "India"
```

A static type checker can show a warning.

### Important

`Final` does not make the value completely immutable at runtime.

It is mainly a message for developers and type checkers.

---

# 22. Object Type Annotation

We can use a class name as a type.

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

Here:

```python
calculator: Calculator
```

means:

```text
calculator is expected to be a Calculator object.
```

---

# 23. Instance Attribute Annotation

We can annotate instance attributes.

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

# 24. Attribute Annotation Without Assignment

We can write:

```python
class Person:

    name: str
    age: int
```

This tells type checkers:

```text
name should be a string
age should be an integer
```

But this does not automatically create values.

Usually we initialize them:

```python
class Person:

    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

---

# 25. Union Types

Sometimes a value can have more than one type.

Modern Python uses `|`.

Example:

```python
value: int | str
```

This means:

```text
value can be an int OR a str.
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

# 26. Type Alias with Union

We can create an alias:

```python
from typing import TypeAlias

ServerValue: TypeAlias = str | int
```

Now:

```python
server: dict[str, ServerValue] = {
    "hostName": "localhost",
    "address": "127.0.0.1",
    "port": 8000
}
```

---

# 27. Generic Collections

Modern Python supports generic collections directly.

Examples:

```python
list[int]
dict[str, int]
set[str]
tuple[int, str]
```

These are modern versions of:

```python
List[int]
Dict[str, int]
Set[str]
Tuple[int, str]
```

Modern syntax is generally preferred in current Python versions.

---

# 28. Old vs Modern Syntax

### Old Style

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

Easy rule:

```text
Modern Python
    ↓
list[int]
dict[str, int]
tuple[int, int]
set[str]
```

---

# 29. **annotations**

Python stores annotations in `__annotations__`.

Example:

```python
x: int = 10
name: str = "John"

print(__annotations__)
```

You may see:

```python
{
    'x': <class 'int'>,
    'name': <class 'str'>
}
```

For a class:

```python
class Person:
    name: str
    age: int
```

We can check:

```python
print(Person.__annotations__)
```

This shows the class annotations.

---

# 30. Type Hinting vs Type Annotation

These two terms are very similar.

### Type Annotation

The actual syntax:

```python
name: str
```

### Type Hinting

The general practice of using type information:

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

Easy way to remember:

```text
Type Annotation
    ↓
The syntax

Type Hinting
    ↓
The practice of using type information
```

---

# 31. Type Hints Do Not Normally Validate at Runtime

This is very important.

Example:

```python
def square(number: int) -> int:
    return number * number
```

The annotation says:

```text
number is expected to be an int.
```

But Python does not normally check this automatically.

For example:

```python
square("5")
```

can produce:

```text
"55"
```

because:

```python
"5" * "5"
```

would actually be invalid, but:

```python
"5" * 5
```

would produce `"55555"`.

So the important point is:

```text
Type hints describe expected types.
They do not normally enforce types at runtime.
```

If runtime validation is needed, use explicit validation or a validation library.

---

# 32. Type Checkers

Type hints are very useful with static type-checking tools.

Common tools include:

```text
mypy
pyright
Pylance
```

Example:

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("10", "20")
```

A type checker can report:

```text
Expected int
Got str
```

before the program runs.

---

# 33. Common Mistakes

## Mistake 1: Thinking Type Hints Force Types

Wrong idea:

```python
x: int
```

means Python will automatically reject strings.

Correct idea:

```text
Type hints describe expected types.
They do not normally enforce types at runtime.
```

---

## Mistake 2: Confusing Type Alias and NewType

### Type Alias

```python
from typing import TypeAlias

UserId: TypeAlias = int
```

This means:

```text
UserId is another name for int.
```

### NewType

```python
UserId = NewType("UserId", int)
```

This creates a distinct type for static type checking.

Easy rule:

```text
TypeAlias
    ↓
Another name

NewType
    ↓
Different static type
```

---

## Mistake 3: Thinking Final Makes Data Immutable

Example:

```python
name: Final[str] = "John"
```

`Final` does not make the object immutable.

It means:

```text
Do not reassign this name.
```

Type checkers can warn if you reassign it.

---

## Mistake 4: Thinking ClassVar Creates a Class Variable

Example:

```python
class Person:

    species: ClassVar[str] = "Human"
```

The assignment creates the class attribute.

`ClassVar` tells type checkers:

```text
This attribute is intended to be class-level.
```

---

# 34. Quick Comparison

| Feature          | Easy Meaning                         |
| ---------------- | ------------------------------------ |
| Type Annotation  | Adds type information                |
| Type Hinting     | Using type information in code       |
| Type Alias       | Another name for a type              |
| `TypeAlias`      | Clearly declares a type alias        |
| `TypedDict`      | Describes a dictionary structure     |
| `NewType`        | Creates a distinct static type       |
| `ClassVar`       | Shows an attribute is class-level    |
| `Final`          | Says a name should not be reassigned |
| `list[int]`      | List of integers                     |
| `dict[str, int]` | String keys and integer values       |
| `int \| str`     | Integer or string                    |

---

# 35. Easy Mental Model

Think about Python typing like this:

```text
Python Typing
│
├── Type Annotation
│   │
│   ├── Variable
│   ├── Function
│   ├── Class
│   └── Collection
│
├── Type Alias
│   │
│   ├── TypeAlias
│   └── NewType
│
└── Special Tools
    │
    ├── TypedDict
    ├── ClassVar
    └── Final
```

---

# 36. Easy Memory Rules

Remember these:

```text
Annotation
    ↓
Adds type information

Type Hinting
    ↓
Uses type information in code

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
Class-level attribute

Final
    ↓
Should not be reassigned
```

---

# 37. Interview Questions

## 1. What is type hinting?

Type hinting is a way to tell developers and tools what types are expected for variables, parameters, and return values.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## 2. Does Python enforce type hints at runtime?

**No.**

Python normally does not automatically enforce type hints at runtime.

Static type checkers such as `mypy` and `pyright` can check them.

---

## 3. What is a type annotation?

A type annotation is the syntax used to specify type information.

Example:

```python
name: str
```

---

## 4. What is a type alias?

A type alias gives another name to an existing type.

Example:

```python
from typing import TypeAlias

UserId: TypeAlias = int
```

---

## 5. What is TypedDict?

`TypedDict` describes the expected keys and value types of a dictionary.

Example:

```python
class Server(TypedDict):
    hostName: str
    address: str
    port: int
```

---

## 6. What is NewType?

`NewType` creates a distinct type for static type checking.

Example:

```python
UserId = NewType("UserId", int)
```

---

## 7. What is ClassVar?

`ClassVar` tells type checkers that an attribute is intended to be a class variable.

Example:

```python
class Person:
    species: ClassVar[str] = "Human"
```

---

## 8. What is Final?

`Final` tells type checkers that a name should not be reassigned.

Example:

```python
COUNTRY: Final[str] = "Bangladesh"
```

---

## 9. What does -> None mean?

It means the function is expected not to return a value.

Example:

```python
def greet(name: str) -> None:
    print(name)
```

---

## 10. TypedDict vs dict — what is the difference?

General dictionary:

```python
dict[str, str | int]
```

This tells us:

```text
keys → strings
values → strings or integers
```

`TypedDict`:

```python
class Server(TypedDict):
    hostName: str
    address: str
    port: int
```

This tells us the exact expected structure.

---

# 38. Final Summary

The most important Python type-hinting concepts are:

```text
Variable Annotation
        ↓
x: int

Function Annotation
        ↓
def add(a: int, b: int) -> int

Object Annotation
        ↓
person: Person

List
        ↓
list[int]

Dictionary
        ↓
dict[str, int]

Tuple
        ↓
tuple[int, str]

Type Alias
        ↓
TypeAlias

Dictionary Structure
        ↓
TypedDict

Distinct Static Type
        ↓
NewType

Class Attribute
        ↓
ClassVar

No Reassignment
        ↓
Final

Union
        ↓
int | str
```

## Most Important Point

> **Type hints tell us what type of data we expect. They normally do not force or validate the type at runtime.**

In simple words:

```text
Type Hint
    ↓
"I expect this value to be of this type."

Not:

    ↓

"Python absolutely will not allow anything other than this type."
```

So, remember:

```text
Type Hinting
    =
Expected Type Information
```

"""