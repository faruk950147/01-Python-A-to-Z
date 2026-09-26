"""
# Python Instance, Class, and Static Methods

Python classes commonly use three types of methods:

1. **Instance Method**
2. **Class Method**
3. **Static Method**

---

# 1. Instance Method

An **instance method** is a method that works with a specific object (instance).

It receives the object automatically through the `self` parameter.

### Syntax

```python
class ClassName:

    def method(self):
        # instance-specific logic
        pass
```

### Example

```python
class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showName(self):
        print(f"Name: {self.name}")

    def showAge(self):
        print(f"Age: {self.age}")

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


human = Human("Faruk", 22)

human.showName()
human.showAge()
human.showInfo()
```

### Output

```text
Name: Faruk
Age: 22
Name: Faruk
Age: 22
```

### Important Points

* Instance methods use `self`.
* `self` refers to the current object.
* They can access instance variables.
* They can also access class variables.
* They are normally called using an object.

```python
human.showName()
```

Conceptually:

```python
Human.showName(human)
```

---

# 2. Class Method

A **class method** is a method that works with the class itself rather than a specific instance.

It receives the class automatically through the `cls` parameter.

A class method is created using the `@classmethod` decorator.

### Syntax

```python
class ClassName:

    @classmethod
    def method(cls):
        # class-level logic
        pass
```

### Why Use a Class Method?

A class method is useful when the method needs to:

* Access class-level data.
* Modify class-level data.
* Create alternative constructors.
* Perform operations related to the class rather than a particular object.

### Example

```python
class Human:

    species = "Homo sapiens"

    @classmethod
    def showClassName(cls):
        print(f"Class Name: {cls.__name__}")
        print(f"Species: {cls.species}")


Human.showClassName()
```

### Output

```text
Class Name: Human
Species: Homo sapiens
```

Here:

```python
cls
```

refers to:

```python
Human
```

Conceptually:

```python
Human.showClassName()
```

passes the class automatically.

---

# 3. Class Method Can Modify Class Variables

A class method is especially useful for modifying shared class-level data.

```python
class Person:

    name = "John"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()

p1.changeName("Doe")

print(p1.name)
print(Person.name)
```

### Output

```text
Doe
Doe
```

The class variable was changed:

```python
Person.name
```

from:

```text
John
```

to:

```text
Doe
```

Because `cls` refers to the class.

---

# 4. Instance Method vs Class Method

Consider this example:

```python
class Person:

    college_name = "TMSS Technical Institute"

    def changeName(self, college_name):
        self.college_name = college_name
```

When we write:

```python
p1 = Person()

p1.changeName("TTI")
```

the statement:

```python
self.college_name = college_name
```

creates an **instance variable**.

It does NOT modify the class variable.

### Example

```python
class Person:

    college_name = "TMSS Technical Institute"

    def changeName(self, college_name):
        self.college_name = college_name


p1 = Person()

p1.changeName("TTI")

print(p1.college_name)
print(Person.college_name)
```

### Output

```text
TTI
TMSS Technical Institute
```

Why?

Because:

```python
self.college_name
```

means:

> Store the value in this particular object.

While:

```python
Person.college_name
```

refers to the class variable.

---

# 5. Instance Method Modifying a Class Variable Directly

An instance method can modify a class variable if we explicitly access the class.

```python
class Person:

    name = "John"

    def changeName(self, name):
        Person.name = name


p1 = Person()

p1.changeName("Doe")

print(p1.name)
print(Person.name)
```

### Output

```text
Doe
Doe
```

Here:

```python
Person.name = name
```

directly modifies the class variable.

This is different from:

```python
self.name = name
```

because `self.name` creates or modifies an instance attribute.

---

# 6. Class Method vs Direct Class Access

The previous example can be written more cleanly using a class method:

```python
class Person:

    name = "John"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()

p1.changeName("Doe")

print(p1.name)
print(Person.name)
```

### Output

```text
Doe
Doe
```

The advantage is that:

```python
cls.name = name
```

works with the class that invoked the method.

This is generally more flexible than hard-coding:

```python
Person.name = name
```

especially when inheritance is involved.

---

# 7. Static Method

A **static method** is a method that does not receive an instance or class reference automatically.

It uses the `@staticmethod` decorator.

### Syntax

```python
class ClassName:

    @staticmethod
    def method():
        pass
```

A static method receives:

* No `self`
* No `cls`

### Example

```python
class Human:

    @staticmethod
    def showClassInfo():
        print("This is the Human class, representing all human beings.")


Human.showClassInfo()
```

### Output

```text
This is the Human class, representing all human beings.
```

---

# 8. Why Use a Static Method?

A static method is useful when a function:

* Does not need object-specific data.
* Does not need class-specific data.
* Is logically related to the class.
* Performs general-purpose utility work.

For example:

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(10, 20))
```

### Output

```text
30
```

The method does not need:

```python
self
```

or:

```python
cls
```

because it does not need information from an object or class.

---

# 9. Static Method Can Access Class Variables Explicitly

A static method does not automatically receive `cls`.

However, it can access class variables explicitly using the class name.

```python
class Person:

    name = "John"

    @staticmethod
    def changeName(name):
        Person.name = name


p1 = Person()

p1.changeName("Doe")

print(p1.name)
print(Person.name)
```

### Output

```text
Doe
Doe
```

This works because the method explicitly uses:

```python
Person.name
```

The static method itself does not receive `Person` automatically.

---

# 10. Instance Method vs Static Method

```python
class Person:

    name = "John"

    def instanceMethod(self):
        print(self.name)

    @staticmethod
    def staticMethod():
        print("Static method")
```

### Instance Method

```python
p1.instanceMethod()
```

Python automatically passes:

```python
p1
```

as `self`.

Conceptually:

```python
Person.instanceMethod(p1)
```

### Static Method

```python
Person.staticMethod()
```

No object or class reference is automatically passed.

---

# 11. Complete Example

```python
class Human:

    # Class variable
    species = "Homo sapiens"

    # Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance methods
    def showName(self):
        print(f"Name: {self.name}")

    def showAge(self):
        print(f"Age: {self.age}")

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    # Class method
    @classmethod
    def showClassName(cls):
        print(f"Class Name: {cls.__name__}")
        print(f"Species: {cls.species}")

    # Static method
    @staticmethod
    def showClassInfo():
        print("This is the Human class, representing all human beings.")


if __name__ == "__main__":

    # Creating an object
    human = Human("Faruk", 22)

    # Instance methods
    print("Instance Method Outputs:")
    human.showName()
    human.showAge()
    human.showInfo()

    print("------------------------")

    # Class method
    print("Class Method Output:")
    Human.showClassName()

    print("------------------------")

    # Static method
    print("Static Method Output:")
    Human.showClassInfo()
```

### Output

```text
Instance Method Outputs:
Name: Faruk
Age: 22
Name: Faruk
Age: 22
------------------------
Class Method Output:
Class Name: Human
Species: Homo sapiens
------------------------
Static Method Output:
This is the Human class, representing all human beings.
```

---

# 12. Main Difference

| Method Type     | First Parameter | Works With            | Can Access Instance Data Automatically? | Can Access Class Data Automatically? |
| --------------- | --------------- | --------------------- | --------------------------------------- | ------------------------------------ |
| Instance Method | `self`          | Object                | Yes                                     | Yes                                  |
| Class Method    | `cls`           | Class                 | No                                      | Yes                                  |
| Static Method   | None            | Neither automatically | No                                      | No                                   |

---

# 13. Simple Memory Trick

Think of the three methods like this:

```text
Instance Method
       ↓
     self
       ↓
    Object
```

```text
Class Method
       ↓
      cls
       ↓
     Class
```

```text
Static Method
       ↓
   No reference
       ↓
 General utility
```

---

# 14. One Class Containing All Three

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def showStudent(self):
        print(f"Student: {self.name}")

    # Class Method
    @classmethod
    def showSchool(cls):
        print(f"School: {cls.school}")

    # Static Method
    @staticmethod
    def welcome():
        print("Welcome to the Student class!")


student = Student("Faruk")

student.showStudent()

Student.showSchool()

Student.welcome()
```

Output:

```text
Student: Faruk
School: ABC School
Welcome to the Student class!
```

---

# 15. Important Concept

The decorators change **how Python binds the function when accessed through the class/object**.

```python
def method(self):
    ...
```

→ Instance method

```python
@classmethod
def method(cls):
    ...
```

→ Class method

```python
@staticmethod
def method():
    ...
```

→ Static method

The key idea is:

```text
Instance Method → self → current object
Class Method    → cls  → current class
Static Method   → no automatic reference
```

---

# 16. Final Summary

### Instance Method

```python
def method(self):
```

* Uses `self`.
* Works with an object.
* Can access instance data.
* Can access class data.
* Most common method type.

### Class Method

```python
@classmethod
def method(cls):
```

* Uses `cls`.
* Works with the class.
* Can access class variables.
* Can modify class variables.
* Useful for class-level operations and alternative constructors.

### Static Method

```python
@staticmethod
def method():
```

* Uses neither `self` nor `cls`.
* Does not automatically receive an object or class.
* Useful for utility functions logically related to the class.
* Can access class data only explicitly, for example through `Person.name`.

## Quick Formula

```text
Instance Method
      ↓
    self
      ↓
   Object
```

```text
Class Method
      ↓
     cls
      ↓
   Class
```

```text
Static Method
      ↓
   No self
   No cls
      ↓
Utility Logic
```

"""

class Human:
    def __init__(self, name):
        self.name = name
    
    def instance_method(self, message):
        return f"Instance method called with {self.name}: {message}"
    
    @classmethod
    def class_method(cls):
        return f"Class method called with {cls.__name__}"
    
    @staticmethod
    def static_method():
        return "Static method called"
    
if __name__ == "__main__":
    human = Human("John")
    print(human.instance_method("Hello"))
    print(Human.class_method())
    print(Human.static_method())


# =================================================================   
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
        print(cls)

    
class Math:

    # Static Method
    @staticmethod
    def add(a, b):
        return a + b


if __name__ == '__main__':
    # Instance method
    s1 = Student("Faruk")
    s1.show()

    # Class method
    Student.change_school("ABC School")
    print(Student.school)

    # Static method
    result = Math.add(5, 3)
    print(result)
