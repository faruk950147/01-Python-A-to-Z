# ===================== what is Multiple Inheritance =====================
# Multiple Inheritance is a type of inheritance in which a class is child (derived)
# class of more than one parent (base) class.

# Base = Parent
# Derived = Child

# Example

class Parent1:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"I'm from Parent1 class attribute name: {self.name}")

class Parent2:
    def __init__(self, age):
        self.age = age
        
    def display(self):
        print(f"I'm from Parent2 class attribute age: {self.age}")

class Child(Parent1, Parent2):
    def __init__(self, name, age, address):
        Parent1.__init__(self, name)
        Parent2.__init__(self, age)
        self.address = address
        
    def display(self):
        Parent1.display(self)
        Parent2.display(self)
        print(f"I'm from Child Class attribute address: {self.address}")

child = Child("Faruk", 20, "Bogura")
child.display()

# Output
# I'm from Parent1 class attribute name: Faruk
# I'm from Parent2 class attribute age: 20
# I'm from Child Class attribute address: Bogura
