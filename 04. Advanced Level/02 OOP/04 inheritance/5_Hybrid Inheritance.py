# Parent class
class Parent:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Parent Name: {self.name}")

# Child1 class
class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display_age(self):
        print(f"Child1 Age: {self.age}")

# Child2 class
class Child2(Parent):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def display_address(self):
        print(f"Child2 Address: {self.address}")

# GrandChild class (Multiple Inheritance)
class GrandChild(Child1, Child2):
    def __init__(self, name, age, address, school):
        Child1.__init__(self, name, age)
        Child2.__init__(self, name, address)
        self.school = school

    def display_school(self):
        print(f"GrandChild School: {self.school}")

# Object
gc = GrandChild("John", 20, "Bogura", "TMSS Tech")
gc.display_name()      # Parent method
gc.display_age()       # Child1 method
gc.display_address()   # Child2 method
gc.display_school()    # GrandChild method
