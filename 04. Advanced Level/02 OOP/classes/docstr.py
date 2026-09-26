class Person:
    """Person class this is docstring"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
if __name__ == "__main__":
    person = Person("John", 30)
    print(person.__doc__) # access docstring