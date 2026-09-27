# ===================== what is Multilevel Inheritance =====================
# Multilevel Inheritance is a type of inheritance in which a class is child (derived)
# class of another class which is child (derived) class of another class.

# Base = Parent
# Derived = Child

# Parent class
class Parent:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Parent Name: {self.name}")

# Child class
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Parent of constructor call
        self.age = age

    def display_age(self):
        print(f"Child Age: {self.age}")

# GrandChild class
class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)  # Child of constructor call
        self.address = address

    def display_address(self):
        print(f"GrandChild Address: {self.address}")

# Object
gc = GrandChild("John", 20, "Bogura")

# Call methods
gc.display_name()      # Parent of method
gc.display_age()       # Child of method
gc.display_address()   # GrandChild of method
