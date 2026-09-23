# ====================== What is Polymorphism ======================

"""
Polymorphism is a feature of Object-Oriented Programming (OOP)
that allows objects of different classes to be treated through
a common interface.

The word "Polymorphism" means:

Poly  = Many
Morph = Forms

Therefore:

Polymorphism = One Interface, Many Forms

Different classes can provide their own implementation
of the same method.
"""


# ====================== What is Polymorphism with Collections ======================

"""
Polymorphism with Collections means storing objects of different
classes in the same collection, such as a list, and using the
same method call on every object.

Each object can respond differently to the same method call.

Example:

animals = [Dog(), Cat(), Bird()]

Here:

Dog, Cat, and Bird are different classes.

But all of them provide the same method:

speak()

Therefore, we can use:

for animal in animals:
    animal.speak()

The same interface is used for different objects.
"""


# ====================== Abstract Base Class ======================

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


# ====================== Subclasses ======================

class Dog(Animal):

    def speak(self):
        return "Woof!"


class Cat(Animal):

    def speak(self):
        return "Meow!"


class Bird(Animal):

    def speak(self):
        return "Chirp!"


# ====================== Collection of Objects ======================

animals = [
    Dog(),
    Cat(),
    Bird()
]


# ====================== Polymorphism in Action ======================

for animal in animals:
    print(animal.speak())


# ====================== Output ======================

"""
Woof!
Meow!
Chirp!
"""


# ====================== How It Works ======================

"""
The collection contains different objects:

animals
   |
   +---- Dog()
   |
   +---- Cat()
   |
   +---- Bird()


Then:

for animal in animals:
    print(animal.speak())


First:

animal = Dog()
animal.speak()
        ↓
"Woof!"


Second:

animal = Cat()
animal.speak()
        ↓
"Meow!"


Third:

animal = Bird()
animal.speak()
        ↓
"Chirp!"
"""


# ====================== Same Interface, Different Behavior ======================

"""
The method name is the same:

speak()

But the behavior is different:

Dog  → "Woof!"
Cat  → "Meow!"
Bird → "Chirp!"

This is polymorphism.
"""


# ====================== Important Point ======================

"""
The for loop does not need to know the exact class of the object.

It only expects that the object provides:

speak()

Therefore:

for animal in animals:
    animal.speak()

works with Dog, Cat, and Bird.

This is called Duck Typing / Polymorphic Behavior.
"""


# ====================== Without Knowing Object Type ======================

for animal in animals:

    print(
        type(animal).__name__,
        "says:",
        animal.speak()
    )


# Output:

"""
Dog says: Woof!
Cat says: Meow!
Bird says: Chirp!
"""


# ====================== Polymorphism Flow ======================

"""
                    Animal
                       |
             +---------+---------+
             |         |         |
             v         v         v
            Dog       Cat      Bird
             |         |         |
          speak()   speak()   speak()
             |         |         |
             v         v         v
          "Woof!"   "Meow!"   "Chirp!"


                Collection
                    |
                    v
          [Dog(), Cat(), Bird()]
                    |
                    v
             for animal in
                animals
                    |
                    v
             animal.speak()
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
      Dog()       Cat()       Bird()
        |           |           |
        v           v           v
     "Woof!"     "Meow!"     "Chirp!"
"""


# ====================== Why Use Collections with Polymorphism ======================

"""
Polymorphism with collections helps us:

1. Store different types of objects together.

2. Use one common interface.

3. Avoid writing separate code for each class.

4. Make code easier to extend.

5. Reduce if/else or type-checking logic.

6. Improve flexibility and maintainability.
"""


# ====================== Example Without Polymorphism ======================

"""
Without polymorphism, we might write:

for animal in animals:

    if isinstance(animal, Dog):
        print(animal.speak())

    elif isinstance(animal, Cat):
        print(animal.speak())

    elif isinstance(animal, Bird):
        print(animal.speak())


This is unnecessary.

With polymorphism, we simply write:
"""


for animal in animals:
    print(animal.speak())


# ====================== Adding a New Class ======================

class Cow(Animal):

    def speak(self):
        return "Moo!"


# Add Cow to the same collection

animals.append(Cow())


# The same code still works

for animal in animals:
    print(animal.speak())


# Output:

"""
Woof!
Meow!
Chirp!
Moo!
"""


# ====================== Key Point ======================

"""
We added a completely new class:

Cow

But we did not need to change this code:

for animal in animals:
    print(animal.speak())

This is one of the major benefits of polymorphism.
"""


# ====================== Polymorphism + Inheritance ======================

"""
Animal
  |
  +---- Dog
  |
  +---- Cat
  |
  +---- Bird
  |
  +---- Cow


All subclasses inherit from Animal.

Animal defines the common interface:

speak()

Each subclass provides its own implementation:

Dog  → Woof!
Cat  → Meow!
Bird → Chirp!
Cow  → Moo!
"""


# ====================== Polymorphism + Abstract Class ======================

"""
Animal is an Abstract Base Class (ABC).

The abstract method:

@abstractmethod
def speak(self):
    pass

forces subclasses to provide their own speak() implementation.

Therefore:

Dog  → must implement speak()
Cat  → must implement speak()
Bird → must implement speak()
Cow  → must implement speak()
"""


# ====================== Simple Definition ======================

"""
Polymorphism with Collections

=

Storing objects of different classes in one collection
and using the same method or interface on each object,
while each object provides its own behavior.
"""


# ====================== Easy Way to Remember ======================

"""
One Collection
      |
      v
[Dog, Cat, Bird]
      |
      v
Same Method
   speak()
      |
      +--------+--------+
      |        |        |
      v        v        v
    Woof!    Meow!    Chirp!


One Interface + Many Implementations
                =
           Polymorphism
"""


# ====================== Final Example ======================

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        return "Woof!"


class Cat(Animal):

    def speak(self):
        return "Meow!"


class Bird(Animal):

    def speak(self):
        return "Chirp!"


class Cow(Animal):

    def speak(self):
        return "Moo!"


# Collection containing different objects

animals = [
    Dog(),
    Cat(),
    Bird(),
    Cow()
]


# Polymorphism

for animal in animals:
    print(animal.speak())


# Output:

"""
Woof!
Meow!
Chirp!
Moo!
"""


# ====================== Final Key Point ======================

"""
Polymorphism

    =
One Interface
    +
Many Implementations


In this example:

Common Interface:
    speak()

Implementations:
    Dog  → Woof!
    Cat  → Meow!
    Bird → Chirp!
    Cow  → Moo!


Collection:
    [Dog(), Cat(), Bird(), Cow()]

Same Code:
    for animal in animals:
        print(animal.speak())


Different objects
        ↓
Same method call
        ↓
Different behavior
        ↓
Polymorphism
"""