"""
# ==========================================================

# CONSTRUCTOR IN PYTHON

# ==========================================================

## 1. What is a Constructor?

A constructor is a special method used to initialize an object
when it is created.

In Python, `__init__()` is commonly called the constructor
because it initializes the object's attributes.

### Important Note

Technically, Python uses two important methods:

```text
__new__()  → Creates the object
__init__() → Initializes the object
```

For beginner-level Python OOP, we commonly refer to
`__init__()` as the constructor.

### Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Faruk Ahmed", 22)
```

When this statement executes:

```python
student = Student("Faruk Ahmed", 22)
```

Python creates the object and then calls `__init__()` to
initialize its attributes.

# ==========================================================

# TYPES OF CONSTRUCTOR

# ==========================================================

Commonly discussed constructor types in Python are:

```text
1. Default Constructor
2. Non-Parameterized Constructor
3. Parameterized Constructor
```

> Note:
> These are common OOP terminology used for learning.
> Python does not formally define these as three separate
> constructor types.

# ==========================================================

# 1. DEFAULT CONSTRUCTOR

# ==========================================================

## What is a Default Constructor?

If we do not explicitly define an `__init__()` method inside
a class, Python provides the default initialization behavior.

### Example

```python
class DefaultConstructor:

    name = "Default User"
    age = 0

    def showInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":

    default_obj = DefaultConstructor()

    default_obj.showInfo()
```

### Output

```text
Name: Default User, Age: 0
```

Here, we did not define:

```python
def __init__(self):
    ...
```

Therefore, Python uses the default initialization behavior.

> Note:
> The term "default constructor" is commonly used in OOP
> teaching. In Python, it is more precise to say that the
> class has no explicitly defined `__init__()` method.

# ==========================================================

# 2. PARAMETERIZED CONSTRUCTOR

# ==========================================================

## What is a Parameterized Constructor?

A parameterized constructor is an `__init__()` method that
accepts additional parameters to initialize object attributes.

### Example

```python
class ParameterizedConstructor:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":

    param_obj = ParameterizedConstructor(
        "Faruk Ahmed",
        22
    )

    param_obj.showInfo()
```

### Output

```text
Name: Faruk Ahmed, Age: 22
```

Here:

```python
__init__(self, name, age)
```

`name` and `age` are parameters.

When we create the object:

```python
ParameterizedConstructor("Faruk Ahmed", 22)
```

the values are passed to the constructor.

# ==========================================================

# 3. NON-PARAMETERIZED CONSTRUCTOR

# ==========================================================

## What is a Non-Parameterized Constructor?

A non-parameterized constructor is an `__init__()` method
that does not receive any additional argument from the caller.

It contains only:

```python
self
```

### Example

```python
class NonParameterizedConstructor:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def showInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":

    non_param_obj = NonParameterizedConstructor()

    non_param_obj.showInfo()
```

### Example Output

```text
Enter your name: Faruk
Enter your age: 22

Name: Faruk, Age: 22
```

### Important

`input()` is NOT a requirement of a non-parameterized
constructor.

For example, this is also a non-parameterized constructor:

```python
class Student:

    def __init__(self):
        self.name = "Faruk"
        self.age = 22
```

The important point is:

```python
__init__(self)
```

There are no additional parameters.

# ==========================================================

# CONSTRUCTOR CALL IN PYTHON

# ==========================================================

A parent class's `__init__()` method can be called from a
child class in different ways.

Two common approaches are:

```text
1. Manual Constructor Call
2. super() Constructor Call
```

# ==========================================================

# 1. MANUAL CONSTRUCTOR CALL

# ==========================================================

In a manual constructor call, we explicitly call the parent
class's `__init__()` method.

### Example

```python
class Parent1:

    def __init__(self):
        print("Parent1 constructor")


class Parent2:

    def __init__(self):
        print("Parent2 constructor")


class Child(Parent1, Parent2):

    def __init__(self):

        # Manually calling Parent1 constructor
        Parent1.__init__(self)

        # Manually calling Parent2 constructor
        Parent2.__init__(self)

        print("Child constructor")


print("===== Manual Constructor Call =====")

child1 = Child()
```

### Output

```text
===== Manual Constructor Call =====
Parent1 constructor
Parent2 constructor
Child constructor
```

### Explanation

Here, we explicitly call:

```python
Parent1.__init__(self)
```

and:

```python
Parent2.__init__(self)
```

So Python does not automatically call both parent
constructors for us.

We explicitly tell Python which constructors to execute.

# ==========================================================

# 2. super()

# ==========================================================

## What is super()?

`super()` is used to access the next class in the
Method Resolution Order (MRO).

It is commonly used in inheritance to call a parent class's
method.

In multiple inheritance, `super()` follows the MRO.

# ==========================================================

# super() CONSTRUCTOR CALL

# ==========================================================

### Example

```python
class Parent1:

    def __init__(self):

        super().__init__()

        print("Parent1 constructor")


class Parent2:

    def __init__(self):

        super().__init__()

        print("Parent2 constructor")


class Child(Parent1, Parent2):

    def __init__(self):

        super().__init__()

        print("Child constructor")


print("\n===== super() Constructor Call =====")

child2 = Child()
```

### Output

```text
===== super() Constructor Call =====
Parent2 constructor
Parent1 constructor
Child constructor
```

# ==========================================================

# UNDERSTANDING MRO

# ==========================================================

For:

```python
class Child(Parent1, Parent2):
    ...
```

the MRO is:

```text
Child
  ↓
Parent1
  ↓
Parent2
  ↓
object
```

We can check the MRO using:

```python
print(Child.mro())
```

or:

```python
print(Child.__mro__)
```

### MRO

```text
Child → Parent1 → Parent2 → object
```

# ==========================================================

# HOW super() CHAIN WORKS

# ==========================================================

When we create:

```python
child2 = Child()
```

Python starts from:

```text
Child.__init__()
```

Inside `Child`:

```python
super().__init__()
```

calls the next class according to the MRO:

```text
Parent1.__init__()
```

Inside `Parent1`:

```python
super().__init__()
```

calls:

```text
Parent2.__init__()
```

Inside `Parent2`:

```python
super().__init__()
```

calls:

```text
object.__init__()
```

Then execution returns back.

Because the `print()` statements come after
`super().__init__()`, the output becomes:

```text
Parent2 constructor
Parent1 constructor
Child constructor
```

# ==========================================================

# IMPORTANT NOTE

# ==========================================================

Do NOT think:

```text
super() = automatically call all parent classes
```

Instead, remember:

```text
super()
   ↓
calls the next method according to MRO
```

For example:

```text
Child
  ↓
Parent1
  ↓
Parent2
  ↓
object
```

Each class should use:

```python
super().__init__()
```

if we want the constructor chain to continue through
the MRO.

# ==========================================================

# CONSTRUCTOR SUMMARY

# ==========================================================

```text
Constructor
     ↓
Used to initialize an object
     ↓
__init__()
```

### Default

```python
class Student:
    pass
```

No explicit `__init__()` is defined.

### Non-Parameterized

```python
class Student:

    def __init__(self):
        self.name = "Faruk"
```

Only `self` is used.

### Parameterized

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Additional arguments are accepted.

# ==========================================================

# DESTRUCTOR

# ==========================================================

## What is a Destructor?

In Python, `__del__()` is commonly referred to as a destructor.

It is a special method that may be called when an object is
being finalized.

### Syntax

```python
def __del__(self):
    ...
```

# ==========================================================

# DESTRUCTOR EXAMPLE

# ==========================================================

```python
class Employee:

    def __init__(self, name):
        self.name = name
        print(f"Employee {self.name} is created")

    def __del__(self):
        print(f"Employee {self.name} is deleted")


if __name__ == "__main__":

    # Creating object
    emp = Employee("John")

    # Removing the reference
    del emp
```

### Possible Output

```text
Employee John is created
Employee John is deleted
```

# ==========================================================

# IMPORTANT del NOTE

# ==========================================================

This statement:

```python
del emp
```

does NOT literally mean:

```text
Destroy the object immediately
```

It means that the reference named `emp` is removed.

If there are no other references to the object, the object
may become eligible for garbage collection/finalization.

For example:

```python
emp1 = Employee("John")

emp2 = emp1

del emp1
```

The object is still referenced by:

```python
emp2
```

So the object is not necessarily finalized at `del emp1`.

Only when the object is no longer reachable may it become
eligible for garbage collection.

# ==========================================================

# **init** vs **del**

# ==========================================================

| Method       | Purpose                                                    |
| ------------ | ---------------------------------------------------------- |
| `__init__()` | Initializes an object                                      |
| `__del__()`  | Finalization hook that may run when an object is finalized |

Example:

```text
Object Creation
       ↓
   __init__()
       ↓
Object is used
       ↓
Object becomes unreachable
       ↓
   __del__() may run
```

# ==========================================================

# **doc** IN PYTHON

# ==========================================================

## What is **doc**?

`__doc__` is a special built-in attribute that contains the
docstring of a module, class, function, or method.

A docstring is a string written inside triple quotes:

```python
"""This is a docstring."""
```

The `__doc__` attribute is used to access that docstring.

# ==========================================================

# CLASS DOCSTRING

# ==========================================================

### Example

```python
class Person:
    """Person class. This is a docstring."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


