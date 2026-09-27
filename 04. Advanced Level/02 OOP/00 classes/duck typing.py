# ====================== Python Duck Typing ======================

"""
Duck Typing হলো Python-এর একটি concept যেখানে object-এর
actual type/class-এর চেয়ে object-এর behavior বেশি গুরুত্বপূর্ণ।

সহজভাবে:

"If it looks like a duck, swims like a duck,
and quacks like a duck — then it is a duck."

Python-এর ক্ষেত্রে এর অর্থ:

Object কোন class-এর সেটা সবসময় গুরুত্বপূর্ণ নয়।
Object-এর প্রয়োজনীয় method বা behavior আছে কিনা,
সেটাই গুরুত্বপূর্ণ।
"""

# ============================================================

# Basic Example

# ============================================================

class Duck:

```
def sound(self):
    return "Quack"
```

class Dog:

```
def sound(self):
    return "Bark"
```

def make_sound(animal):
print(animal.sound())

duck = Duck()
dog = Dog()

make_sound(duck)       # Quack
make_sound(dog)        # Bark

# ============================================================

# এখানে কী হলো?

# ============================================================

"""
Python check করেনি:

```
"animal কি Duck class-এর object?"
"animal কি Dog class-এর object?"
```

বরং Python শুধু দেখেছে:

```
animal-এর sound() method আছে কি না?
```

Duck-এর sound() আছে
Dog-এর sound() আছে

তাই দুই object-ই make_sound() function-এর সাথে কাজ করেছে।
"""

# ============================================================

# Key Point

# ============================================================

"""
Duck Typing:

✔ Type-এর পরিবর্তে behavior গুরুত্বপূর্ণ
✔ Strict type checking প্রয়োজন নেই
✔ Object-এর required method থাকলেই কাজ করতে পারে
✔ Runtime-এ method lookup হয়
✔ Python code-কে flexible করে
"""

# ============================================================

# Another Duck Typing Example

# ============================================================

class Duck:

```
def quack(self):
    print("Quack quack!")
```

class Person:

```
def quack(self):
    print("I can quack too!")
```

def make_it_quack(being):

```
# We don't care whether being is Duck or Person.
# We only care whether quack() exists.

being.quack()
```

d = Duck()
p = Person()

make_it_quack(d)

# Output:

# Quack quack!

make_it_quack(p)

# Output:

# I can quack too!

# ============================================================

# Why is this called Duck Typing?

# ============================================================

"""
ধরা যাক আমাদের এমন একটি object দরকার
যেটা quack() করতে পারে।

আমরা বলছি না:

```
"তোমাকে অবশ্যই Duck হতে হবে।"
```

আমরা বলছি:

```
"তোমার quack() method থাকতে হবে।"
```

অর্থাৎ:

```
Required behavior → quack()
```

Class/type → Not important

যদি কোনো object quack() করতে পারে,
তাহলে সেটাকে আমাদের function ব্যবহার করতে পারবে।
"""

# ============================================================

# Duck Typing vs Type Checking

# ============================================================

class Duck:

```
def quack(self):
    print("Quack!")
```

class Person:

```
def quack(self):
    print("Person can quack!")
```

def make_sound(obj):

```
# No type checking
obj.quack()
```

make_sound(Duck())
make_sound(Person())

# ============================================================

# Explicit Type Checking

# ============================================================

def make_sound_strict(obj):

```
if isinstance(obj, Duck):
    obj.quack()
else:
    print("Object is not a Duck")
```

make_sound_strict(Duck())

make_sound_strict(Person())

"""
এই approach-এ আমরা explicitly check করছি:

```
isinstance(obj, Duck)
```

কিন্তু Duck Typing-এ আমরা type check করি না।

আমরা সরাসরি required behavior ব্যবহার করি:

```
obj.quack()
```

"""

# ============================================================

# What Happens If Method Does Not Exist?

# ============================================================

class Cat:
pass

