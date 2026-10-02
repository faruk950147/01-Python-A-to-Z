"""
# Association, Aggregation and Composition in Python

## 1. Introduction

In OOP, objects can have relationships with other objects.

The main relationships are:

```text
Association
Aggregation
Composition
Inheritance
```

The easiest way to remember them:

```text
Association  → USES / INTERACTS WITH
Aggregation  → HAS-A + Independent
Composition  → HAS-A + Strongly Owned
Inheritance  → IS-A
```

---

# Part 1: Association

## 2. What is Association?

**Association** is a general relationship between two objects.

It means one object **uses, communicates with, or interacts with** another object.

### Simple Definition

> Association means two objects are connected, but neither object necessarily owns the other.

Example:

```text
Teacher ───── Student
```

A teacher teaches a student.

Both can exist independently.

---

## 3. Simple Example

```python
class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} is teaching {student.name}")


class Student:
    def __init__(self, name):
        self.name = name


teacher = Teacher("John")
student = Student("David")

teacher.teach(student)
```

### Output

```text
John is teaching David
```

Here:

```text
Teacher ───── Student
```

The teacher interacts with the student.

So this is:

```text
Association
```

---

## 4. Why is it Association?

The objects are created separately:

```python
teacher = Teacher("John")
student = Student("David")
```

Then:

```python
teacher.teach(student)
```

The teacher uses the student object.

But:

```text
Teacher does not own Student
Student does not own Teacher
```

Both can exist independently.

Therefore:

```text
Association = Interaction
```

---

# 5. Real-Life Association Examples

```text
Doctor ───── Patient
```

Doctor treats Patient.

```text
Teacher ───── Student
```

Teacher teaches Student.

```text
Customer ───── Order
```

Customer places Order.

```text
Driver ───── Car
```

Driver drives Car.

The important idea is:

```text
A interacts with B
```

---

# Part 2: Aggregation

## 6. What is Aggregation?

**Aggregation** is a special type of relationship where one object **has** another object, but the other object can exist independently.

### Simple Definition

> Aggregation is a weak HAS-A relationship where the part can exist without the whole.

Example:

```text
Department ◇──── Teacher
```

Meaning:

```text
Department HAS-A Teacher
```

But:

```text
Teacher can exist without Department
```

---

# 7. Simple Aggregation Example

```python
class Teacher:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def show_teacher(self):
        print(
            f"{self.name} department has "
            f"teacher {self.teacher.name}"
        )


teacher = Teacher("John")

department = Department(
    "CSE",
    teacher
)

department.show_teacher()
```

### Output

```text
CSE department has teacher John
```

The teacher is created first:

```python
teacher = Teacher("John")
```

Then the teacher is given to the department:

```python
department = Department("CSE", teacher)
```

So:

```text
Department
     │
     └── Teacher
```

This can represent **Aggregation**.

---

# 8. Why is it Aggregation?

The teacher can exist without the department.

For example:

```python
teacher = Teacher("John")
```

The teacher already exists.

Then:

```python
department = Department("CSE", teacher)
```

The department simply keeps a reference to the teacher.

So:

```text
Department HAS-A Teacher
```

and:

```text
Teacher can exist independently
```

Therefore:

```text
Aggregation
```

---

# 9. Main Features of Aggregation

Aggregation usually has:

```text
1. HAS-A relationship
2. Whole-Part relationship
3. Independent part
4. Weak ownership
5. Part can have another reference
```

Example:

```text
Department ◇──── Teacher
```

Think:

> "I have you, but you can live without me."

---

# 10. Aggregation Example with Multiple Objects

```python
class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for player in self.players:
            print(player.name)


player1 = Player("John")
player2 = Player("David")
player3 = Player("Mike")

team = Team("Warriors")

team.add_player(player1)
team.add_player(player2)
team.add_player(player3)

team.show_players()
```

Conceptually:

```text
Team
 │
 ├── Player
 ├── Player
 └── Player
```

The players were created separately.

So this can represent:

```text
Aggregation
```

---

# Part 3: Composition

## 11. What is Composition?

**Composition** is a strong whole-part relationship.

One object contains another object as a strongly owned part, and the part's lifecycle is strongly connected to the whole according to the domain model.

### Simple Definition

> Composition means one object is made up of another object as a strongly owned part.

Example:

```text
House ◆──── Room
```

Think:

> "You are a strongly controlled part of me."

---

# 12. Simple Composition Example

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car = Car()

car.start()
```

### Output

```text
Engine started
```

Here:

```python
self.engine = Engine()
```

creates an engine object as part of the `Car` object.

Conceptually:

```text
Car
 └── Engine
```

This can represent **Composition** when the domain model treats the engine as a strongly owned part of that car.

---

# 13. Composition Example

```python
class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self):
        self.room = Room("Bedroom")

    def show_room(self):
        print(self.room.name)


house = House()

house.show_room()
```

### Output

```text
Bedroom
```

Here:

```text
House
 └── Room
```

The `House` creates and contains the `Room`.

If the domain model says that the room belongs exclusively to that house and its lifecycle depends on that house, this is **Composition**.

---

# 14. Aggregation vs Composition

This is the most important difference.

## Aggregation

```text
Department ◇──── Teacher
```

Teacher can exist independently.

```text
Department removed
       ↓
Teacher can still exist
```

---

## Composition

```text
House ◆──── Room
```

If the room is defined as a lifecycle-dependent part of that particular house:

```text
House removed
       ↓
Room no longer exists as a part of that house
```

So:

```text
Aggregation → Independent Part
Composition → Dependent Part
```

---

# 15. Very Important Python Rule

Do **not** think:

```text
Created outside = Aggregation
Created inside = Composition
```

This is too simple.

For example:

```python
class Car:
    def __init__(self, engine):
        self.engine = engine
```

The engine is created outside.

But this does not automatically mean UML aggregation.

And:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

The engine is created inside.

But this alone does not automatically prove UML composition.

The correct rule is:

> **The relationship depends on ownership and lifecycle semantics, not only on Python syntax.**

---

# Part 4: Association vs Aggregation vs Composition

## 16. Association

```text
Teacher ───── Student
```

Meaning:

```text
Teacher interacts with Student
```

No required ownership.

### Remember:

```text
Association = USES
```

---

## 17. Aggregation

```text
Department ◇──── Teacher
```

Meaning:

```text
Department HAS-A Teacher
```

Teacher can exist independently.

### Remember:

```text
Aggregation = HAS-A + Independent
```

---

## 18. Composition

```text
House ◆──── Room
```

Meaning:

```text
House strongly HAS-A Room
```

The part has a strong lifecycle dependency on the whole according to the domain model.

### Remember:

```text
Composition = HAS-A + Strong Ownership/Lifecycle
```

---

# 19. Main Comparison Table

| Relationship | Simple Meaning   | Ownership              | Part Independent? | Example            |
| ------------ | ---------------- | ---------------------- | ----------------- | ------------------ |
| Association  | Uses / Interacts | No required ownership  | Yes               | Teacher–Student    |
| Aggregation  | Weak HAS-A       | Weak                   | Yes               | Department–Teacher |
| Composition  | Strong HAS-A     | Strong                 | Generally no      | House–Room         |
| Inheritance  | IS-A             | Parent-child hierarchy | N/A               | Dog–Animal         |

---

# 20. UML Symbols

## Association

```text
Teacher ───── Student
```

Plain line.

---

## Aggregation

```text
Department ◇──── Teacher
```

Hollow diamond:

```text
◇
```

---

## Composition

```text
House ◆──── Room
```

Filled diamond:

```text
◆
```

The diamond is placed on the **whole/container side**.

---

# 21. Association vs Aggregation

### Association

```text
Doctor ───── Patient
```

Doctor treats Patient.

It is simply an interaction.

```text
Doctor interacts with Patient
```

### Aggregation

```text
Department ◇──── Teacher
```

Department has Teachers.

It is a whole-part relationship.

```text
Teacher can exist independently
```

Therefore:

```text
Association
    ↓
General relationship
```

while:

```text
Aggregation
    ↓
Whole-Part relationship
    ↓
Independent Part
```

---

# 22. Aggregation vs Composition

Both are **whole-part relationships**.

The main difference is the lifecycle relationship.

```text
Aggregation
    ↓
Weak relationship
    ↓
Part can exist independently
```

```text
Composition
    ↓
Strong relationship
    ↓
Part's lifecycle depends on Whole
```

Example:

```text
Aggregation:

Department ◇──── Teacher
```

```text
Composition:

House ◆──── Room
```

---

# 23. Composition vs Inheritance

These are completely different concepts.

## Composition

```text
HAS-A
```

Example:

```text
Car HAS-A Engine
```

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

---

## Inheritance

```text
IS-A
```

Example:

```text
Dog IS-A Animal
```

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass
```

So:

```text
Composition → HAS-A
Inheritance → IS-A
```

---

# 24. Why Use Composition?

Composition allows us to build a class using other objects.

For example:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

Now we can provide different engines.

```python
class PetrolEngine:
    def start(self):
        print("Petrol engine started")


class ElectricEngine:
    def start(self):
        print("Electric engine started")
```

Then:

```python
car1 = Car(PetrolEngine())
car2 = Car(ElectricEngine())

car1.start()
car2.start()
```

### Output

```text
Petrol engine started
Electric engine started
```

This makes the design more flexible.

---

# 25. Favor Composition Over Inheritance

A common OOP principle is:

> **Favor composition over inheritance.**

This does not mean composition is always better.

It means:

```text
Use inheritance
when there is a real IS-A relationship.

Use composition
when there is a HAS-A relationship
or when combining objects gives a better design.
```

Example:

```text
Dog IS-A Animal
```

Use inheritance.

```text
Car HAS-A Engine
```

Use composition.

---

# 26. Python Does Not Have Special Keywords

Python does not have:

```python
association
aggregation
composition
```

keywords.

These are **OOP and software design concepts**.

Python uses normal features such as:

```text
Classes
Objects
Attributes
References
Lists
Methods
Constructors
Inheritance
```

Example:

```python
self.teacher = teacher
```

This means the object has a reference to another object.

The relationship type depends on the intended design.

---

# 27. Important Point About Object Lifetime

Do not think Python automatically destroys child objects when the parent is deleted.

Example:

```python
engine = Engine()

car = Car(engine)

del car
```

The `engine` object can still exist because:

```python
engine
```

still refers to it.

Therefore, UML composition is about:

```text
Ownership
+
Lifecycle semantics
+
Domain design
```

not simply Python garbage collection.

---

# 28. Interview Questions

## Q1. What is Association?

### Answer

> **Association is a general relationship between two independent objects where they interact with, communicate with, or use each other without requiring ownership.**

Example:

```text
Teacher ───── Student
```

---

## Q2. What is Aggregation?

### Answer

> **Aggregation is a weak whole-part relationship where one object has another object, but the part can exist independently of the whole.**

Example:

```text
Department ◇──── Teacher
```

---

## Q3. What is Composition?

### Answer

> **Composition is a strong whole-part relationship where one object strongly owns another object as a part, and the part's lifecycle is strongly dependent on the whole according to the domain model.**

Example:

```text
House ◆──── Room
```

---

## Q4. Difference Between Association and Aggregation?

### Answer

> **Association is a general interaction between objects, while aggregation is a more specific whole-part relationship where the part can exist independently.**

```text
Association:
Doctor ───── Patient

Aggregation:
Department ◇──── Teacher
```

---

## Q5. Difference Between Aggregation and Composition?

### Answer

> **Aggregation has an independent part, while composition has a strong ownership and lifecycle dependency between the whole and the part.**

```text
Aggregation:
Department ◇──── Teacher

Composition:
House ◆──── Room
```

---

## Q6. What is HAS-A?

### Answer

HAS-A means one object contains, references, or uses another object.

Examples:

```text
Car HAS-A Engine
Computer HAS-A CPU
Department HAS-A Teacher
```

HAS-A relationships can be modeled as aggregation or composition depending on the design semantics.

---

## Q7. What is IS-A?

### Answer

IS-A represents inheritance.

Example:

```text
Dog IS-A Animal
```

Python:

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

---

# 29. Common Mistakes

### Mistake 1

```text
HAS-A = Always Composition
```

Wrong.

HAS-A can represent aggregation or composition depending on ownership and lifecycle.

---

### Mistake 2

```text
Created inside __init__ = Always Composition
```

Wrong.

Creation location alone does not determine the UML relationship.

---

### Mistake 3

```text
Passed into constructor = Always Aggregation
```

Wrong.

Passing an object is often just dependency injection.

---

### Mistake 4

Confusing:

```text
HAS-A
```

with:

```text
IS-A
```

Remember:

```text
Car HAS-A Engine
```

but:

```text
Dog IS-A Animal
```

---

# 30. Complete Comparison

```text
Association
    ↓
General Relationship
    ↓
USES / INTERACTS WITH
    ↓
Teacher ───── Student
```

```text
Aggregation
    ↓
Whole-Part Relationship
    ↓
Weak HAS-A
    ↓
Part is independent
    ↓
Department ◇──── Teacher
```

```text
Composition
    ↓
Whole-Part Relationship
    ↓
Strong HAS-A
    ↓
Part has strong lifecycle dependency
    ↓
House ◆──── Room
```

```text
Inheritance
    ↓
IS-A Relationship
    ↓
Dog ───── Animal
```

---

# 31. Easy Memory Trick

Remember these four sentences:

```text
Association:
"I interact with you."

Aggregation:
"I have you, but you can exist independently."

Composition:
"You are a strongly owned part of me."

Inheritance:
"I am a type of you."
```

---

# 32. Final Cheat Sheet

```text
┌───────────────────────────────────────┐
│         OOP RELATIONSHIPS             │
├───────────────────────────────────────┤
│                                       │
│ Association                           │
│ → USES / INTERACTS WITH               │
│ → Teacher ───── Student               │
│                                       │
│ Aggregation                           │
│ → WEAK HAS-A                          │
│ → Independent Part                    │
│ → Department ◇──── Teacher            │
│                                       │
│ Composition                           │
│ → STRONG HAS-A                        │
│ → Strong Lifecycle Dependency         │
│ → House ◆──── Room                   │
│                                       │
│ Inheritance                           │
│ → IS-A                                │
│ → Dog ───── Animal                    │
│                                       │
└───────────────────────────────────────┘
```

---

# 33. One-Line Summary

```text
Association  → Uses / Interacts
Aggregation  → Has + Independent
Composition  → Has + Strongly Owned
Inheritance  → Is-A
```

### The easiest way to remember:

> **Association = "I use you."**

> **Aggregation = "I have you, but you can live without me."**

> **Composition = "You are a strongly owned part of me."**

> **Inheritance = "I am a type of you."**



Association
    ↓
"I work with you / interact with you"
    ↓
Teacher ───── Student


Aggregation
    ↓
"I have you, but you can exist independently"
    ↓
Department ◇──── Teacher


Composition
    ↓
"You are a strongly owned part of me"
    ↓
House ◆──── Room
"""