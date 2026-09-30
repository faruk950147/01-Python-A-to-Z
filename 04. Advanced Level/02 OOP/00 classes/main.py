"""
# Python OOP — Complete Structured Notes

## Table of Contents

    1. OOP Introduction
    2. Class
    3. Object
    4. Class vs Object
    5. Object Creation
    6. `__new__()` and `__init__()`
    7. `self`
    8. Attributes

    * Instance Attribute
    * Class Attribute
    9. Methods

    * Instance Method
    * Class Method
    * Static Method
    10. Method Binding
    11. Alternative Constructor
    12. Encapsulation
    13. Public, `_name`, `__name`
    14. Name Mangling
    15. Inheritance
    16. Types of Inheritance
    17. Method Overriding
    18. `super()`
    19. MRO
    20. Polymorphism
    21. Duck Typing
    22. Dynamic Typing vs Duck Typing
    23. Abstraction
    24. Abstract Base Class
    25. Method Overloading
    26. `*args` and `**kwargs`
    27. Magic / Dunder Methods
    28. `__str__()` and `__repr__()`
    29. Operator Overloading
    30. `__eq__()`
    31. `@property`
    32. Property Setter
    33. Composition
    34. Aggregation
    35. Association
    36. Inheritance vs Composition
    37. Nested Class
    38. `__call__()`
    39. Callable Objects
    40. Stateful Callable Objects
    41. Class-Based Decorator
    42. `isinstance()`
    43. `issubclass()`
    44. `id()`
    45. `del`
    46. Python Memory Model
    47. Reference Counting
    48. Garbage Collection
    49. `__name__ == "__main__"`
    50. Complete OOP Example
    51. OOP Concept Comparison
    52. Quick Revision
    53. Learning Roadmap
    54. Interview Questions
    55. Final Memory Formula

# 1. What is OOP?

    **OOP = Object-Oriented Programming**

    OOP is a programming paradigm where programs are designed around **classes and objects**.

    Real-world examples:

    ```text
    Student
    Employee
    Car
    Bank Account
    Book
    Mobile
    Product
    University
    Department
    ```

    The commonly taught four pillars of OOP are:

    ```text
    1. Encapsulation
    2. Inheritance
    3. Polymorphism
    4. Abstraction
    ```

    Other important Python OOP concepts:

    ```text
    Class
    Object
    self
    Class/Instance Attributes
    Instance/Class/Static Methods
    Method Binding
    Method Overriding
    super()
    MRO
    Duck Typing
    Dunder Methods
    @property
    Composition
    Aggregation
    Association
    Nested Class
    Callable Objects
    ```

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

    A class can define:

    ```text
    Attributes
    Methods
    Properties
    Class-level behavior
    ```

    ### Important

    In Python, a class is itself an object.

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

    `type` is the metaclass of normal Python classes.

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
    s1      → Object / Instance
    s2      → Object / Instance
    ```

    Multiple objects can be created from the same class.

    Each instance can have its own state.

# 4. Class vs Object

    | Class                          | Object                         |
    | ------------------------------ | ------------------------------ |
    | Blueprint / template           | Instance                       |
    | Defines structure and behavior | Represents a concrete instance |
    | Used to create objects         | Created from a class           |
    | `Student`                      | `s1`, `s2`                     |

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
    ↓
    s1 references the instance
    ```

    The variable `s1` is a **name/reference** associated with the object.

# 6. `__new__()` and `__init__()`

    These are two different special methods involved in object creation.

    ```text
    __new__()
    ↓
    Creates/returns an instance

    __init__()
    ↓
    Initializes the instance
    ```

    Example:

    ```python
    class Student:

        def __new__(cls, name):
            print("__new__() called")
            instance = super().__new__(cls)
            return instance

        def __init__(self, name):
            print("__init__() called")
            self.name = name


    student = Student("Faruk")
    ```

    Output:

    ```text
    __new__() called
    __init__() called
    ```

    ### Important

    Beginner materials often call `__init__()` the constructor.

    More technically:

    ```text
    __new__()
    → Responsible for creating/returning the instance

    __init__()
    → Initializes the instance
    ```

    For normal Python development, you usually only need to define `__init__()`.

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

    is executed:

    ```text
    self → s1
    ```

    Therefore:

    ```python
    self.name
    ```

    means:

    ```text
    name attribute of the current instance
    ```

# 9. `self` is a Convention

    Python does not require the first parameter of an instance method to be named `self`.

    For example:

    ```python
    class Student:

        def show(current):
            print("Hello")
    ```

    This works:

    ```python
    student = Student()
    student.show()
    ```

    However, the standard Python convention is:

    ```python
    def show(self):
    ```

    Always prefer `self`.

# 10. Instance Attribute

    An **instance attribute** belongs to a particular object.

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

    Conceptually:

    ```text
    s1 → name = "Faruk"

    s2 → name = "Rahim"
    ```

# 11. Class Attribute

        An attribute defined directly inside the class body is a **class attribute**.

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

        Access:

        ```python
        print(Student.school)
        ```

        An instance can also access it:

        ```python
        s1 = Student("Faruk")

        print(s1.school)
        ```

        When accessing `s1.school`, Python checks the instance and then the class according to its attribute lookup rules.

# 12. Instance Attribute vs Class Attribute

    ### Instance Attribute

    ```python
    self.name
    ```

    * Associated with an individual instance
    * Different instances can have different values
    * Represents object-specific state

    ### Class Attribute

    ```python
    Student.school
    ```

    * Defined on the class
    * Accessible through instances unless shadowed
    * Useful for class-level data

    Example:

    ```python
    class Student:

        school = "TMSS"

        def __init__(self, name):
            self.name = name


    s1 = Student("Faruk")
    s2 = Student("Rahim")

    print(s1.name)
    print(s2.name)

    print(s1.school)
    print(s2.school)
    ```

    Output:

    ```text
    Faruk
    Rahim
    TMSS
    TMSS
    ```

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

    works through the bound-method mechanism and is equivalent in effect to:

    ```python
    Student.show(s1)
    ```

# 14. Class Method
    A class method is a method that works directly with the class, not with specific objects (instance). 
    It uses cls to refer to the class and is created using the @classmethod decorator.
    It receives the class automatically through the `cls` parameter.

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

# 16. Three Main Method Types

    | Method          | Automatic First Argument | Main Purpose            |
    | --------------- | ------------------------ | ----------------------- |
    | Instance Method | `self`                   | Instance behavior       |
    | Class Method    | `cls`                    | Class-level behavior    |
    | Static Method   | None                     | Utility/helper behavior |

    Memory:

    ```text
    Instance Method
        ↓
    self
        ↓
    Object

    Class Method
        ↓
    cls
        ↓
    Class

    Static Method
        ↓
    No automatic self/cls
        ↓
    Utility
    ```

# 17. All Three Methods in One Class

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

# 18. Alternative Constructor

    One important use of `@classmethod` is creating an alternative constructor.

    ```python
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @classmethod
        def from_string(cls, data):
            name, age = data.split("-")
            return cls(name, int(age))
    ```

    Usage:

    ```python

    student = Student.from_string("Faruk-25")

    print(student.name)
    print(student.age)
    ```

    Output:

    ```text
    Faruk
    25
    ```

    ### Why `cls(...)`?

    Because `cls` refers to the class on which the class method was called.

    This also works naturally with subclasses.

# 19. Method Binding

    When an instance method is accessed through an instance, Python produces a **bound method**.

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

    The instance is automatically supplied as `self`.

# 20. `Student.show` vs `s.show`

    ### Through class

    ```python
    Student.show
    ```

    This retrieves the function through the class.

    ### Through instance

    ```python
    s.show
    ```

    This produces a bound method with `s` automatically supplied as the first argument.

    In Python 3, `Student.show` is not normally called an "unbound method"; it is simply a function retrieved from the class.

# 21. Encapsulation

    Encapsulation means keeping related state and behavior together while controlling or managing how internal state is accessed and modified.

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

# 22. Public, `_name`, and `__name`

    Python does not provide Java/C++-style strict access modifiers for ordinary attributes.

    ## Public

    ```python
    self.name
    ```

    Normal public attribute.

    ## Single Underscore

    ```python
    self._name
    ```

    Conventionally means:

    ```text
    Internal / non-public API
    ```

    It is not enforced by Python.

    ## Double Underscore

    ```python
    self.__name
    ```

    Triggers name mangling.

# 23. Name Mangling

    Name mangling is a Python mechanism that changes the internal name of an attribute or method beginning with `__` inside a class.

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

    You can demonstrate it:

    ```python
    student = Student()

    print(student._Student__name)
    ```

    Output:

    ```text
    Faruk
    ```

    ### Why does Python use name mangling?

    Mainly to reduce accidental name collisions, especially when inheritance is involved.

    Important:

    ```text
    __name
    ```

    is **not truly private** in the strict sense.

    Memory:

    ```text
    name
    ↓
    Public

    _name
    ↓
    Internal-use convention

    __name
    ↓
    Name Mangling
    ```
# 24. Inheritance

    Inheritance allows a subclass to reuse or extend behavior from a base class.

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
    Animal → Parent / Base / Superclass
    Dog    → Child / Derived / Subclass
    ```

    Inheritance commonly represents:

    ```text
    IS-A relationship
    ```

    Example:

    ```text
    Dog IS-A Animal
    ```

# 25. Types of Inheritance

    ## 25.1 Single Inheritance

        One child inherits from one parent.

        ```python
        class Animal:
            pass


        class Dog(Animal):
            pass
        ```

        ```text
        Animal
        ↓
        Dog
        ```

    ## 25.2 Multilevel Inheritance

        Inheritance across multiple levels.

        ```python
        class Animal:
            pass


        class Dog(Animal):
            pass


        class Puppy(Dog):
            pass
        ```

        ```text
        Animal
        ↓
        Dog
        ↓
        Puppy
        ```

    ## 25.3 Multiple Inheritance

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

        Output:

        ```text
        Programming
        Cooking
        ```

    ## 25.4 Hierarchical Inheritance

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

    ## 25.5 Hybrid Inheritance

        Hybrid inheritance is a combination of multiple inheritance patterns.

        For example:

        ```text
        Single
        +
        Multiple
        +
        Multilevel
        ```

        Complex multiple-inheritance hierarchies require understanding MRO.

# 26. Method Overriding

    Method overriding occurs when a subclass provides its own implementation of an inherited method.

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

    Here:

    ```text
    Animal.sound()
        ↓
    Inherited method

    Dog.sound()
        ↓
    New implementation
    ```

# 27. `super()`

    `super()` provides access to the next implementation in the **MRO (Method Resolution Order)**.

    Example:

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

    Simple hierarchy:

    ```text
    Dog
    ↓
    Animal
    ↓
    object
    ```

    `super()` follows the MRO.

    ### Important

    Do not think:

    ```python
    super()
    ```

    always simply means:

    ```text
    parent
    ```

    More accurately:

    ```text
    super()
    → next class according to the MRO
    ```

    This matters especially in multiple inheritance.

# 28. Method Resolution Order (MRO)

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

    For multiple inheritance, Python uses **C3 linearization** to construct the MRO.

    You can inspect it using:

    ```python
    print(C.__mro__)
    ```

    or:

    ```python
    print(C.mro())
    ```

# 29. `object` Class

    Python's ordinary classes ultimately inherit from `object`.

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

    Typical output:

    ```text
    (<class '__main__.Student'>, <class 'object'>)
    ```

# 30. Polymorphism

    **Polymorphism** means the same interface or operation can produce different behavior depending on the object.

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

# 31. Duck Typing

    Duck typing is a Python style where code focuses on whether an object supports the required behavior rather than checking its exact concrete class.

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

    The function only requires:

    ```python
    thing.quack()
    ```

    It does not require the object to be an instance of `Duck`.

# 32. Duck Typing and `AttributeError`

    If the required operation does not exist:

    ```python
    class Car:
        pass


    def make_it_quack(thing):
        thing.quack()


    car = Car()

    make_it_quack(car)
    ```

    Python raises:

    ```text
    AttributeError
    ```

    because `Car` does not provide `quack()`.

# 33. Dynamic Typing vs Duck Typing

    These are different concepts.

    ### Dynamic Typing

    Python determines object types at runtime.

    ```python
    x = 10

    x = "Hello"

    x = [1, 2, 3]
    ```

    ### Duck Typing

    Code focuses on required behavior rather than requiring a specific concrete type.

    ```python
    def process(obj):
        obj.run()
    ```

    The function assumes that `obj` supports:

    ```python
    run()
    ```

    Memory:

    ```text
    Dynamic Typing
    → Type information is handled at runtime

    Duck Typing
    → Required behavior/capability matters
    ```

# 34. Abstraction

    **Abstraction** means exposing essential behavior/interface while hiding unnecessary implementation details.

    Python provides tools such as:

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

    The class specifies that concrete subclasses should provide `speak()`.

# 35. Abstract Class

    An abstract base class can define methods that subclasses are required to implement.

    ```python
    from abc import ABC, abstractmethod


    class Shape(ABC):

        @abstractmethod
        def area(self):
            pass
    ```

    Concrete implementation:

    ```python
    class Circle(Shape):

        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.1416 * self.radius ** 2
    ```

    Usage:

    ```python
    circle = Circle(5)

    print(circle.area())
    ```

    A subclass that does not implement all required abstract methods remains abstract and cannot normally be instantiated.

# 36. Polymorphism + Abstract Base Class

    ```python
    from abc import ABC, abstractmethod


    class Animal(ABC):

        @abstractmethod
        def speak(self):
            pass


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

    Usage:

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

    The abstract base class defines a common interface.

# 37. Adding a New Class

    ```python
    class Cow(Animal):

        def speak(self):
            return "Moo!"
    ```

    Now:

    ```python
    animals.append(Cow())
    ```

    The same loop works:

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

    The loop does not need to know the concrete class.

# 38. Method Overloading

    Traditional method overloading means:

    ```text
    Same method name
    +
    Different parameter signatures
    ```

    Languages such as Java and C++ support traditional signature-based method overloading.

    Python does **not** support traditional method overloading based only on different parameter lists.

    Example:

    ```python
    class Calculator:

        def add(self, a):
            return a

        def add(self, a, b):
            return a + b
    ```

    The second `add()` definition replaces the first one in the class namespace.

    Therefore:

    ```python
    calc = Calculator()

    calc.add(5)
    ```

    raises:

    ```text
    TypeError
    ```

# 39. Alternatives to Traditional Overloading

    Python commonly uses:

    ```text
    Default arguments
    *args
    **kwargs
    Conditional logic
    functools.singledispatch
    ```

    Example:

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

    This is flexible argument handling, not traditional signature-based overloading.

    # 40. `*args`

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

# 41. `**kwargs`

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

# 42. `*args` vs `**kwargs`

    ```text
    *args
    ↓
    Extra positional arguments
    ↓
    Tuple


    **kwargs
    ↓
    Extra keyword arguments
    ↓
    Dictionary
    ```

# 43. Magic / Dunder Methods

    Special methods are commonly called **dunder methods** because their names begin and end with double underscores.

    Examples:

    ```python
    __new__
    __init__
    __str__
    __repr__
    __len__
    __eq__
    __add__
    __call__
    ```

    They allow user-defined classes to interact with Python syntax and built-in operations.

# 44. `__str__()`

    `__str__()` provides a user-friendly string representation of an object.

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

    `print(obj)` generally uses:

    ```python
    str(obj)
    ```

    which can invoke:

    ```python
    obj.__str__()
    ```

# 45. `__repr__()`

    `__repr__()` is generally intended to provide a useful developer-oriented representation.

    ```python
    class Student:

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f"Student(name={self.name!r})"


    student = Student("Faruk")

    print(repr(student))
    ```

    Output:

    ```text
    Student(name='Faruk')
    ```

    A useful `repr` helps with debugging and inspecting objects.

# 46. `__str__()` vs `__repr__()`

    ```text
    __str__()
    ↓
    User-friendly representation

    __repr__()
    ↓
    Developer/debugging representation
    ```

# 47. Operator Overloading

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

    The expression:

    ```python
    n1 + n2
    ```

    uses Python's addition protocol, which can invoke:

    ```python
    __add__()
    ```

# 48. `__eq__()`

    `__eq__()` can define equality behavior.

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

    Without a custom equality implementation, ordinary user-defined objects generally compare by identity.

# 49. `@property`

    `@property` allows method-based logic to be accessed using attribute syntax.

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

    Instead of:

    ```python
    student.name()
    ```

    we use:

    ```python
    student.name
    ```

    # 50. Property Setter

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

# 51. Composition

    Composition represents a strong **HAS-A** relationship where an object contains another object as part of its implementation.

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

    The `Car` object contains an `Engine` object.

# 52. Aggregation

    Aggregation is commonly described as a looser **HAS-A** relationship where the contained object can exist independently.

    ```python
    class Teacher:
        pass


    class Department:

        def __init__(self, teacher):
            self.teacher = teacher
    ```

    The `Teacher` is created outside:

    ```python
    teacher = Teacher()

    department = Department(teacher)
    ```

    The teacher can continue to exist independently of the department.

    ### Important

    Composition and aggregation are conceptual design relationships. Python does not enforce special syntax for them.

# 53. Association

    Association is a general relationship where objects interact or are connected without necessarily implying ownership.

    Examples:

    ```text
    Teacher ↔ Student
    Doctor ↔ Patient
    Customer ↔ Bank
    ```

    Association is broader than composition and aggregation.

# 54. Composition vs Aggregation

    ### Composition

    ```text
    Stronger whole-part relationship
    ```

    Example:

    ```python
    class Car:

        def __init__(self):
            self.engine = Engine()
    ```

    Conceptually:

    ```text
    Car
    ↓
    contains
    ↓
    Engine
    ```

    ### Aggregation

    ```text
    Looser whole-part relationship
    ```

    Example:

    ```python
    teacher = Teacher()

    department = Department(teacher)
    ```

    The `Teacher` can exist independently.

    Memory:

    ```text
    Composition
    → Stronger whole-part relationship

    Aggregation
    → Weaker whole-part relationship
    ```

# 55. Inheritance vs Composition

    ### Inheritance

    Represents:

    ```text
    IS-A
    ```

    Example:

    ```text
    Dog IS-A Animal
    ```

    ```python
    class Dog(Animal):
        pass
    ```

    ### Composition

    Represents:

    ```text
    HAS-A
    ```

    Example:

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

# 56. Nested Class

    A **nested class** is a class defined inside another class.

    Example:

    ```python
    class University:

        def __init__(self, name):
            self.name = name

        def display(self):
            print(self.name)

        class Department:

            def __init__(self, name):
                self.name = name

            def display(self):
                print(self.name)
    ```

    Usage:

    ```python
    if __name__ == "__main__":

        university = University("TMSS Technical University")

        university.display()

        department1 = University.Department("CSE")
        department2 = University.Department("EEE")

        department1.display()
        department2.display()
    ```

    Output:

    ```text
    TMSS Technical University
    CSE
    EEE
    ```

    ### Important Concept

    `Department` is an attribute of the `University` class.

    Therefore:

    ```python
    University.Department
    ```

    refers to the nested class.

    You can also access it through an instance:

    ```python
    university.Department
    ```

    because attribute lookup can find `Department` on the class.

# 57. Nested Class with Instance Attribute

    You can create a nested-class object and store it as an instance attribute.

    ```python
    class University:

        def __init__(self, name):
            self.name = name
            self.department = self.Department("Department")

        def display(self):
            print(self.name)

        class Department:

            def __init__(self, name):
                self.name = name

            def display(self):
                print(self.name)


    if __name__ == "__main__":

        university = University("TMSS Technical University")

        university.display()
        university.department.display()
    ```

    Output:

    ```text
    TMSS Technical University
    Department
    ```

    Here:

    ```text
    University
        ↓
    Department class
        ↓
    Department object
        ↓
    university.department
    ```

    ### Creating Specific Departments

    ```python
    university.department1 = University.Department("CSE")
    university.department2 = University.Department("EEE")

    university.department1.display()
    university.department2.display()
    ```

    Output:

    ```text
    CSE
    EEE
    ```

    ### Important Distinction

    A nested class is **not automatically composition**.

    This:

    ```python
    class University:
        class Department:
            pass
    ```

    means:

    ```text
    Department is defined inside University
    ```

    Whereas this:

    ```python
    self.department = self.Department("CSE")
    ```

    means:

    ```text
    University instance contains a Department instance
    ```

    That object relationship can be described as a form of composition depending on the intended design.

# 58. `__call__()`

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

    uses the object's callable protocol and invokes:

    ```python
    t.__call__()
    ```

# 59. `__call__()` with Parameters

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

# 60. Callable Object

    An object that can be called using function-call syntax is called a **callable object**.

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

# 61. Stateful Callable Object

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

    The object maintains:

    ```text
    count = 1
    count = 2
    count = 3
    ```

# 62. Multiple Stateful Callable Objects

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
    c1 → Separate instance state
    c2 → Separate instance state
    ```

# 63. `__init__()` vs `__call__()`

    Object creation:

    ```text
    Class()
    ↓
    __new__()
    ↓
    __init__()
    ↓
    Initialized instance
    ```

    Calling an existing object:

    ```text
    obj()
    ↓
    Callable protocol
    ↓
    __call__()
    ```

# 64. Class-Based Decorator

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
    hello = MyDecorator(hello)
    ```

    Now:

    ```text
    hello
    ```

    refers to a callable `MyDecorator` instance.

# 65. `__call__()` + Polymorphism

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

    Both objects support:

    ```python
    operation(a, b)
    ```

    but provide different behavior.

# 66. `__call__()` + Duck Typing

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

    `calculate()` does not need to know the concrete class.

    It only requires:

    ```text
    operation(a, b)
    ```

# 67. `isinstance()`

    `isinstance()` checks whether an object is an instance of a specified class or its subclasses.

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

    Because:

    ```text
    Dog IS-A Animal
    ```

# 68. `issubclass()`

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

# 69. `id()`

    `id()` returns the identity value of an object during its lifetime.

    ```python
    class Work:

        def __init__(self, name):
            self.name = name


    work1 = Work("John")
    work2 = Work("Alice")

    print(id(work1))
    print(id(work2))
    ```

    More accurate definition:

    ```text
    id(object)
    → Identity value of the object
    ```

    Do not define it simply as:

    ```text
    memory address
    ```

    In CPython, the identity is commonly related to the object's memory address, but that is an implementation detail.

# 70. `del`

    `del` can remove a name/reference or delete an attribute.

    Example:

    ```python
    work = Work("John")

    del work
    ```

    This removes the name `work` from the current namespace.

    It does not necessarily mean that the object is immediately destroyed.

    Example:

    ```python
    work = Work("John")

    another = work

    del work
    ```

    Now:

    ```text
    another
    ↓
    Work Object
    ```

    The object still exists because another reference points to it.

# 71. Deleting an Attribute

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

# 72. Python Memory Model

    Avoid explaining Python's memory model exactly as:

    ```text
    Variable → Stack
    Object   → Heap
    ```

    as a universal language rule.

    A safer conceptual model is:

    ```text
    Name
    ↓
    Reference to an object
    ↓
    Python Object
    ↓
    Implementation-managed memory
    ```

    In CPython, Python objects are generally allocated in heap-managed memory.

    Exact implementation details can vary between Python implementations.

# 73. Reference Counting

    CPython uses **reference counting** as an important part of its memory-management system.

    Example:

    ```python
    work = Work("John")

    another = work

    del work
    ```

    After:

    ```python
    del work
    ```

    the object still has a reference:

    ```text
    another
    ↓
    Work Object
    ```

    If an object's reference count reaches zero in CPython, it can generally be deallocated promptly.

# 74. Garbage Collection

    Python also has a garbage collector that can detect and reclaim certain unreachable reference cycles.

    Example:

    ```text
    Object A → Object B
    ↑         |
    |_________|
    ```

    A reference-counting system alone may not reclaim such a cycle.

    Python's cyclic garbage collector can detect such unreachable cycles.

    Therefore, avoid saying:

    ```text
    "No reference = garbage collector immediately deletes object"
    ```

    Better:

    ```text
    An unreachable object may become eligible
    for memory reclamation.

    The exact timing depends on the Python
    implementation and runtime.
    ```

# 75. `gc.collect()`

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

# 76. `__name__ == "__main__"`

    Every Python file is a module.

    Python automatically assigns a special variable:

    ```python
    __name__
    ```

    to every module.

    Its value depends on how the module is used.

    | Usage                | `__name__`    |
    | -------------------- | ------------- |
    | Run directly         | `"__main__"`  |
    | Imported as a module | Module's name |

    Example:

    ```python
    def hello():
        print("Hello from function!")


    if __name__ == "__main__":
        print("This code runs directly!")
        hello()
    ```

    Running:

    ```bash
    python greet.py
    ```

    Output:

    ```text
    This code runs directly!
    Hello from function!
    ```

# 77. Why Use `if __name__ == "__main__"`?

    It allows code to run only when the file is executed directly.

    When imported:

    ```python
    import greet
    ```

    the block:

    ```python
    if __name__ == "__main__":
    ```

    is skipped because:

    ```python
    __name__ == "greet"
    ```

    This helps:

    ```text
    Reuse modules
    Avoid unwanted execution during import
    Separate reusable code from script execution
    Keep test/demo code inside the module
    ```

# 78. Example: Module Import

    ### `greet.py`

    ```python
    def hello():
        print("Hello from function!")


    if __name__ == "__main__":
        print("Running directly")
        hello()
    ```

    ### `main.py`

    ```python
    import greet

    greet.hello()
    ```

    Output:

    ```text
    Hello from function!
    ```

    The direct-execution block in `greet.py` does not run during import.

# 79. Real-World Example

    ### `calculator.py`

    ```python
    def add(a, b):
        return a + b


    def subtract(a, b):
        return a - b


    if __name__ == "__main__":
        print("Testing calculator functions")
        print(add(5, 3))
        print(subtract(5, 3))
    ```

    Run directly:

    ```bash
    python calculator.py
    ```

    Output:

    ```text
    Testing calculator functions
    8
    2
    ```

    Import from another file:

    ```python
    import calculator

    print(calculator.add(10, 5))
    ```

    Output:

    ```text
    15
    ```

    The test code does not automatically run during import.

# 80. Complete OOP Example

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


    if __name__ == "__main__":

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
    @property
    Instance Method
    Class Method
    Static Method
    Polymorphism
    Encapsulation
    __name__ == "__main__"
    ```

# 81. Encapsulation vs Abstraction

    | Encapsulation                               | Abstraction                              |
    | ------------------------------------------- | ---------------------------------------- |
    | Bundles state and behavior                  | Exposes essential interface              |
    | Manages access to internal state            | Hides unnecessary implementation details |
    | Uses properties, conventions, name mangling | Uses ABCs and abstract methods           |
    | Focuses on state organization/access        | Focuses on interface/design              |

    Easy memory:

    ```text
    Encapsulation
    → How is state organized and accessed?

    Abstraction
    → What interface should users work with?
    ```

# 82. Overloading vs Overriding

    | Overloading                                          | Overriding                          |
    | ---------------------------------------------------- | ----------------------------------- |
    | Same name + different parameter signatures           | Child provides a new implementation |
    | Traditional form is not directly supported in Python | Supported through inheritance       |
    | Inheritance is not required                          | Inheritance is involved             |
    | Defaults, `*args`, etc. are common alternatives      | Normal method dispatch is used      |

    Memory:

    ```text
    Overloading
    → Same Name + Different Signatures

    Overriding
    → Inherited Method + New Implementation
    ```

# 83. Polymorphism vs Duck Typing

    ### Polymorphism

    ```text
    Same interface
    +
    Different implementations
    ```

    ### Duck Typing

    ```text
    Required behavior/capability
    +
    Concrete type is less important
    ```

    Example:

    ```python
    def make_sound(obj):
        obj.speak()
    ```

    The function only requires:

    ```python
    obj.speak()
    ```

# 84. Four Fundamental OOP Concepts

    ```text
    1. Encapsulation
    ↓
    Bundle state + behavior
    and manage access

    2. Inheritance
    ↓
    Reuse/extend behavior
    through an IS-A relationship

    3. Polymorphism
    ↓
    Same interface
    different behavior

    4. Abstraction
    ↓
    Expose essential interface
    hide unnecessary details
    ```

# 85. Quick Revision

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

    __new__()
        ↓
    Creates/returns an instance

    __init__()
        ↓
    Initializes an instance

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
    Bundle + Manage State Access

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
    Behavior/Capability over Concrete Type

    Abstraction
        ↓
    Essential Interface

    Method Overriding
        ↓
    Child provides new implementation

    super()
        ↓
    Next implementation according to MRO

    MRO
        ↓
    Method Resolution Order

    @property
        ↓
    Method-based logic through attribute syntax

    __call__()
        ↓
    Allows object to be called like a function

    __name__ == "__main__"
        ↓
    Run code only when module is executed directly
    ```

# 86. Python OOP Learning Roadmap

    ```text
    1. Class
    ↓
    2. Object
    ↓
    3. __new__() and __init__()
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
    10. Method Binding
        ↓
    11. Encapsulation
        ↓
    12. Inheritance
        ↓
    13. super()
        ↓
    14. Method Overriding
        ↓
    15. Polymorphism
        ↓
    16. Duck Typing
        ↓
    17. Abstraction
        ↓
    18. Dunder Methods
        ↓
    19. @property / Setter
        ↓
    20. Composition
        ↓
    21. Aggregation / Association
        ↓
    22. Nested Class
        ↓
    23. MRO
        ↓
    24. __call__ / Callable Objects
        ↓
    25. Memory Management
        ↓
    26. __name__ == "__main__"
        ↓
    27. OOP Design Principles
        ↓
    28. Projects + Practice
    ```

# 87. Interview Questions

    ## Basic OOP

    ```text
    1. What is OOP?
    2. What is a class?
    3. What is an object?
    4. Difference between class and object?
    5. What is self?
    6. What is __new__()?
    7. What is __init__()?
    8. Difference between __new__() and __init__()?
    9. What is an instance attribute?
    10. What is a class attribute?
    11. What is an instance method?
    12. What is a class method?
    13. What is a static method?
    14. Difference between self and cls?
    ```

    ## Core OOP

    ```text
    15. What are the four pillars of OOP?
    16. What is encapsulation?
    17. What is inheritance?
    18. What are the types of inheritance?
    19. What is polymorphism?
    20. What is abstraction?
    21. What is an abstract class?
    22. What is method overriding?
    23. What is super()?
    24. What is MRO?
    25. What is composition?
    26. What is aggregation?
    27. What is association?
    28. What is a nested class?
    ```

    ## Python-Specific

    ```text
    29. Does Python support traditional method overloading?
    30. What are *args and **kwargs?
    31. What is duck typing?
    32. What is dynamic typing?
    33. What is method binding?
    34. What is a bound method?
    35. What is name mangling?
    36. Is __name truly private?
    37. What is @property?
    38. What is a setter?
    39. What are dunder methods?
    40. What is __str__()?
    41. What is __repr__()?
    42. What is __eq__()?
    43. What is operator overloading?
    44. What is __call__()?
    45. What is a callable object?
    46. What does callable() do?
    ```

    ## Runtime / Memory

    ```text
    47. What does id() return?
    48. What happens when del obj is used?
    49. What is reference counting?
    50. What is garbage collection?
    51. What are reference cycles?
    52. Why should Python's Stack/Heap model not be explained exactly like C/C++?
    53. What is __name__?
    54. Why use if __name__ == "__main__"?
    ```

# 88. Final 20 Lines to Memorize

    ```text
    1. Class → Blueprint / Template

    2. Object → Instance of a Class

    3. self → Conventional reference to the current instance

    4. cls → Conventional reference to the current class

    5. __new__() → Creates/returns an instance

    6. __init__() → Initializes an instance

    7. Instance Attribute → Object-specific state

    8. Class Attribute → Attribute defined on the class

    9. Instance Method → Receives self

    10. Class Method → @classmethod + cls

    11. Static Method → @staticmethod + no automatic self/cls

    12. Encapsulation → Bundle state/behavior + manage access

    13. Inheritance → IS-A relationship

    14. Composition → HAS-A relationship

    15. Polymorphism → Same interface + different behavior

    16. Duck Typing → Behavior/capability matters

    17. Abstraction → Essential interface

    18. Overriding → Child provides a new implementation

    19. MRO → Method Resolution Order

    20. __call__() → Allows an object to be called like a function
    ```

# 89. One-Line Definitions

    ```text
    Class
    → A blueprint/template for creating objects.

    Object
    → An instance of a class.

    self
    → Conventional reference to the current instance.

    cls
    → Conventional reference to the current class.

    __new__()
    → Special method responsible for creating/returning an instance.

    __init__()
    → Special method that initializes an instance.

    Encapsulation
    → Bundling state and behavior while managing access to state.

    Inheritance
    → Mechanism for creating a class based on another class.

    Polymorphism
    → Same interface/operation with different object-specific behavior.

    Abstraction
    → Exposing essential behavior while hiding unnecessary implementation details.

    Duck Typing
    → Relying on supported behavior rather than a concrete type.

    Method Overriding
    → A subclass provides its own implementation of an inherited method.

    Composition
    → A strong whole-part/HAS-A relationship using contained objects.

    Aggregation
    → A looser whole-part/HAS-A relationship where the contained object can exist independently.

    Association
    → A general relationship or interaction between objects.

    Nested Class
    → A class defined inside another class.

    MRO
    → The order Python uses to search classes for methods and attributes.

    __call__()
    → Special method that allows an object to be called using ().

    @property
    → Allows method-based logic to be accessed with attribute syntax.

    @classmethod
    → Creates a method that receives the class as its first argument.

    @staticmethod
    → Creates a method with no automatically supplied instance/class argument.

    __str__()
    → Provides a user-oriented string representation.

    __repr__()
    → Provides a developer-oriented representation.

    __eq__()
    → Defines equality behavior.

    __add__()
    → Defines behavior for +.

    isinstance()
    → Checks whether an object is an instance of a class or its subclasses.

    issubclass()
    → Checks whether one class is a subclass of another.

    callable()
    → Checks whether an object is callable.

    __name__
    → Special module variable indicating the module's execution/import context.
    ```

# 90. Final OOP Concept Map

    ```text
                            PYTHON OOP
                                │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            Class              Object            Methods
            │                  │                  │
            │                  │        ┌─────────┼─────────┐
            │                  │        │         │         │
            │                  │    Instance    Class     Static
            │                  │       │          │         │
            │                  │      self       cls        -
            │                  │
            └──────────────────┼────────────────────────────
                                │
                        Four Pillars
                                │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
        Encapsulation        Inheritance       Polymorphism
            │                  │                  │
            │                  │          ┌───────┴────────┐
            │                  │          │                │
        Property             MRO       Overriding     Duck Typing
        Name Mangling         │
                                │
                            super()
                                │
                            Abstraction
                                │
                        ABC / abstractmethod
                                │
                                │
                    Object Relationships
                                │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
        Composition        Aggregation       Association
            │
            HAS-A

        Inheritance
            IS-A

    Special Methods
        │
        ├── __new__
        ├── __init__
        ├── __str__
        ├── __repr__
        ├── __eq__
        ├── __add__
        └── __call__

    Python Runtime
        │
        ├── id()
        ├── del
        ├── Reference Counting
        └── Garbage Collection

    Modules
        │
        └── __name__ == "__main__"
    ```

    # Final Memory Formula

    ```text
    PYTHON OOP
    │
    ├── Class
    │   └── Blueprint
    │
    ├── Object
    │   └── Instance
    │
    ├── Object Creation
    │   ├── __new__()
    │   └── __init__()
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
    │   ├── __new__
    │   ├── __init__
    │   ├── __str__
    │   ├── __repr__
    │   ├── __eq__
    │   ├── __add__
    │   └── __call__
    │
    ├── Encapsulation Tools
    │   ├── _name
    │   ├── __name
    │   ├── Name Mangling
    │   └── @property
    │
    ├── Inheritance Tools
    │   ├── super()
    │   ├── MRO
    │   ├── isinstance()
    │   └── issubclass()
    │
    ├── Callable Objects
    │   ├── __call__()
    │   └── callable()
    │
    ├── Runtime
    │   ├── id()
    │   ├── del
    │   ├── Reference Counting
    │   └── Garbage Collection
    │
    └── Modules
        └── __name__ == "__main__"
    ```

"""