cat = Cat()

# cat.quack()

"""
Output:

AttributeError:
'Cat' object has no attribute 'quack'

কারণ Cat object-এর quack() method নেই।

Python আগে থেকে type দেখে function বন্ধ করেনি।
Runtime-এ method access করার সময় error হয়েছে।
"""

# ============================================================

# Duck Typing and Runtime Behavior

# ============================================================

def run_program(obj):

```
obj.run()
```

class Computer:

```
def run(self):
    print("Computer is running")
```

class Program:

```
def run(self):
    print("Program is running")
```

computer = Computer()
program = Program()

run_program(computer)
run_program(program)

"""
Computer এবং Program completely different classes।

তবুও দুটো object কাজ করছে কারণ:

```
Computer → run()
Program  → run()
```

Function-এর জন্য class identity গুরুত্বপূর্ণ নয়।
Required behavior গুরুত্বপূর্ণ।
"""

# ============================================================

# Duck Typing with File-like Objects

# ============================================================

"""
Python-এর অনেক API এমনভাবে design করা হয়
যেখানে object-এর specific class না দেখে
required methods ব্যবহার করা হয়।

উদাহরণ:

একটি function যদি write() method ব্যবহার করে,
তাহলে সেই object file, memory buffer বা অন্য কোনো
file-like object হতে পারে।

Concept:

```
"Can you perform the required operation?"
```

Class কী সেটা সবসময় গুরুত্বপূর্ণ নয়।
"""

# ============================================================

# Duck Typing and len()

# ============================================================

"""
len() example-টি Duck Typing-এর সাথে related
behavior-based programming বোঝাতে পারে।

String:
"""

print(len("Hello"))

"""
List:
"""

print(len([1, 2, 3]))

"""
Tuple:
"""

print(len((10, 20, 30)))

"""
এগুলো আলাদা type হলেও len() ব্যবহার করা যায়।

কারণ Python object-এর length বের করার জন্য
appropriate protocol/behavior ব্যবহার করে।

তবে technically এই example-টিকে
"Python's length protocol" বলা আরও precise।
"""

# ============================================================

# Duck Typing vs Static Typing

# ============================================================

"""
Duck Typing
-----------

Python-এ object-এর behavior-এর ওপর বেশি নির্ভর করা হয়।

Example:

```
def make_sound(animal):
    animal.sound()
```

এখানে animal-এর exact type নির্দিষ্ট করা নেই।

যে object-এর sound() আছে,
সে function-এর সাথে কাজ করতে পারে।
"""

"""
Static Typing
-------------

Static typing-এ variable/function-এর type
আগে থেকেই declare বা constrain করা হয়।

Java example:

```
int add(int x, int y) {
    return x + y;
}
```

এখানে x এবং y-এর type int।

String argument দিলে সেটা এই function-এর
declared type-এর সাথে compatible নয়।
"""

# ============================================================

# Important Correction

# ============================================================

"""
এই example:

```
def add(x, y):
    return x + y

add(5, 10)
add("A", "B")
```

এটি সরাসরি Duck Typing-এর best example নয়।

এটি মূলত Python-এর:

```
✔ Dynamic Typing
✔ Operator Polymorphism
```

বোঝায়।

কারণ + operator:

```
int + int
str + str
```

দুই ক্ষেত্রেই কাজ করে।

Duck Typing-এর clearer example হলো:

```
def make_sound(obj):
    obj.sound()
```

এখানে function object-এর class না দেখে
তার behavior ব্যবহার করছে।
"""

# ============================================================

# Dynamic Typing

# ============================================================

"""
Python dynamically typed language।

Variable-এর type আগে থেকে fixed থাকে না।
Runtime-এ object-এর type নির্ধারিত হয়।
"""

x = 10

print(type(x))

# <class 'int'>

x = "Hello"

print(type(x))

# <class 'str'>

