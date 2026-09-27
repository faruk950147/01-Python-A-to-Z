# ===================== what is Single Inheritance =====================
# Base = Parent
# Derived = Child
# Single Inheritance is a type of inheritance in which a class is child (Derived) 
# of only one parent (Base) class.


# ===================== Example =====================

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

child = Child("John", 20)
print(child.name, child.age)


