# Static Method: 
# A static method is bound to the class, not the instance (object).
# It cannot access or modify class or instance state directly.
# It is defined using the @staticmethod decorator.

# 1. Instance Method Example:
# Changing the name through an instance (object)
# will NOT change the class variable.
from ast import If


class Person:
    name = "John"

    def changeName(self, name):
        # 'self' refers to the object (instance)
        # This creates a new instance variable 'name' for this object only
        self.name = name


if __name__ == "__main__":
    p1 = Person()
    p1.changeName("Doe")

    print(p1.name)       # Output: Doe  (instance variable)
    print(Person.name)   # Output: John (class variable remains unchanged)


# 2. Class Method Example:
# Changing the name using a class reference will modify
# the class variable for all instances.
# Directly modifying the class variable using the class name
class Person2:
    name = "John"

    @classmethod
    def changeName(cls, name):
        # cls refers to the class itself (Person2)
        # This modifies the class variable for all instances
        # Person2.name = name (alternative way)
        cls.name = name

if __name__ == "__main__":
    # Now:
    p1 = Person2()
    p1.changeName("Doe")

    print(p1.name)        # Doe
    print(Person2.name)   # Doe


# 3. Static Method Example:
# Static methods don’t take 'self' or 'cls' as parameters.
# They behave like normal functions but logically belong to the class.
class Person3:
    name = "John"

    @staticmethod
    def changeName(name):
        # Accessing class variable using class name
        Person3.name = name


if __name__ == "__main__":
    p1 = Person3()
    p1.changeName("Doe")

    print(p1.name)        # Output: Doe
    print(Person3.name)   # Output: Doe