if __name__ == "__main__":

    # Creating object
    person = Person("John", 30)

    # Accessing class docstring through object
    print(person.__doc__)

    # Accessing class docstring through class
    print(Person.__doc__)
```

### Output

```text
Person class. This is a docstring.
Person class. This is a docstring.
```

Both work:

```python
person.__doc__
```

and:

```python
Person.__doc__
```

# ==========================================================

# **doc** USING CLASS NAME

# ==========================================================

We can access a class's docstring using:

```python
Person.__doc__
```

### Example

```python
class Student:
    """This is the Student class."""


print(Student.__doc__)
```

### Output

```text
This is the Student class.
```

# ==========================================================

# **doc** USING OBJECT

# ==========================================================

We can also access the class docstring through an object:

```python
student = Student()

print(student.__doc__)
```

### Output

```text
This is the Student class.
```

The object can access the class's docstring through
attribute lookup.

# ==========================================================

# METHOD DOCSTRING

# ==========================================================

Docstrings can also be written inside methods.

```python
class Person:
    """Represents a person."""

    def __init__(self, name, age):
        """Initialize a Person object."""
        self.name = name
        self.age = age

    def showInfo(self):
        """Display person information."""
        print(f"Name: {self.name}, Age: {self.age}")
```

We can access the docstrings like this:

```python
print(Person.__doc__)
print(Person.__init__.__doc__)
print(Person.showInfo.__doc__)
```

### Output

```text
Represents a person.
Initialize a Person object.
Display person information.
```

# ==========================================================

# FUNCTION DOCSTRING

# ==========================================================

Docstrings are also available for normal functions.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add.__doc__)
```