"""
এখানে x নিজে int বা string হয়ে যায়নি।

বরং:

```
x → 10
```

পরে:

```
x → "Hello"
```

অর্থাৎ variable একটি reference/name,
আর object-এর নিজস্ব type থাকে।
"""

# ============================================================

# Conceptual Memory View

# ============================================================

"""
প্রথমে:

```
x
|
v
```

10
int

পরে:

```
x
|
v
```

"Hello"
str

অর্থাৎ একই variable name
ভিন্ন object-কে reference করতে পারে।
"""

# ============================================================

# Duck Typing Internally

# ============================================================

def show(obj):

```
obj.run()
```

"""
Conceptually Python যখন:

```
show(object)
```

execute করে,

তখন:

```
obj.run()
```

এর সময় runtime-এ Python object-এর
run attribute/method খুঁজে।

যদি run() পাওয়া যায়:

```
→ method call হবে
```

যদি না পাওয়া যায়:

```
→ AttributeError হবে
```

"""

# ============================================================

# Example

# ============================================================

class A:

```
def run(self):
    print("A is running")
```

class B:

```
def run(self):
    print("B is running")
```

show(A())
show(B())

# ============================================================

# Error Example

# ============================================================

class C:
pass

# show(C())

"""
Output:

AttributeError:
'C' object has no attribute 'run'
"""

# ============================================================

# Why Python Supports Duck Typing

# ============================================================

"""
Python-এর dynamic object model এবং runtime attribute lookup
Duck Typing-কে খুব natural করে তোলে।

মূল বৈশিষ্ট্য:

✔ Runtime behavior
✔ Dynamic typing
✔ Flexible interfaces
✔ Polymorphism
✔ No mandatory inheritance
✔ No strict class requirement
"""

# ============================================================

# Duck Typing vs Inheritance

# ============================================================

"""
Inheritance-based approach:

```
Animal
  |
  +---- Duck
  |
  +---- Dog
```

Duck Typing:

```
Duck ──────┐
           |
Dog  ──────┼──> sound()
           |
Person ────┘
```

এখানে Duck, Dog এবং Person-এর
common parent class থাকা জরুরি নয়।

শুধু required method থাকলেই হবে।
"""

# ============================================================

# Main Difference

# ============================================================

"""
Inheritance:

```
"তুমি কোন class থেকে এসেছে?"
```

Duck Typing:

```
"তুমি কী করতে পারো?"
```

Example:

Inheritance:
isinstance(obj, Animal)

Duck Typing:
obj.make_sound()
"""

# ============================================================

# Simple Analogy

# ============================================================

"""
Static/Strict approach:

```
"তোমার ID card দেখাও।
 তুমি Duck হলে তবেই ঢুকতে পারবে।"
```

Duck Typing:

```
"তুমি কি quack করতে পারো?
 পারলে ঢুকতে পারো।"
```

অর্থাৎ:

```
Type → Less important
Behavior → More important
```

"""

# ============================================================

# Final Summary

# ============================================================

"""
Python Duck Typing:

1. Object-এর exact type/class প্রধান বিষয় নয়।

2. Object কী behavior provide করে সেটি গুরুত্বপূর্ণ।

3. Required method/attribute থাকলে object ব্যবহার করা যায়।

4. সাধারণত explicit type checking দরকার হয় না।

5. Runtime-এ attribute/method lookup হয়।

6. Method না থাকলে AttributeError হতে পারে।

7. Duck Typing inheritance-এর ওপর নির্ভর করে না।

8. এটি Python-এর flexible এবং polymorphic programming style-এর
   একটি গুরুত্বপূর্ণ অংশ।

সহজভাবে মনে রাখুন:

```
Duck Typing =
"What can you do?"

Not:
"What type are you?"
```

"""

# ============================================================

# One-Line Definition

# ============================================================

"""
Duck Typing means:

"An object's suitability is determined by the methods and
behavior it provides rather than by its specific type or class."
"""
