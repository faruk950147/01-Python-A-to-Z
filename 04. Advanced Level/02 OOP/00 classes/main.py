"""
# Python OOP — Complete Notes

## 1. What is OOP?

**OOP = Object-Oriented Programming**

OOP is a programming paradigm where programs are organized around **objects and classes**.

Common real-world examples:

* Student
* Employee
* Car
* Bank Account
* Book
* Mobile
* Product

The main concepts of OOP are:

```text
Class
Object
Encapsulation
Inheritance
Polymorphism
Abstraction
```

---

# 2. Class

A **class** is a blueprint/template used to create objects.

```python
class Student:
    pass
```

Here:

```text
Student → Class
```

A class defines attributes and methods that its objects can have.

Important:

A class in Python is itself an object.

```python
class Student:
    pass

print(type(Student))
```

Output:

```text
<class 'type'>
```

So:

```text
Student
   ↓
Class Object
   ↓
type
```

---

# 3. Object

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

| Class                      | Object                         |
| -------------------------- | ------------------------------ |
| Blueprint/template         | Instance                       |
| Defines structure/behavior | Represents a concrete instance |
| Used to create objects     | Created from a class           |
| `Student`                  | `s1`, `s2`                     |

Example:

```python
class Student:
    pass

s1 = Student()
s2 = Student()
```

---

# 5. Creating an Object

General syntax:

```python
object_name = ClassName()
```

Example:

```python
class Student:
    pass

s1 = Student()
```

Conceptually:

```text
Student()
   ↓
New instance

s1
   ↓
Reference to that instance
```

---

# 6. `__init__()` Method

`__init__()` is a special method used to **initialize an instance after it has been created**.

```python
class Student:

    def __init__(self):
        print("Student initialized")


s1 = Student()
```

Output:

```text
Student initialized
```

### Important terminology

It is common to call `__init__()` a "constructor" in beginner materials.

Technically:

```text
__new__() → creates the instance
__init__() → initializes the instance
```

For normal Python programming, you will usually work with `__init__()`.

---

# 7. `__init__()` with Parameters

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

`self` is the conventional name for the reference to the **current instance**.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

When:

```python
s1 = Student("Faruk")
```

is executed, conceptually:

```text
self → s1
```

And:

```python
self.name
```

refers to the `name` attribute of that instance.

---

# 9. `self` is a Convention

Python does not require the parameter to literally be named `self`.

For example:

```python
class Student:

    def show(current):
        print("Hello")
```

This works, but using `self` is the standard Python convention.

Use:

```python
def show(self):
```

not unusual names.

---

# 10. Instance Variable / Instance Attribute

An instance variable/attribute belongs to a particular object.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Here:

```python
self.name
```

is an instance attribute.

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

Each object has its own instance data.

---

# 11. Class Variable / Class Attribute

A variable defined directly inside the class body is a class attribute.

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

is a class attribute.

Access:

```python
print(Student.school)
```

An instance can also access it:

```python
s1 = Student("Faruk")

print(s1.school)
```

Python first looks for an instance attribute and then follows the attribute lookup rules, including the class.

---

# 12. Instance Attribute vs Class Attribute

```python
class Student:

    school = "TMSS"

    def __init__(self, name):
        self.name = name
```

Here:

```text
school → Class Attribute
name   → Instance Attribute
```

### Instance Attribute

```python
self.name
```

* Belongs to an instance.
* Different objects can have different values.
* Usually accessed through an instance.

### Class Attribute

```python
Student.school
```

* Defined on the class.
* Shared through the class unless an instance provides an overriding attribute.
* Useful for data/behavior common to the class.

---

# 13. Instance Method

An instance method normally takes `self` as its first parameter.

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

Conceptually:

```python
s1.show()
```

is equivalent to:

```python
Student.show(s1)
```

---

# 14. Class Method

A class method receives the class as its first argument.

Use:

```python
@classmethod
```

Example:

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

Convention:

```text
self → Current Instance
cls  → Current Class
```

---

# 15. Static Method

A static method does not automatically receive `self` or `cls`.

Use:

```python
@staticmethod
```

Example:

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

Usage:

```python
print(Math.add(5, 3))
```

Output:

```text
8
```

Use a static method when the operation logically belongs to the class but does not need instance or class state.

---

# 16. Three Main Method Types

| Method          | First Parameter    | Access   | Main Purpose            |
| --------------- | ------------------ | -------- | ----------------------- |
| Instance Method | `self`             | Instance | Instance behavior       |
| Class Method    | `cls`              | Class    | Class-level behavior    |
| Static Method   | None automatically | Neither  | Utility/helper behavior |

Memory trick:

```text
Instance → self → Object

Class → cls → Class

Static → No automatic self/cls → Utility
```

---

# 17. All Three in One Class

```python
class Student:

    school = "TMSS"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show(self):
        print(self.name)

    # Class method
    @classmethod
    def change_school(cls, school):
        cls.school = school

    # Static method
    @staticmethod
    def info():
        print("This is Student class.")
```

---

# 18. Alternative Constructor

One important use of `@classmethod` is creating an **alternative constructor**.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown", 0)
```

Usage:

```python
student = Student.create_anonymous()

print(student.name)
print(student.age)
```

Output:

```text
Unknown
0
```

Why `cls(...)`?

Because it creates an instance of the current class and also works properly with subclasses.

---

# 19. Method Binding

When an instance method is accessed through an instance, Python creates a **bound method**.

```python
class Student:

    def show(self):
        print("Hello")


s = Student()

s.show()
```

Conceptually:

```python
Student.show(s)
```

So:

```text
s.show
   ↓
Bound Method
   ↓
Method + s instance
```

---

# 20. `Student.show` vs `s.show`

### Through class

```python
Student.show
```

This accesses the function descriptor through the class.

### Through instance

```python
s.show
```

This produces a bound method with `s` automatically supplied as `self`.

Python 3 does not normally call `Student.show` an "unbound method"; it is simply a function accessed through the class.

---

# 21. Method Overloading

Traditional method overloading means:

```text
Same method name
+
Different parameter lists
```

For example:

```text
add(a)
add(a, b)
add(a, b, c)
```

Languages such as Java and C++ support traditional method overloading.

Python does **not** support traditional signature-based method overloading directly.

Example:

```python
class Calculator:

    def add(self, a):
        return a

    def add(self, a, b):
        return a + b
```

The second definition replaces the first one in the class namespace.

Therefore:

```python
calc.add(5)
```

would raise a `TypeError` because the active `add()` expects two arguments besides `self`.

---

# 22. Alternatives to Traditional Overloading

Python commonly uses:

* Default arguments
* `*args`
* `**kwargs`
* Conditional logic
* `functools.singledispatch` in appropriate cases

Example using default arguments:

```python
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))
```

Output:

```text
5
15
30
```

This is flexible argument handling, not traditional method overloading.

---

# 23. `*args`

`*args` collects extra positional arguments into a tuple.

```python
class Calculator:

    def add(self, *args):
        return sum(args)


calc = Calculator()

print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))
```

Conceptually:

```python
calc.add(5, 10, 15)
```

creates:

```python
args = (5, 10, 15)
```

---

# 24. `**kwargs`

`**kwargs` collects extra keyword arguments into a dictionary.

```python
class Student:

    def show(self, **kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)


student = Student()

student.show(
    name="Faruk",
    age=22,
    department="CSE"
)
```

Conceptually:

```text
kwargs
   ↓
Dictionary
```

---

# 25. `*args` vs `**kwargs`

```text
*args
 ↓
Positional arguments
 ↓
Tuple


**kwargs
 ↓
Keyword arguments
 ↓
Dictionary
```

---

# 26. Method Overriding

Method overriding happens when a child class provides its own implementation of an inherited method.

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

Requirements:

1. There is an inheritance relationship.
2. Parent provides/inherits the method.
3. Child defines a method with the same name.
4. The child implementation is selected for normal instance dispatch.

---

# 27. `super()`

`super()` gives access to the **next implementation in the MRO**.

Simple example:

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Bark")


dog = Dog()
dog.sound()
```

Output:

```text
Animal sound
Bark
```

In this simple hierarchy:

```text
Dog.sound()
    ↓
super().sound()
    ↓
Animal.sound()
```

Important:

`super()` should not be thought of as simply "parent".

It follows Python's **Method Resolution Order (MRO)**.

---

# 28. Polymorphism

Polymorphism means that the same interface or operation can produce different behavior depending on the object.

Example:

```python
class Dog:

    def speak(self):
        return "Woof!"


class Cat:

    def speak(self):
        return "Meow!"


def make_sound(animal):
    print(animal.speak())


make_sound(Dog())
make_sound(Cat())
```

Output:

```text
Woof!
Meow!
```

Same interface:

```python
animal.speak()
```

Different behavior:

```text
Dog → Woof!
Cat → Meow!
```

---

# 29. Duck Typing

Duck typing is a Python style where code often focuses on whether an object supports the required operation rather than checking its exact class.

Classic idea:

```text
"If it behaves like a duck,
we can use it like a duck."
```

Example:

```python
class Duck:

    def quack(self):
        print("Quack!")


class Person:

    def quack(self):
        print("Person is quacking!")


def make_it_quack(thing):
    thing.quack()


make_it_quack(Duck())
make_it_quack(Person())
```

The function does not care whether the object is a `Duck` or `Person`.

It only requires:

```python
thing.quack()
```

---

# 30. Duck Typing and `AttributeError`

If the required operation does not exist:

```python
class Car:
    pass


def make_it_quack(thing):
    thing.quack()


car = Car()

make_it_quack(car)
```

Python normally raises:

```text
AttributeError
```

because `Car` does not provide `quack()`.

---

# 31. Dynamic Typing vs Duck Typing

These are different concepts.

### Dynamic Typing

Python variables can refer to objects of different types during runtime.

```python
x = 10
x = "Hello"
x = [1, 2, 3]
```

### Duck Typing

Code focuses on required behavior rather than requiring a particular concrete type.

```python
def process(obj):
    obj.run()
```

The function assumes that `obj` supports `run()`.

Memory:

```text
Dynamic Typing
→ Type determined/checked at runtime

Duck Typing
→ Required behavior matters
```

---

# 32. Polymorphism with Collections

Different objects can be stored in the same collection and processed through the same interface.

```python
class Dog:

    def speak(self):
        return "Woof!"


class Cat:

    def speak(self):
        return "Meow!"


class Bird:

    def speak(self):
        return "Chirp!"


animals = [
    Dog(),
    Cat(),
    Bird()
]

for animal in animals:
    print(animal.speak())
```

Output:

```text
Woof!
Meow!
Chirp!
```

The loop does not need separate logic for each concrete class.

---

# 33. Polymorphism + Abstract Base Class

Python provides the `abc` module for abstract base classes.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

Concrete subclasses:

```python
class Dog(Animal):

    def speak(self):
        return "Woof!"


class Cat(Animal):

    def speak(self):
        return "Meow!"


class Bird(Animal):

    def speak(self):
        return "Chirp!"
```

Collection:

```python
animals = [
    Dog(),
    Cat(),
    Bird()
]

for animal in animals:
    print(animal.speak())
```

Output:

```text
Woof!
Meow!
Chirp!
```

---

# 34. Adding a New Class

```python
class Cow(Animal):

    def speak(self):
        return "Moo!"
```

Now:

```python
animals.append(Cow())
```

The same loop still works:

```python
for animal in animals:
    print(animal.speak())
```

Output:

```text
Woof!
Meow!
Chirp!
Moo!
```

The loop itself did not need to be modified.

This demonstrates the practical benefit of programming against a common interface.

---

# 35. Abstraction

**Abstraction** means exposing essential behavior while hiding unnecessary implementation details.

Python provides:

```python
abc
ABC
@abstractmethod
```

Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

---

# 36. Abstract Class

An abstract base class can define methods that subclasses are required to implement.

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

A subclass should implement the abstract method before it can normally be instantiated.

```python
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2
```

---

# 37. Encapsulation

Encapsulation means keeping related data and behavior together and controlling how state is accessed or modified.

Example:

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

uses Python's **name-mangling mechanism**.

---

# 38. Public, Protected Convention, Private Name Mangling

Python does not have Java/C++-style access modifiers in the same strict sense.

### Public

```python
self.name
```

Normal public attribute.

### Single Underscore

```python
self._name
```

Conventionally means:

```text
Internal / non-public API
```

It is not enforced as private.

### Double Underscore

```python
self.__name
```

Python applies name mangling.

Example:

```python
class Student:

    def __init__(self):
        self.__name = "Faruk"
```

Conceptually:

```text
__name
   ↓
_Student__name
```

Important:

`__name` is **not truly inaccessible/private**. Name mangling mainly helps avoid accidental name collisions, especially in inheritance.

---

# 39. `_name` vs `__name`

```text
name
 ↓
Public


_name
 ↓
Internal-use convention


__name
 ↓
Name mangling
```

Do not describe:

```python
__name
```

as absolutely "private" in the same sense as languages with enforced private access.

---

# 40. Four Fundamental OOP Concepts

The commonly taught four pillars are:

```text
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
```

Memory:

```text
Encapsulation
→ Bundle + control access

Inheritance
→ Reuse / IS-A

Polymorphism
→ Same interface, different behavior

Abstraction
→ Essential interface, hidden implementation details
```

---

# 41. `__str__()`

`__str__()` provides a user-friendly string representation.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Faruk")

print(student)
```

Output:

```text
Faruk
```

`print(obj)` generally uses `str(obj)`, which can invoke `obj.__str__()`.

---

# 42. `__repr__()`

`__repr__()` is generally intended to provide a useful, developer-oriented representation.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name!r})"
```

Example:

```python
student = Student("Faruk")

print(repr(student))
```

Possible output:

```text
Student(name='Faruk')
```

---

# 43. `__str__()` vs `__repr__()`

```text
__str__
   ↓
User-friendly representation

__repr__
   ↓
Developer/debugging representation
```

A good `repr` is often useful for understanding exactly what object/value is being represented.

---

# 44. Magic / Dunder Methods

Special methods are commonly called **dunder methods** because their names begin and end with double underscores.

Examples:

```python
__init__
__str__
__repr__
__len__
__eq__
__add__
__call__
```

They allow Python syntax and built-in operations to interact with user-defined objects.

---

# 45. Operator Overloading

Special methods allow classes to define behavior for operators.

Example:

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
```

Usage:

```python
n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2

print(n3.value)
```

Output:

```text
30
```

Conceptually:

```python
n1 + n2
```

dispatches through the appropriate addition protocol, involving:

```python
__add__()
```

---

# 46. `__eq__()`

`__eq__()` can define equality behavior for objects.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.name == other.name
```

Usage:

```python
s1 = Student("Faruk")
s2 = Student("Faruk")

print(s1 == s2)
```

Output:

```text
True
```

Without a custom equality implementation, user-defined objects generally use identity-based equality inherited from `object`.

---

# 47. `@property`

`@property` allows a method to be accessed using attribute syntax.

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
student = Student("Faruk")

print(student.name)
```

Notice:

```python
student.name
```

instead of:

```python
student.name()
```

---

# 48. Property Setter

A setter controls how a property's value is assigned.

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
student = Student(20)

print(student.age)

student.age = 25

print(student.age)
```

Invalid value:

```python
student.age = -5
```

raises:

```text
ValueError
```

---

# 49. Composition

Composition represents a **HAS-A** relationship where an object contains another object as part of its implementation.

Example:

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
HAS-A
 ↓
Engine
```

---

# 50. Aggregation

Aggregation is a looser HAS-A relationship where the contained object can exist independently.

```python
class Teacher:
    pass


class Department:

    def __init__(self, teacher):
        self.teacher = teacher
```

The `Teacher` object is created outside:

```python
teacher = Teacher()

department = Department(teacher)
```

The teacher can exist independently of the department object.

---

# 51. Association

Association means objects are related/interact with each other without necessarily implying ownership.

Examples:

```text
Teacher ↔ Student
Doctor ↔ Patient
Customer ↔ Bank
```

Association is a broad relationship concept.

---

# 52. Composition vs Aggregation

### Composition

```text
Stronger ownership relationship
```

Example:

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

### Aggregation

```text
Weaker ownership relationship
```

Example:

```python
teacher = Teacher()

department = Department(teacher)
```

Memory:

```text
Composition → contained object managed as part of the whole

Aggregation → contained object can exist independently
```

---

# 53. Inheritance

Inheritance allows a child class to reuse or extend behavior from a parent class.

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

Terminology:

```text
Animal → Parent/Base/Superclass
Dog    → Child/Derived/Subclass
```

---

# 54. Single Inheritance

One child inherits from one parent.

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

# 55. Multilevel Inheritance

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

# 56. Multiple Inheritance

A class inherits from multiple base classes.

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
child = Child()

child.skills()
child.talent()
```

---

# 57. Hierarchical Inheritance

One parent has multiple child classes.

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

# 58. Hybrid Inheritance

Hybrid inheritance is a combination of multiple inheritance patterns.

For example:

```text
Single + Multiple + Multilevel
```

Python's MRO is important when multiple inheritance creates a complex hierarchy.

---

# 59. Method Resolution Order (MRO)

MRO determines the order in which Python searches classes for methods and attributes.

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
C
↓
B
↓
A
↓
object
```

For multiple inheritance, Python uses the **C3 linearization algorithm** to construct the MRO.

---

# 60. `object` Class

Python's normal class hierarchy ultimately includes `object`.

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

You can inspect:

```python
print(Student.__mro__)
```

---

# 61. `isinstance()`

`isinstance()` checks whether an object is an instance of a class or compatible subclass.

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

Output:

```text
True
True
```

---

# 62. `issubclass()`

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

# 63. `__call__()`

`__call__()` allows an object to be called using function-call syntax.

```python
class Test:

    def __call__(self):
        print("Object called")


t = Test()

t()
```

Output:

```text
Object called
```

Conceptually:

```python
t()
```

invokes the object's callable protocol, which for a normal Python class is provided through:

```python
t.__call__()
```

---

# 64. `__call__()` with Parameters

```python
class Add:

    def __call__(self, a, b):
        return a + b


calc = Add()

print(calc(5, 3))
```

Output:

```text
8
```

Conceptually:

```python
calc(5, 3)
```

uses:

```python
calc.__call__(5, 3)
```

---

# 65. Callable Object

An object that can be called like a function is called a **callable object**.

```python
class Test:

    def __call__(self):
        print("Called")


t = Test()

print(callable(t))
```

Output:

```text
True
```

---

# 66. `callable()`

`callable()` checks whether an object appears callable.

```python
def add(a, b):
    return a + b


class Test:

    def __call__(self):
        pass


t = Test()

print(callable(add))
print(callable(t))
```

Output:

```text
True
True
```

Without `__call__()`:

```python
class Test:
    pass


t = Test()

print(callable(t))
```

Output:

```text
False
```

Calling:

```python
t()
```

would raise:

```text
TypeError
```

---

# 67. Stateful Callable Object

A callable object can maintain state between calls.

```python
class Counter:

    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count


counter = Counter()

print(counter())
print(counter())
print(counter())
```

Output:

```text
1
2
3
```

The object remembers:

```text
count = 1
count = 2
count = 3
```

---

# 68. Multiple Stateful Callable Objects

```python
class Counter:

    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count


c1 = Counter()
c2 = Counter()

print(c1())
print(c1())

print(c2())
print(c2())
```

Output:

```text
1
2
1
2
```

Because:

```text
c1 → Separate state
c2 → Separate state
```

---

# 69. `__init__()` vs `__call__()`

```text
Class()
   ↓
Instance creation
   ↓
__init__()
   ↓
Initialize instance
```

Whereas:

```text
obj()
   ↓
Callable object
   ↓
__call__()
```

Example:

```python
class Test:

    def __init__(self):
        print("Initialized")

    def __call__(self):
        print("Called")


obj = Test()

obj()
```

Output:

```text
Initialized
Called
```

---

# 70. Class-Based Decorator

`__call__()` is commonly used to implement decorators as classes.

```python
class MyDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before function")

        self.func()

        print("After function")
```

Usage:

```python
@MyDecorator
def hello():
    print("Hello")


hello()
```

Output:

```text
Before function
Hello
After function
```

Conceptually:

```python
@MyDecorator
def hello():
    print("Hello")
```

is approximately:

```python
def hello():
    print("Hello")


hello = MyDecorator(hello)
```

Now `hello` refers to a callable decorator object.

---

# 71. `__call__()` + Polymorphism

```python
class Add:

    def __call__(self, a, b):
        return a + b


class Multiply:

    def __call__(self, a, b):
        return a * b


operations = [
    Add(),
    Multiply()
]

for operation in operations:
    print(operation(5, 3))
```

Output:

```text
8
15
```

Both objects support the same interface:

```python
operation(a, b)
```

but have different implementations.

---

# 72. `__call__()` + Duck Typing

```python
class Add:

    def __call__(self, a, b):
        return a + b


class Multiply:

    def __call__(self, a, b):
        return a * b


def calculate(operation, a, b):
    return operation(a, b)
```

Usage:

```python
print(calculate(Add(), 5, 3))
print(calculate(Multiply(), 5, 3))
```

Output:

```text
8
15
```

`calculate()` does not need to know the exact class.

It only requires:

```text
operation(a, b)
```

to work.

---

# 73. Class Working Flow

Consider:

```python
class Work:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
```

Then:

```python
work = Work("John", 30)
```

Conceptually:

```text
Work
 ↓
Class Object
 ↓
Work("John", 30)
 ↓
New Work Instance
 ↓
__init__()
 ↓
self.name = "John"
self.age = 30
 ↓
work references the instance
```

Object state:

```text
+----------------------+
| Work Object          |
|----------------------|
| name = "John"        |
| age  = 30            |
+----------------------+
          ↑
          |
        work
```

---

# 74. Method Call Flow

When:

```python
work.show_info()
```

is called, Python binds the instance to the method.

Conceptually:

```python
Work.show_info(work)
```

Therefore:

```text
work
 ↓
self
 ↓
self.name
 ↓
work.name
 ↓
"John"
```

---

# 75. Multiple Objects

```python
work1 = Work("John", 30)
work2 = Work("Alice", 25)
```

Conceptually:

```text
work1 ──→ Work Object
          name = John
          age = 30


work2 ──→ Work Object
          name = Alice
          age = 25
```

They are separate instances.

---

# 76. `id()`

`id()` returns an object's identity value during its lifetime.

```python
work1 = Work("John", 30)
work2 = Work("Alice", 25)

print(id(work1))
print(id(work2))
```

Important:

Do not define `id()` simply as "memory address".

A more accurate definition is:

```text
id(object)
→ identity value of the object
```

In CPython, the identity is commonly related to the object's memory address, but this is an implementation detail rather than the language-level definition.

---

# 77. `del`

`del` can remove a name/reference or an attribute.

Example:

```python
work = Work("John", 30)

del work
```

This removes the name `work` from the namespace.

It does **not** necessarily mean that the object is immediately destroyed.

Example:

```python
work = Work("John", 30)

another = work

del work
```

Now:

```text
another
   ↓
Work Object
```

The object still has a reference.

---

# 78. Deleting an Attribute

```python
class Student:

    def __init__(self):
        self.name = "Faruk"


student = Student()

del student.name
```

After this:

```python
print(student.name)
```

raises:

```text
AttributeError
```

---

# 79. Python Memory Model

Python's memory model should not be explained as exactly:

```text
Variable → Stack
Object   → Heap
```

like a simplified C/C++ model.

A safer explanation is:

```text
Variable
   ↓
Reference
   ↓
Python Object
   ↓
Implementation-managed memory
```

In CPython, Python objects are generally allocated in heap-managed memory.

Function calls use execution frames.

The exact memory implementation can vary between Python implementations.

---

# 80. Reference Counting

CPython uses reference counting as an important part of memory management.

Example:

```python
work = Work("John", 30)

another = work

del work
```

The object still exists because:

```text
another
   ↓
Object
```

If the object has no remaining references, its reference count may reach zero and CPython can deallocate it promptly.

---

# 81. Garbage Collection

Python also provides garbage collection mechanisms, particularly for detecting and reclaiming cyclic garbage.

Example concept:

```text
Object A → Object B
   ↑         |
   |_________|
```

A cycle can keep reference counts non-zero.

Python's cyclic garbage collector can help handle such cycles.

Therefore, avoid saying:

```text
"No reference = garbage collector immediately deletes object"
```

A better statement is:

```text
An unreachable object may become eligible for memory reclamation.
The exact timing depends on the Python implementation and runtime.
```

---

# 82. `gc.collect()`

Python provides the `gc` module.

```python
import gc

gc.collect()
```

This requests a garbage-collection cycle.

It should not be interpreted as:

```text
"Delete every unused object immediately."
```

It is a request to perform garbage collection according to the runtime's rules.

---

# 83. Inheritance vs Composition

### Inheritance

Represents an **IS-A** relationship.

```text
Dog IS-A Animal
```

```python
class Dog(Animal):
    pass
```

### Composition

Represents a **HAS-A** relationship.

```text
Car HAS-A Engine
```

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

Memory:

```text
Inheritance → IS-A

Composition → HAS-A
```

---

# 84. Encapsulation vs Abstraction

| Encapsulation                                | Abstraction                              |
| -------------------------------------------- | ---------------------------------------- |
| Bundles data and behavior                    | Exposes essential interface              |
| Helps control access to state                | Hides unnecessary implementation details |
| Can use properties/name mangling/conventions | Can use ABCs and abstract methods        |
| Focuses on managing internal state           | Focuses on what interface is exposed     |

Easy memory:

```text
Encapsulation
→ How is data/state organized and accessed?

Abstraction
→ What interface should users work with?
```

---

# 85. Overloading vs Overriding

| Overloading                                                          | Overriding                                   |
| -------------------------------------------------------------------- | -------------------------------------------- |
| Same method name for different parameter patterns                    | Child provides a new implementation          |
| Traditional signature-based form is not directly supported in Python | Supported                                    |
| Inheritance not required                                             | Inheritance involved                         |
| Python uses alternatives such as defaults/`*args`                    | Child replaces/influences inherited behavior |

Memory:

```text
Overloading
→ Same Name + Flexible Inputs

Overriding
→ Parent → Child + New Implementation
```

---

# 86. Polymorphism vs Duck Typing

They are related but not identical terms.

### Polymorphism

General idea:

```text
One interface
+
Different implementations
```

### Duck Typing

A Python style of achieving flexible behavior by relying on capabilities/behavior instead of explicit concrete-type checks.

Example:

```python
def make_sound(obj):
    obj.speak()
```

The function does not need:

```python
isinstance(obj, Dog)
```

or:

```python
isinstance(obj, Cat)
```

---

# 87. Complete OOP Example

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

Concepts demonstrated:

```text
Abstract Class
Inheritance
super()
Instance Attributes
Class Attributes
Property
Instance Method
Class Method
Static Method
Polymorphism
Encapsulation
```

---

# 88. Important OOP Concepts

```text
Class
Object

__init__()
self

Instance Attribute
Class Attribute

Instance Method
Class Method
Static Method

Method Binding
Bound Method

Encapsulation
Inheritance
Polymorphism
Abstraction

Method Overriding
super()
MRO

Method Overloading limitations
*args
**kwargs

Magic/Dunder Methods
__str__()
__repr__()
__eq__()
__add__()
__call__()

@property
Setter

Composition
Aggregation
Association

isinstance()
issubclass()

callable()
```

---

# 89. Quick Revision

```text
Class
    ↓
Blueprint / Template

Object
    ↓
Instance of a Class

self
    ↓
Current Instance

cls
    ↓
Current Class

__init__()
    ↓
Initialize Instance

Instance Attribute
    ↓
Object-specific State

Class Attribute
    ↓
Class-level Attribute

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
Bundle + Manage Access

Inheritance
    ↓
IS-A

Composition
    ↓
HAS-A

Polymorphism
    ↓
Same Interface + Different Behavior

Duck Typing
    ↓
Behavior/Capability over Explicit Type Checking

Abstraction
    ↓
Essential Interface

super()
    ↓
Next implementation according to MRO

MRO
    ↓
Method/Attribute Lookup Order

__call__()
    ↓
Object can be called like a function
```

---

# 90. OOP Learning Roadmap

```text
1. Class
   ↓
2. Object
   ↓
3. __init__()
   ↓
4. self
   ↓
5. Instance Attribute
   ↓
6. Class Attribute
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
15. Duck Typing
    ↓
16. Abstraction
    ↓
17. Magic Methods
    ↓
18. @property / Setter
    ↓
19. Composition
    ↓
20. Aggregation / Association
    ↓
21. MRO
    ↓
22. __call__ / Callable Objects
    ↓
23. OOP Design
    ↓
24. Projects + Practice
```

---

# 91. Interview Questions

## Basic

1. What is OOP?
2. What is a class?
3. What is an object?
4. Difference between class and object?
5. What is `self`?
6. What is `__init__()`?
7. What is an instance attribute?
8. What is a class attribute?
9. What is an instance method?
10. What is a class method?
11. What is a static method?
12. Difference between `self` and `cls`?

## Core OOP

13. What are the four pillars of OOP?
14. What is encapsulation?
15. What is inheritance?
16. What are the types of inheritance?
17. What is polymorphism?
18. What is abstraction?
19. What is an abstract class?
20. What is method overriding?
21. What is `super()`?
22. What is MRO?

## Python-Specific

23. Does Python support traditional method overloading?
24. What are `*args` and `**kwargs`?
25. What is duck typing?
26. What is dynamic typing?
27. What is method binding?
28. What is a bound method?
29. What is name mangling?
30. Is `__name` truly private?
31. What is `@property`?
32. What is a setter?
33. What are dunder methods?
34. What is `__str__()`?
35. What is `__repr__()`?
36. What is `__eq__()`?
37. What is operator overloading?
38. What is `__call__()`?
39. What is a callable object?
40. What does `callable()` do?

## Object Relationships

41. What is composition?
42. What is aggregation?
43. What is association?
44. Difference between composition and inheritance?
45. What is an IS-A relationship?
46. What is a HAS-A relationship?

## Runtime / Memory

47. What does `id()` return?
48. What happens when `del obj` is used?
49. What is reference counting?
50. What is garbage collection?
51. Why should Python's Stack/Heap model not be explained exactly like C/C++?

---

# 92. Most Important Differences

### `self` vs `cls`

```text
self
 ↓
Current Instance

cls
 ↓
Current Class
```

### Instance vs Class Attribute

```text
Instance Attribute
→ Belongs to individual object

Class Attribute
→ Defined on class
```

### Instance vs Class vs Static Method

```text
Instance
→ self
→ Instance behavior

Class
→ cls
→ Class behavior

Static
→ No automatic self/cls
→ Utility behavior
```

### Inheritance vs Composition

```text
Inheritance
→ IS-A

Composition
→ HAS-A
```

### Overriding vs Overloading

```text
Overriding
→ Child redefines inherited method

Traditional Overloading
→ Same name + different signatures
→ Not directly supported in Python
```

### Polymorphism vs Duck Typing

```text
Polymorphism
→ Same interface, different behavior

Duck Typing
→ Required behavior matters more than concrete type
```

### `__init__` vs `__call__`

```text
Class()
→ __init__()
→ Initialize instance

obj()
→ __call__()
→ Call object
```

---

# 93. Final Concept Map

```text
                    PYTHON OOP
                        │
        ┌───────────────┼────────────────┐
        │               │                │
      Class           Object           Methods
        │               │                │
        │               │       ┌────────┼─────────┐
        │               │       │        │         │
        │               │   Instance   Class    Static
        │               │      │         │         │
        │               │     self      cls       -
        │               │
        └───────────────┼──────────────────────────
                        │
                Four Pillars
                        │
          ┌─────────────┼─────────────┐
          │             │             │
    Encapsulation   Inheritance   Polymorphism
          │             │             │
          │             │        ┌────┴─────┐
          │             │        │          │
          │             │    Overriding  Duck Typing
          │             │
          │          MRO / super()
          │
       Properties
       Name Mangling
                        │
                   Abstraction
                        │
                      ABC
                @abstractmethod
                        │
                        │
                Object Relationships
                        │
          ┌─────────────┼──────────────┐
          │             │              │
      Composition   Aggregation    Association
          │
        HAS-A
          │
      Inheritance
        IS-A
```

---

# 94. Final 20 Lines to Memorize

```text
1. Class → Blueprint / Template

2. Object → Instance of a Class

3. self → Current Instance

4. cls → Current Class

5. __init__() → Initialize an Instance

6. Instance Attribute → Object-specific state

7. Class Attribute → Class-level attribute

8. Instance Method → self

9. Class Method → @classmethod + cls

10. Static Method → @staticmethod

11. Encapsulation → Bundle + Manage Access

12. Inheritance → IS-A

13. Composition → HAS-A

14. Polymorphism → Same Interface + Different Behavior

15. Duck Typing → Behavior/Capability matters

16. Abstraction → Essential Interface

17. Overriding → Child provides new implementation

18. MRO → Method Resolution Order

19. __call__() → Makes an object callable

20. callable(obj) → Checks whether obj is callable
```

---

# 95. One-Line Definitions

```text
Class
→ A blueprint/template for creating objects.

Object
→ An instance of a class.

self
→ Conventional reference to the current instance.

cls
→ Conventional reference to the current class.

__init__()
→ Initializes a newly created instance.

Encapsulation
→ Bundling state and behavior while managing access to state.

Inheritance
→ Mechanism for creating a class based on another class.

Polymorphism
→ Same interface/operation with different object-specific behavior.

Abstraction
→ Exposing essential behavior while hiding unnecessary implementation details.

Duck Typing
→ Relying on an object's supported behavior rather than its concrete type.

Method Overriding
→ Child class provides its own implementation of an inherited method.

Composition
→ HAS-A relationship using contained objects.

Aggregation
→ A looser HAS-A relationship where contained objects can exist independently.

Association
→ General relationship between independent objects.

MRO
→ The order Python uses to search classes for methods/attributes.

__call__()
→ Special method that allows an object to be called using ().

@property
→ Allows method-based logic to be accessed with attribute syntax.

@classmethod
→ Creates a method that receives the class as its first argument.

@staticmethod
→ Creates a method with no automatically supplied instance/class argument.
```

---

# Final Memory Formula

```text
OOP
│
├── Class → Blueprint
├── Object → Instance
│
├── Methods
│   ├── Instance → self
│   ├── Class → cls
│   └── Static → No automatic self/cls
│
├── Four Pillars
│   ├── Encapsulation
│   ├── Inheritance
│   ├── Polymorphism
│   └── Abstraction
│
├── Relationships
│   ├── Inheritance → IS-A
│   ├── Composition → HAS-A
│   ├── Aggregation
│   └── Association
│
├── Polymorphism
│   ├── Overriding
│   └── Duck Typing
│
├── Special Methods
│   ├── __init__
│   ├── __str__
│   ├── __repr__
│   ├── __eq__
│   ├── __add__
│   └── __call__
│
└── Python Features
    ├── @property
    ├── Setter
    ├── MRO
    ├── isinstance()
    ├── issubclass()
    └── callable()
```

**সবচেয়ে গুরুত্বপূর্ণ flow:**

```text
Class
  ↓
Object
  ↓
self
  ↓
Instance Attributes
  ↓
Instance Methods
  ↓
Inheritance
  ↓
Overriding
  ↓
Polymorphism
  ↓
Abstraction
  ↓
OOP Design
```

"""