### Output

```text
Return the sum of two numbers.
```

# ==========================================================

# MODULE DOCSTRING

# ==========================================================

A module can also have a docstring.

The module docstring should normally be written at the
beginning of the Python file.

### Example

```python
"""
This module demonstrates Python docstrings.
"""


class Person:
    """Represents a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

The module docstring can be accessed using:

```python
print(__doc__)
```

# ==========================================================

# COMPLETE **doc** EXAMPLE

# ==========================================================

```python
class Person:
    """Person class. Represents a person."""

    def __init__(self, name, age):
        """Initialize a Person object."""
        self.name = name
        self.age = age

    def __str__(self):
        """Return a string representation of the object."""
        return f"Person(name={self.name}, age={self.age})"

    def showInfo(self):
        """Display person information."""
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":

    # Create object
    person = Person("John", 30)

    # Print object
    print(person)

    # Access class docstring through object
    print(person.__doc__)

    # Access class docstring through class
    print(Person.__doc__)

    # Access __init__() docstring
    print(Person.__init__.__doc__)

    # Access __str__() docstring
    print(Person.__str__.__doc__)

    # Access showInfo() docstring
    print(Person.showInfo.__doc__)
```

### Output

```text
Person(name=John, age=30)

Person class. Represents a person.

Person class. Represents a person.

Initialize a Person object.

Return a string representation of the object.

Display person information.
```

# ==========================================================

# QUICK SUMMARY

# ==========================================================

```text
__doc__
   ↓
Accesses the docstring
```

### Class

```python
Person.__doc__
```

### Object

```python
person.__doc__
```

### Constructor

```python
Person.__init__.__doc__
```

### Method

```python
Person.showInfo.__doc__
```

### Function

```python
add.__doc__
```

### Module

```python
__doc__
```

# ==========================================================

# COMMENT vs DOCSTRING

# ==========================================================

A docstring is NOT the same as a normal comment.

### Comment

```python
# This is a comment
```

Comments are mainly written for developers and are not stored
as the object's documentation.

### Docstring

```python
"""This is a docstring."""
```

Docstrings are stored by Python and can be accessed using
the `__doc__` attribute.

Therefore:

```text
Comment
   ↓
# ...

Docstring
   ↓
""" ... """
   ↓
__doc__
```

# ==========================================================

# FINAL SUMMARY

# ==========================================================

## **new**()

```text
Creates the object
```

## **init**()

```text
Initializes the object
```

## super()

```text
Calls the next method according to MRO
```

## MRO

```text
Method Resolution Order
```

Example:

```text
Child → Parent1 → Parent2 → object
```

## **del**()

```text
Finalization hook
```

## **doc**

```text
Provides access to a docstring
```

# ==========================================================

# EASY WAY TO REMEMBER

# ==========================================================

```text
__new__()
    ↓
Creates Object

__init__()
    ↓
Initializes Object

super()
    ↓
Follows MRO

__del__()
    ↓
Finalization Hook

__doc__
    ↓
Accesses Docstring
```

# ==========================================================

# ONE-LINE DEFINITIONS

# ==========================================================

**Constructor:**

> A special mechanism used to initialize an object's state.

**`__init__()`:**

> The method commonly used in Python to initialize an object.

**Parameterized Constructor:**

> An `__init__()` method that accepts additional arguments.

**Non-Parameterized Constructor:**

> An `__init__()` method that accepts no additional arguments beyond `self`.

**`super()`:**

> A mechanism for accessing the next class in the MRO.

**MRO:**

> The order in which Python searches classes for methods and attributes.

**Destructor:**

> `__del__()` is a finalization hook that may run when an object is being finalized.

**`__doc__`:**

> A special attribute used to access the docstring of a module, class, function, or method.

"""