"""
====================== Function with Methods & Decorators in Python ======================

In Python, Functions, Methods, and Decorators are closely related, but they
have different purposes.


---------------------------------------------------------------------------
1. Function
---------------------------------------------------------------------------

A Function is a reusable block of code defined independently.

Example:

def add(a, b):
    return a + b


result = add(10, 20)

print(result)

Output:

30

Here:

add(10, 20)

is a function call.


---------------------------------------------------------------------------
2. Method
---------------------------------------------------------------------------

A Method is a function defined inside a class and associated with a class
or its objects.

Example:

class Calculator:

    def add(self, a, b):
        return a + b


calc = Calculator()

result = calc.add(10, 20)

print(result)

Output:

30

Here:

calc.add(10, 20)

is a method call.

The self parameter refers to the current object.

Conceptually:

calc.add(10, 20)

works like:

Calculator.add(calc, 10, 20)


---------------------------------------------------------------------------
3. What is a Decorator?
---------------------------------------------------------------------------

A Decorator is a function that modifies or extends the behavior of another
function or method without changing its original source code.

Basic syntax:

@decorator
def function():
    pass


Example:

def my_decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper


@my_decorator
def hello():
    print("Hello")


hello()

Output:

Before function
Hello
After function


This:

@my_decorator
def hello():
    print("Hello")

is approximately equivalent to:

def hello():
    print("Hello")


hello = my_decorator(hello)


---------------------------------------------------------------------------
4. Decorators with Methods
---------------------------------------------------------------------------

Decorators can also be applied to methods inside a class.

Example:

def log_method(func):

    def wrapper(self):
        print("Method started")

        func(self)

        print("Method finished")

    return wrapper


class Student:

    @log_method
    def show(self):
        print("Student information")


student = Student()

student.show()

Output:

Method started
Student information
Method finished

Here:

@log_method

decorates the show() method.


---------------------------------------------------------------------------
5. Built-in Method Decorators
---------------------------------------------------------------------------

Python provides several important decorators for methods.

Common method decorators:

1. @staticmethod
2. @classmethod
3. @property
4. @property.setter


---------------------------------------------------------------------------
6. @staticmethod
---------------------------------------------------------------------------

A static method does not automatically receive self or cls.

Example:

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))

Output:

30


---------------------------------------------------------------------------
7. @classmethod
---------------------------------------------------------------------------

A class method automatically receives the class as cls.

Example:

class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


Student.show_school()

Output:

ABC School


Here:

cls

refers to the Student class.


---------------------------------------------------------------------------
8. @property
---------------------------------------------------------------------------

@property allows a method to be accessed like an attribute.

Example:

class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


student = Student("Faruk")

print(student.name)

Output:

Faruk


Instead of:

student.name()

we use:

student.name


---------------------------------------------------------------------------
9. @property.setter
---------------------------------------------------------------------------

@property.setter is used to control how a property is modified.

Example:

class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


student = Student("Faruk")

print(student.name)

student.name = "Ahmed"

print(student.name)

Output:

Faruk
Ahmed


---------------------------------------------------------------------------
10. Function → Method → Decorator
---------------------------------------------------------------------------

The relationship can be remembered like this:


Function
   ↓
Reusable block of code


Method
   ↓
Function defined inside a class
   ↓
Associated with an object or class


Decorator
   ↓
Modifies or extends a function or method
   ↓
Uses @decorator syntax


---------------------------------------------------------------------------
11. Important Examples
---------------------------------------------------------------------------

Function:

def function():
    pass


Method:

class MyClass:

    def method(self):
        pass


Static Method:

class MyClass:

    @staticmethod
    def method():
        pass


Class Method:

class MyClass:

    @classmethod
    def method(cls):
        pass


Property:

class MyClass:

    @property
    def value(self):
        return self._value


---------------------------------------------------------------------------
12. In Short
---------------------------------------------------------------------------

Function:
    A reusable block of code defined independently.

Method:
    A function defined inside a class.

Decorator:
    A function that modifies or extends the behavior of another
    function or method.

Instance Method:
    def method(self):

Class Method:
    @classmethod
    def method(cls):

Static Method:
    @staticmethod
    def method():

Property:
    @property
    def value(self):


Final Concept:

Function
    ↓
Independent callable block


Method
    ↓
Function associated with a class


Decorator
    ↓
Modifies or extends the behavior of a function or method

"""