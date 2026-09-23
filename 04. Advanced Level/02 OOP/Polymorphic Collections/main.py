# polymorphism collections is a feature of object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). 
from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Subclasses
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

# Collection of animals
animals = [Dog(), Cat(), Bird()]

# Polymorphism in action
for animal in animals:
    print(animal.speak())

