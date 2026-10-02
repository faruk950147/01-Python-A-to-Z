"""
# Association, Aggregation and Composition in Python

## 1. Introduction

In Object-Oriented Programming (OOP), objects can have relationships with other objects.

The main object relationships are:

```text
Association
Aggregation
Composition
Inheritance
```

The easiest way to remember them:

```text
Association  → USES / INTERACTS WITH
Aggregation  → HAS-A + Independent Part
Composition  → HAS-A + Strong Ownership
Inheritance  → IS-A
```

---

# Part 1: Association

## 2. What is Association?

**Association** is a general relationship between two objects.

It means one object can **use, communicate with, interact with, or work with** another object.

### Simple Definition

> **Association is a general relationship between two objects where they are connected or interact, without requiring one object to own the other.**

Example:

```text
Teacher ───── Student
```

A teacher teaches a student.

Both objects can exist independently.

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

The `Teacher` interacts with the `Student`.

Therefore, this is an example of:

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

The `Teacher` uses the `Student` object.

There is no required ownership:

```text
Teacher does not own Student
Student does not own Teacher
```

Both can exist independently.

Therefore:

```text
Association = General Interaction
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

Customer places an Order.

```text
Driver ───── Car
```

Driver drives Car.

The important idea is:

```text
A interacts with B
```

So:

```text
Association → USES / INTERACTS WITH
```

---

# Part 2: Aggregation

## 6. What is Aggregation?

**Aggregation** is a specialized form of association that represents a **whole-part relationship**.

The whole object has or groups one or more part objects, but the part has an **independent lifecycle** and is not exclusively owned by the whole.

### Simple Definition

> **Aggregation is a whole-part relationship where the part can exist independently of the whole.**

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

The hollow diamond `◇` is placed on the **whole side**.

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

The teacher is created separately:

```python
teacher = Teacher("John")
```

Then the teacher is associated with the department:

```python
department = Department("CSE", teacher)
```

Conceptually:

```text
Department ◇──── Teacher
```

This can represent **Aggregation** when the domain model treats the teacher as an independently existing part.

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

The department simply maintains a reference to the teacher.

Therefore:

```text
Department HAS-A Teacher
```

and:

```text
Teacher has an independent lifecycle
```

So the relationship can be modeled as:

```text
Aggregation
```

---

# 9. Main Features of Aggregation

Aggregation generally represents:

```text
1. Whole-Part relationship
2. HAS-A relationship
3. Independent part
4. No exclusive ownership
5. Part can exist without the whole
```

Example:

```text
Department ◇──── Teacher
```

Think:

> **"I have you, but you can exist without me."**

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
Team ◇──── Player
          Player
          Player
```

The players were created independently:

```python
player1 = Player("John")
player2 = Player("David")
player3 = Player("Mike")
```

Then they were added to the team.

If the domain model says the players can exist independently of the team, this represents:

```text
Aggregation
```

---

# Part 3: Composition

## 11. What is Composition?

**Composition** is a strong form of whole-part relationship.

The whole object **strongly owns** its parts, and the part's lifecycle is tied to the whole according to the domain model.

### Simple Definition

> **Composition is a whole-part relationship where the part is strongly owned by the whole and normally cannot meaningfully exist independently of that whole.**

Example:

```text
House ◆──── Room
```

The filled diamond `◆` is placed on the **whole side**.

Think:

> **"You are a strongly owned part of me."**

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

creates the `Engine` as part of the `Car`.

Conceptually:

```text
Car ◆──── Engine
```

This can represent **Composition** when the domain model treats that engine as a strongly owned part of that particular car.

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

Conceptually:

```text
House ◆──── Room
```

The `House` creates and contains the `Room`.

If the domain model defines the room as an exclusive, lifecycle-dependent part of that house, this is:

```text
Composition
```

---

# 14. Aggregation vs Composition

Both are:

```text
Whole-Part Relationships
```

The main difference is **ownership and lifecycle semantics**.

## Aggregation

```text
Department ◇──── Teacher
```

The teacher can exist independently.

Conceptually:

```text
Department removed
        ↓
Teacher can still exist
```

Therefore:

```text
Aggregation
→ Independent Part
→ No Exclusive Ownership
```

---

## Composition

```text
House ◆──── Room
```

If the room is modeled as a lifecycle-dependent part of that particular house:

```text
House removed
        ↓
Room no longer exists
as a part of that house
```

Therefore:

```text
Composition
→ Strong Ownership
→ Lifecycle Dependency
```

### Easy Difference

```text
Aggregation  → Independent Part
Composition  → Lifecycle-Dependent Part
```

---

# 15. Very Important Python Rule

Do NOT think:

```text
Created outside = Aggregation
Created inside = Composition
```

This is an oversimplification.

For example:

```python
class Car:
    def __init__(self, engine):
        self.engine = engine
```

The engine is created outside.

But this does **not automatically** mean UML aggregation.

Similarly:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

The engine is created inside.

But this alone does **not automatically prove** UML composition.

The correct principle is:

> **The relationship depends on ownership, lifecycle semantics, and the intended domain model—not merely on Python syntax.**

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

There is no required whole-part ownership.

Remember:

```text
Association = USES / INTERACTS WITH
```

---

# 17. Aggregation

```text
Department ◇──── Teacher
```

Meaning:

```text
Department HAS-A Teacher
```

The teacher has an independent lifecycle.

Remember:

```text
Aggregation = HAS-A + Independent Part
```

---

# 18. Composition

```text
House ◆──── Room
```

Meaning:

```text
House strongly HAS-A Room
```

The room's lifecycle is tied to the house according to the domain model.

Remember:

```text
Composition = HAS-A + Strong Ownership/Lifecycle
```

---

# 19. Main Comparison Table

| Relationship | Meaning           | Ownership                      | Part Independent? | UML Symbol     | Example            |
| ------------ | ----------------- | ------------------------------ | ----------------- | -------------- | ------------------ |
| Association  | Uses / Interacts  | No required ownership          | Usually yes       | `─────`        | Teacher–Student    |
| Aggregation  | Whole-Part        | No exclusive ownership         | Yes               | `◇────`        | Department–Teacher |
| Composition  | Strong Whole-Part | Strong ownership               | Normally no       | `◆────`        | House–Room         |
| Inheritance  | IS-A              | Parent-child type relationship | N/A               | Generalization | Dog–Animal         |

### Important

Aggregation and composition are both more specific forms of **whole-part relationships**.

Association is the broader/general relationship.

---

# 20. UML Symbols

## Association

```text
Teacher ───── Student
```

Plain line:

```text
─────
```

---

## Aggregation

```text
Department ◇──── Teacher
```

Hollow diamond:

```text
◇
```

The diamond is placed on the **whole side**.

---

## Composition

```text
House ◆──── Room
```

Filled diamond:

```text
◆
```

The diamond is placed on the **whole side**.

---

# 21. Association vs Aggregation

## Association

```text
Doctor ───── Patient
```

Doctor treats Patient.

It simply represents an interaction:

```text
Doctor interacts with Patient
```

---

## Aggregation

```text
Department ◇──── Teacher
```

Department has Teachers.

It represents a whole-part relationship:

```text
Department
    ↓
has Teacher
```

while the teacher can exist independently.

Therefore:

```text
Association
    ↓
General Relationship
```

and:

```text
Aggregation
    ↓
Whole-Part Relationship
    ↓
Independent Part
```

---

# 22. Aggregation vs Composition

Both represent:

```text
Whole-Part Relationship
```

But their ownership and lifecycle semantics differ.

```text
Aggregation
    ↓
Whole-Part
    ↓
No Exclusive Ownership
    ↓
Part is Independent
```

```text
Composition
    ↓
Whole-Part
    ↓
Strong Ownership
    ↓
Part's Lifecycle is Tied to Whole
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

These represent completely different concepts.

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

Therefore:

```text
Composition → HAS-A
Inheritance → IS-A
```

---

# 24. Why Use Composition?

Composition allows us to build a class using other objects.

For example:

```python
class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

Now different engine objects can be provided.

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

This design is flexible because `Car` depends on an engine interface/behavior rather than a single concrete engine implementation.

---

# 25. Favor Composition Over Inheritance

A common OOP design principle is:

> **Favor composition over inheritance.**

This does NOT mean composition is always better.

It means:

```text
Use inheritance
when there is a genuine IS-A relationship.
```

And:

```text
Use composition
when there is a HAS-A relationship
or when combining objects gives a more flexible design.
```

Example:

```text
Dog IS-A Animal
```

Inheritance can be appropriate.

```text
Car HAS-A Engine
```

Composition can be appropriate.

The important thing is to choose the relationship that matches the domain and design requirements.

---

# 26. Python Does Not Have Special Keywords

Python does not have special keywords such as:

```python
association
aggregation
composition
```

These are **OOP and software design concepts**.

Python uses normal language features such as:

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

For example:

```python
self.teacher = teacher
```

This creates an object reference.

Whether that reference represents:

```text
Association
Aggregation
Composition
```

depends on the intended design and semantics.

---

# 27. Important Point About Object Lifetime

Do not assume Python automatically destroys child objects when a parent object is deleted.

For example:

```python
engine = Engine()

car = Car(engine)

del car
```

If another reference still points to the engine:

```python
engine
```

then the `Engine` object can continue to exist.

Therefore:

```text
Python Object Lifetime
        ≠
UML Composition Semantics
```

UML composition describes a **design relationship** involving strong ownership and lifecycle semantics.

It is not simply a statement about Python garbage collection.

Therefore:

```text
Composition
    ↓
Ownership
+
Lifecycle Semantics
+
Domain Model
```

---

# Part 5: Interview Questions

## Q1. What is Association?

### Answer

> **Association is a general relationship between two objects where they interact with, communicate with, or use each other without requiring ownership.**

Example:

```text
Teacher ───── Student
```

---

## Q2. What is Aggregation?

### Answer

> **Aggregation is a whole-part relationship where the part has an independent lifecycle and is not exclusively owned by the whole.**

Example:

```text
Department ◇──── Teacher
```

---

## Q3. What is Composition?

### Answer

> **Composition is a strong whole-part relationship where the whole strongly owns the part and the part's lifecycle is tied to the whole according to the domain model.**

Example:

```text
House ◆──── Room
```

---

## Q4. Difference Between Association and Aggregation?

### Answer

> **Association is a general relationship between objects, while aggregation is a more specific whole-part relationship in which the part can exist independently of the whole.**

```text
Association:

Doctor ───── Patient
```

```text
Aggregation:

Department ◇──── Teacher
```

---

## Q5. Difference Between Aggregation and Composition?

### Answer

> **Aggregation represents a whole-part relationship with an independently existing part, while composition represents strong ownership where the part's lifecycle is tied to the whole.**

```text
Aggregation:

Department ◇──── Teacher
```

```text
Composition:

House ◆──── Room
```

---

## Q6. What is HAS-A?

### Answer

**HAS-A** describes a relationship where one object contains, references, or is made up of another object.

Examples:

```text
Car HAS-A Engine
Computer HAS-A CPU
Department HAS-A Teacher
```

A HAS-A relationship may represent different designs, including aggregation or composition, depending on ownership and lifecycle semantics.

---

## Q7. What is IS-A?

### Answer

**IS-A** represents an inheritance/generalization relationship.

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

# Part 6: Common Mistakes

## Mistake 1

```text
HAS-A = Always Composition
```

Wrong.

HAS-A can represent different designs.

For example:

```text
Aggregation → HAS-A + Independent Part
Composition → HAS-A + Strong Ownership
```

---

## Mistake 2

```text
Created inside __init__ = Always Composition
```

Wrong.

Creation location alone does not determine the UML relationship.

---

## Mistake 3

```text
Passed into constructor = Always Aggregation
```

Wrong.

Passing an object into a constructor is often simply:

```text
Dependency Injection
```

The UML relationship depends on the intended domain semantics.

---

## Mistake 4

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

## Mistake 5

Thinking:

```text
del parent
    ↓
Python automatically destroys all child objects
```

This is not generally correct.

Object lifetime depends on references and Python's memory-management mechanisms.

UML composition is a design concept, not simply a garbage-collection rule.

---

# 28. Complete Conceptual Comparison

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
HAS-A
    ↓
Independent Part
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
Strong Ownership
    ↓
Lifecycle Tied to Whole
    ↓
House ◆──── Room
```

```text
Inheritance
    ↓
IS-A Relationship
    ↓
Dog IS-A Animal
```

---

# 29. Easy Memory Trick

Remember these four sentences:

```text
Association:
"I interact with you."
```

```text
Aggregation:
"I have you, but you can exist independently."
```

```text
Composition:
"You are a strongly owned part of me."
```

```text
Inheritance:
"I am a type of you."
```

---

# 30. Final Cheat Sheet

```text
┌────────────────────────────────────────────┐
│             OOP RELATIONSHIPS              │
├────────────────────────────────────────────┤
│                                            │
│ Association                                │
│ → USES / INTERACTS WITH                    │
│ → General Relationship                     │
│ → Teacher ───── Student                    │
│                                            │
│ Aggregation                                │
│ → WHOLE-PART                               │
│ → HAS-A                                    │
│ → Independent Part                         │
│ → No Exclusive Ownership                   │
│ → Department ◇──── Teacher                 │
│                                            │
│ Composition                                │
│ → WHOLE-PART                               │
│ → Strong HAS-A                             │
│ → Strong Ownership                         │
│ → Lifecycle Tied to Whole                  │
│ → House ◆──── Room                         │
│                                            │
│ Inheritance                                │
│ → IS-A                                     │
│ → Generalization                           │
│ → Dog IS-A Animal                          │
│                                            │
└────────────────────────────────────────────┘
```

---

# 31. One-Line Summary

```text
Association  → Uses / Interacts
Aggregation  → Has + Independent Part
Composition  → Has + Strong Ownership/Lifecycle
Inheritance  → Is-A
```

### The easiest way to remember:

> **Association = "I interact with you."**

> **Aggregation = "I have you, but you can exist independently."**

> **Composition = "You are a strongly owned part of me."**

> **Inheritance = "I am a type of you."**

---

# 32. Final Mental Model

Think about the relationships in this order:

```text
                OOP Relationships
                       │
          ┌────────────┴────────────┐
          │                         │
      Object-to-Object          Type Relationship
          │                         │
     ┌────┴────┐                    │
     │         │                 Inheritance
     │         │                    │
Association  Whole-Part            IS-A
             │
        ┌────┴────┐
        │         │
   Aggregation  Composition
        │         │
 Independent   Strong Ownership
    Part       + Lifecycle
```

So the key distinction is:

```text
Association
    ↓
Do they interact?

Aggregation
    ↓
Is it a whole-part relationship
with an independent part?

Composition
    ↓
Is it a whole-part relationship
with strong ownership and lifecycle dependency?

Inheritance
    ↓
Is one class a specialized type of another?
```

This gives you the cleanest conceptual understanding of:

```text
Association
Aggregation
Composition
Inheritance
```
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