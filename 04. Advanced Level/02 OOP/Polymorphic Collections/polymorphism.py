# Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). 

class Animal1:
    def speak(self):
        return "Some generic sound"

class Dog1(Animal1):
    def speak(self):
        return "Woof!"

class Cat1(Animal1):
    def speak(self):
        return "Meow!"
    
if __name__ == "__main__":
    dog = Dog1()
    cat = Cat1()
    print(dog.speak())  # Output: Woof!
    print(cat.speak())  # Output: Meow!
    print()

# In Python, polymorphism is achieved through:

# 1. Method Overloading: Allowing a class to have multiple methods with the same name but different parameters.
# 2. Method Overriding: Implementing a method in a subclass with the same name and signature as in its superclass.
# 3. Duck Typing: Allowing objects of different classes to be used interchangeably if they have the same interface (attributes and methods).
# 4. Operator Overloading: Allowing operators to work with different data types.
# 5. Polymorphic Collections: Using a single collection to store objects of different classes.

# =============================
# 1. Method Overloading (default argument)
# =============================
class Math:
    def add(self, a, b=0):
        return a + b

print("Method Overloading Examples:")
m = Math()
print(m.add(5))       # Output: 5
print(m.add(5, 10))   # Output: 15
print()

# =============================
# 2. Method Overriding ()
# =============================
class Animal2:
    def speak(self):
        return "Some generic sound"

class Dog2(Animal2):
    def speak(self):
        return "Woof!"

class Cat2(Animal2):
    def speak(self):
        return "Meow!"

print("Method Overriding Examples:")
dog = Dog2()
cat = Cat2()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print()

# =============================
# 3. Duck Typing ()
# =============================
class Bird2:
    def speak(self):
        return "Chirp!"

def animal_sound(animal):
    print(animal.speak())

print("Duck Typing Example:")
bird = Bird2()
animal_sound(dog)   # Output: Woof!
animal_sound(cat)   # Output: Meow!
animal_sound(bird)  # Output: Chirp!
print()

# =============================
# 4. Operator Overloading
# =============================
print("Operator Overloading Examples:")
print(5 + 10)        # Output: 15 (integer)
print("Hi " + "Bye") # Output: Hi Bye (string)
print([1,2] + [3,4]) # Output: [1, 2, 3, 4]
print()

# =============================
# 5. Polymorphic Collections
# =============================
print("Polymorphic Collections Example:")
animals = [dog, cat, bird]  # one collection for different classes
for a in animals:
    print(a.speak())
# Output:
# Woof!
# Meow!
# Chirp!
