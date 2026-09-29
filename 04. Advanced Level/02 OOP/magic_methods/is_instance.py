# isinstance() 
# takes two arguments and returns True if the first argument is an instance of the second argument
# 1.first is object
# 2.second is class
class Human:
    pass
if __name__ == "__main__":
    human = Human()
    # print(isinstance(human, Human))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
if __name__ == "__main__":
    person = Person("John", 30)
    print(isinstance(person, Person))
    print(isinstance(person, Human))