"""
# Python OOP — Full Notes

## 1. What is OOP?

**OOP = Object-Oriented Programming**

OOP is a programming paradigm where programs are designed around **classes and objects**.

Real-world examples:

* Student
* Car
* Bank Account
* Employee
* Book
* Mobile

---

# 2. What is a Class?

A **class is a blueprint or template for creating objects**.

```python
class Student:
    pass
```

Here, `Student` is a class.

A class defines the structure and behavior that its objects can have.

---

# 3. What is an Object?

An **object is an instance of a class**.

```python
class Student:
    pass


s1 = Student()
s2 = Student()
```

Here:

```text
Student → Class
s1      → Object
s2      → Object
```

Multiple objects can be created from the same class.

---

# 4. Class vs Object

| Class                  | Object               |
| ---------------------- | -------------------- |
| Blueprint              | Instance             |
| Template               | Real instance        |
| Used to create objects | Created from a class |
| `Student`              | `s1`, `s2`           |

Example:

```python
class Student:
    pass


s1 = Student()
s2 = Student()
```

---

# 5. How to Create an Object

Basic syntax:

```python
object_name = ClassName()
```

Example:

```python
class Student:
    pass


s1 = Student()
```

Here:

```text
Student() → Creates an object
s1        → Reference to the object
```

---

# 6. Constructor

In Python, `__init__()` is used to initialize an object.

```python
class Student:

    def __init__(self):
        print("Student object created")


s1 = Student()
```

Output:

```text
Student object created
```

The `__init__()` method is automatically called when an object is created.

---

# 7. Constructor with Parameters

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Faruk", 25)

print(s1.name)
print(s1.age)
```

Output:

```text
Faruk
25
```

---

# 8. What is `self`?

`self` is a reference to the **current object**.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

When we create:

```python
s1 = Student("Faruk")
```

`self` refers to the current object, `s1`.

Shortcut:

```text
self → Current Object
```

---

# 9. Instance Variable

A variable that belongs to a particular object is called an **instance variable**.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Here:

```python
self.name
```

is an instance variable.

Example:

```python
s1 = Student("Faruk")
s2 = Student("Rahim")

print(s1.name)
print(s2.name)
```

Output:

```text
Faruk
Rahim
```

Each object can have different instance data.

---

# 10. Class Variable

A variable defined at the class level is called a **class variable**.

```python
class Student:

    school = "TMSS"

    def __init__(self, name):
        self.name = name
```

Here:

```python
school
```

is a class variable.

Access:

```python
print(Student.school)
```

It can also usually be accessed through an instance:

```python
s1 = Student("Faruk")

print(s1.school)
```

---

# 11. Instance Variable vs Class Variable

```python
class Student:

    school = "TMSS"

    def __init__(self, name):
        self.name = name
```

Here:

```text
school → Class Variable
name   → Instance Variable
```

### Instance Variable

```python
self.name
```

* Belongs to an individual object
* Can have different values for different objects
* Usually accessed using `self`

### Class Variable

```python
Student.school
```

* Belongs to the class
* Usually shared by instances unless an instance overrides it
* Can be accessed through the class

---

# 12. Instance Method

A method that operates on an object is called an **instance method**.

It normally takes `self` as its first parameter.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)
```

Usage:

```python
s1 = Student("Faruk")

s1.show()
```

Output:

```text
Faruk
```

---

# 13. Class Method

A class method operates on class-level data.

The `@classmethod` decorator is used.

```python
class Student:

    school = "TMSS"

    @classmethod
    def change_school(cls, name):
        cls.school = name
```

Usage:

```python
Student.change_school("ABC School")

print(Student.school)
```

Output:

```text
ABC School
```

Shortcut:

```text
cls → Current Class
```

---

# 14. Static Method

A static method does not require `self` or `cls`.

The `@staticmethod` decorator is used.

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

Usage:

```python
result = Math.add(5, 3)

print(result)
```

Output:

```text
8
```

---

# 15. Three Types of Methods

```text
Instance Method
      ↓
    self
      ↓
Operates on object data


Class Method
      ↓
     cls
      ↓
Operates on class data


Static Method
      ↓
No self / cls
      ↓
Utility operation
```

Example:

```python
class Student:

    school = "TMSS"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def show(self):
        print(self.name)

    # Class Method
    @classmethod
    def change_school(cls, name):
        cls.school = name

    # Static Method
    @staticmethod
    def info():
        print("This is Student class.")
```

---

# 16. How to Access an Object

### Object

```python
s1
```

### Attribute

```python
s1.name
```

### Method

```python
s1.show()
```

General syntax:

```text
object.attribute
object.method()
```

---

# 17. Delete Object / Attribute

The `del` keyword can be used to delete a reference or an attribute.

### Delete a reference

```python
s1 = Student("Faruk")

del s1
```

### Delete an attribute

```python
del s1.name
```

After deleting:

```python
print(s1.name)
```

will raise an `AttributeError`.

Note:

`del s1` removes the name/reference `s1`. It does not necessarily mean the object is immediately destroyed. Python manages object lifetime through reference counting and garbage collection.

---

# 18. Four Pillars of OOP

The four fundamental pillars of OOP are:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

---

# 19. Encapsulation

**Encapsulation** means bundling data and methods inside a class and controlling access to the data.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

Here:

```python
self.__balance
```

uses Python's private-name convention through name mangling.

---

# 20. Access Conventions in Python

### Public

```python
self.name
```

A public attribute.

### Protected Convention

```python
self._name
```

A single underscore conventionally indicates that an attribute is intended for internal/protected use.

### Private Name Mangling

```python
self.__name
```

Python applies name mangling to double-underscore attributes.

Example:

```python
class Student:

    def __init__(self):
        self.__name = "Faruk"
```

Conceptually, Python transforms the name to:

```text
__name
   ↓
_Student__name
```

---

# 21. Inheritance

**Inheritance** allows a child class to reuse attributes and methods from a parent class.

```python
class Animal:

    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()
```

Output:

```text
Animal speaks
```

Here:

```text
Animal → Parent/Base Class
Dog    → Child/Derived Class
```

---

# 22. Single Inheritance

One child class inherits from one parent class.

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

Diagram:

```text
Animal
   ↓
  Dog
```

---

# 23. Multilevel Inheritance

Inheritance across multiple levels.

```python
class Animal:
    pass


class Dog(Animal):
    pass


class Puppy(Dog):
    pass
```

Diagram:

```text
Animal
   ↓
 Dog
   ↓
Puppy
```

---

# 24. Multiple Inheritance

A class inherits from multiple parent classes.

```python
class Father:

    def skills(self):
        print("Programming")


class Mother:

    def talent(self):
        print("Cooking")


class Child(Father, Mother):
    pass
```

Usage:

```python
c = Child()

c.skills()
c.talent()
```

---

# 25. Hierarchical Inheritance

One parent class has multiple child classes.

```python
class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

Diagram:

```text
       Animal
       /    \
     Dog    Cat
```

---

# 26. Hybrid Inheritance

A combination of two or more inheritance patterns is called **Hybrid Inheritance**.

---

# 27. `super()`

`super()` is used to access methods or the constructor of a parent class.

```python
class Animal:

    def __init__(self):
        print("Animal constructor")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog constructor")


dog = Dog()
```

Output:

```text
Animal constructor
Dog constructor
```

---

# 28. Method Overriding

When a child class provides its own implementation of a method already defined in the parent class, it is called **method overriding**.

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()
```

Output:

```text
Bark
```

---

# 29. Polymorphism

**Poly = Many**

**Morphism = Forms**

Polymorphism means the same interface or method can have different behavior for different objects.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```text
Bark
Meow
```

The same:

```python
animal.sound()
```

produces different behavior.

---

# 30. Duck Typing

Python often focuses on what an object can do rather than its exact type.

```python
class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")


def make_sound(animal):
    animal.speak()


make_sound(Dog())
make_sound(Cat())
```

---

# 31. Abstraction

**Abstraction** means hiding unnecessary implementation details and exposing the essential interface.

Python provides the `abc` module for implementing abstraction.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Child class:

```python
class Dog(Animal):

    def sound(self):
        print("Bark")
```

---

# 32. Abstract Class

A class that contains one or more abstract methods can be an **abstract class**.

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

A subclass must implement the abstract methods before it can be instantiated.

---

# 33. Encapsulation vs Abstraction

| Encapsulation                 | Abstraction                              |
| ----------------------------- | ---------------------------------------- |
| Bundles data and methods      | Hides implementation details             |
| Related to controlling access | Related to exposing essential interfaces |
| `_` and `__` may be used      | `ABC` and `@abstractmethod` may be used  |

Shortcut:

```text
Encapsulation → How to organize/protect data?

Abstraction → What should the user see?
```

---

# 34. Constructor vs Method

### Constructor / Initializer

```python
def __init__(self):
```

Used to initialize an object.

### Normal Method

```python
def show(self):
```

Must normally be called explicitly.

```python
s1.show()
```

---

# 35. `__str__()`

`__str__()` provides a user-friendly string representation of an object.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


s1 = Student("Faruk")

print(s1)
```

Output:

```text
Faruk
```

---

# 36. `__repr__()`

`__repr__()` is generally intended to provide an unambiguous or developer-oriented representation.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name!r})"
```

---

# 37. Magic / Dunder Methods

Special methods whose names start and end with double underscores are commonly called **dunder methods**.

Examples:

```text
__init__
__str__
__repr__
__len__
__eq__
__add__
```

---

# 38. Operator Overloading

Special methods can be used to define how operators work with custom objects.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2

print(n3.value)
```

Output:

```text
30
```

Here:

```python
n1 + n2
```

uses:

```python
__add__()
```

---

# 39. `__eq__()`

`__eq__()` can customize equality comparison between objects.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
```

---

# 40. Property

The `@property` decorator allows a method to be accessed like an attribute.

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

Usage:

```python
s1 = Student("Faruk")

print(s1.name)
```

---

# 41. Setter

A setter can be used to control how a property's value is changed.

```python
class Student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative")
```

Usage:

```python
s1 = Student(20)

print(s1.age)

s1.age = 25
```

---

# 42. Composition

Composition is a relationship where one class contains an object of another class.

```python
class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
```

Here:

```text
Car
 ↓
Engine
```

Car **HAS-A** Engine.

---

# 43. Aggregation

Aggregation is a relationship where one object uses or contains another object, while the contained object can exist independently.

```python
class Teacher:
    pass


class Department:

    def __init__(self, teacher):
        self.teacher = teacher
```

The `Teacher` object is created outside and passed into `Department`.

---

# 44. Association

Association is a relationship between independent objects.

Examples:

```text
Teacher ↔ Student
Doctor ↔ Patient
Customer ↔ Bank
```

---

# 45. Inheritance vs Composition

### Inheritance

**IS-A relationship**

```text
Dog IS-A Animal
```

```python
class Dog(Animal):
    pass
```

### Composition

**HAS-A relationship**

```text
Car HAS-A Engine
```

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

Shortcut:

```text
Inheritance → IS-A
Composition → HAS-A
```

---

# 46. Method Resolution Order (MRO)

MRO determines the order in which Python searches for methods and attributes in an inheritance hierarchy.

Example:

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
```

Conceptually:

```text
C → B → A → object
```

---

# 47. `object` Class

Python classes ultimately participate in an inheritance hierarchy rooted at the built-in `object` class.

```python
class Student:
    pass
```

Conceptually:

```text
Student
   ↓
object
```

---

# 48. `isinstance()`

`isinstance()` checks whether an object is an instance of a class.

```python
class Student:
    pass


s1 = Student()

print(isinstance(s1, Student))
```

Output:

```text
True
```

---

# 49. `issubclass()`

`issubclass()` checks whether one class is a subclass of another.

```python
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
```

Output:

```text
True
```

---

# 50. Complete OOP Example

```python
from abc import ABC, abstractmethod


class Person(ABC):

    species = "Human"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @abstractmethod
    def introduce(self):
        pass


class Student(Person):

    school = "TMSS"

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(
            f"My name is {self.name}. "
            f"I am {self._age} years old."
        )

    @classmethod
    def change_school(cls, school):
        cls.school = school

    @staticmethod
    def info():
        print("This is Student class.")


student = Student("Faruk", 25, 101)

student.introduce()

print(student.name)
print(student.student_id)

Student.change_school("ABC School")

print(Student.school)

Student.info()
```

---

# 51. Important OOP Concepts

```text
Class
Object
Constructor
self
Instance Variable
Class Variable

Instance Method
Class Method
Static Method

Encapsulation
Inheritance
Polymorphism
Abstraction

Method Overriding
super()
Multiple Inheritance
MRO

Magic Methods
__init__()
__str__()
__repr__()
__eq__()
__add__()

@property
Setter

Composition
Aggregation
Association

isinstance()
issubclass()
```

---

# 52. Quick Revision

```text
Class
    ↓
Blueprint

Object
    ↓
Instance of Class

self
    ↓
Current Object

cls
    ↓
Current Class

__init__()
    ↓
Initialize Object

Instance Variable
    ↓
Object-specific Data

Class Variable
    ↓
Class-level Data

Instance Method
    ↓
self

Class Method
    ↓
@classmethod + cls

Static Method
    ↓
@staticmethod

Encapsulation
    ↓
Bundle + Control Access

Inheritance
    ↓
Reuse / IS-A

Polymorphism
    ↓
Same Interface, Different Behavior

Abstraction
    ↓
Hide Implementation Details

Composition
    ↓
HAS-A

Inheritance
    ↓
IS-A
```

---

# 53. OOP Learning Roadmap

```text
1. Class
   ↓
2. Object
   ↓
3. __init__()
   ↓
4. self
   ↓
5. Instance Variable
   ↓
6. Class Variable
   ↓
7. Instance Method
   ↓
8. Class Method
   ↓
9. Static Method
   ↓
10. Encapsulation
    ↓
11. Inheritance
    ↓
12. super()
    ↓
13. Method Overriding
    ↓
14. Polymorphism
    ↓
15. Abstraction
    ↓
16. Magic Methods
    ↓
17. Property / Setter
    ↓
18. Composition
    ↓
19. MRO
    ↓
20. OOP Projects + Practice
```

---

# 54. One-Line Definition

**Class** is a blueprint.

**Object** is an instance of a class.

**Encapsulation, Inheritance, Polymorphism, and Abstraction** are the four fundamental pillars of OOP.

---

# 55. Most Important Interview Questions

1. What is OOP?
2. What is a class?
3. What is an object?
4. What is the difference between class and object?
5. What is `self`?
6. What is `__init__()`?
7. What is an instance variable?
8. What is a class variable?
9. What is an instance method?
10. What is a class method?
11. What is a static method?
12. Difference between `self` and `cls`?
13. What are the four pillars of OOP?
14. What is encapsulation?
15. What is inheritance?
16. What are the types of inheritance?
17. What is `super()`?
18. What is method overriding?
19. What is polymorphism?
20. What is duck typing?
21. What is abstraction?
22. What is an abstract class?
23. What are magic/dunder methods?
24. What is operator overloading?
25. What is `__str__()`?
26. What is `__repr__()`?
27. What is `@property`?
28. What is composition?
29. Difference between inheritance and composition?
30. What is MRO?
31. What is `isinstance()`?
32. What is `issubclass()`?
33. What is name mangling?
34. What is the difference between public, protected, and private conventions in Python?
35. What is the difference between aggregation and composition?
"""