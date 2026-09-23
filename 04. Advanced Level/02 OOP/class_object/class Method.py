# Class Method:
# A method that is bound to the class rather than the instance (object).
# It can access or modify class-level data (shared by all objects),
# but it cannot access instance-specific data.
# It is defined using the @classmethod decorator.


# 1. Instance Method Example:
# Using an instance method to change a class variable will NOT affect the class itself.
# It only creates a new instance variable for that particular object.

class Person:
    # Class variable (shared by all objects)
    college_name = "TMSS Technical Institute"

    def changeName(self, college_name):
        # 'self' refers to the instance (object), not the class.
        # This creates a NEW instance variable 'college_name'
        # instead of modifying the class variable.
        self.college_name = college_name


if __name__ == "__main__":
    p1 = Person()
    p1.changeName("TTI")  # Changes only for this object

    print(p1.college_name)      # Output: TTI (instance variable)
    print(Person.college_name)  # Output: TMSS Technical Institute (class variable remains unchanged)


# 2. Instance Method modifying Class Variable (using class name directly):
# Accessing and changing the class variable directly will modify it for all objects.

class Person2:
    name = "John"

    def changeName(self, name):
        # Modifying the class variable directly through the class
        Person2.name = name


if __name__ == "__main__":
    p1 = Person2()
    p1.changeName("Doe")

    print(p1.name)       # Output: Doe
    print(Person2.name)  # Output: Doe


# 3. Class Method Example:
# Clean and preferred way to modify class-level data.

class Person3:
    name = "John"

    @classmethod
    def changeName(cls, name):
        # 'cls' refers to the class itself
        cls.name = name


if __name__ == "__main__":
    p1 = Person3()
    p1.changeName("Doe")

    print(p1.name)       # Output: Doe
    print(Person3.name)  # Output: Doe


# 4. Combined Example: Instance, Class, and Static Methods

class Human:
    # Class variable (shared by all instances)
    species = "Homo sapiens"

    def __init__(self, name, age):
        # Instance variables (unique to each object)
        self.name = name
        self.age = age

    # Instance Methods
    # Require an object (use 'self')
    def showName(self):
        print(f"Name: {self.name}")

    def showAge(self):
        print(f"Age: {self.age}")

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    # Class Method
    # Works on the class itself (takes 'cls')
    @classmethod
    def showClassName(cls):
        print(f"Class Name: {cls.__name__}")
        print(f"Species: {cls.species}")

    # Static Method
    # Does not take 'self' or 'cls'
    # Used for general-purpose logic related to the class
    @staticmethod
    def showClassInfo():
        print("This is the Human class, representing all human beings.")


if __name__ == "__main__":
    human = Human("Faruk", 22)

    # Instance Methods
    print("Instance Method Outputs:")
    human.showName()
    human.showAge()
    human.showInfo()

    print("------------------------")

    # Class Method
    print("Class Method Output:")
    Human.showClassName()

    print("------------------------")

    # Static Method
    print("Static Method Output:")
    Human.showClassInfo()
