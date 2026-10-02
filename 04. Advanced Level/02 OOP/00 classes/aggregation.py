"""
# Aggregation in Python

## 1. What is Aggregation?

**Aggregation** is a type of **HAS-A relationship** between two classes where one class contains or references objects of another class, but the contained objects can **exist independently** of the container.

### Simple Definition

> **Aggregation is a weak whole-part relationship where one object has references to other objects, but those objects can exist independently.**

In simple words:

```text
Aggregation = HAS-A + Independent Existence
```

Example:

```text
Department ───── Teacher
```

A:

```text
Department HAS-A Teacher
```

But a teacher can exist even if the department is removed.

Therefore, this is **Aggregation**.

---

# 2. Simple Example

Consider:

```text
Department → Teacher
```

A department has teachers.

But teachers can exist independently from the department.

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
            f"{self.name} department has teacher "
            f"{self.teacher.name}"
        )


teacher = Teacher("John")

department = Department(
    "Computer Science",
    teacher
)

department.show_teacher()
```

### Output

```text
Computer Science department has teacher John
```

Here:

```python
teacher = Teacher("John")
```

The `Teacher` object is created **outside** the `Department`.

Then:

```python
department = Department(
    "Computer Science",
    teacher
)
```

The existing `Teacher` object is passed into the `Department`.

Therefore:

```text
Department
     │
     └──── Teacher
```

This represents **Aggregation**.

---

# 3. Why is this Aggregation?

Look carefully at:

```python
teacher = Teacher("John")
```

The teacher exists independently.

Then:

```python
department = Department(
    "Computer Science",
    teacher
)
```

The department receives an already existing teacher.

The department does not create the teacher internally:

```python
self.teacher = Teacher("John")
```

Instead:

```python
self.teacher = teacher
```

So the relationship is:

```text
Department HAS-A Teacher
```

but:

```text
Teacher can exist without Department
```

Therefore:

```text
Aggregation
```

---

# 4. Main Characteristics of Aggregation

Aggregation generally has these characteristics:

### 1. HAS-A relationship

Example:

```text
Department HAS-A Teacher
```

### 2. Whole-Part relationship

One object represents the whole, while another object represents a part.

```text
Department → Teacher
```

### 3. Independent existence

The part can exist without the whole.

```text
Teacher
   ↓
can exist independently
```

### 4. Weak ownership

The whole references the part, but does not strongly control its entire lifecycle.

### 5. Objects are usually created separately

For example:

```python
teacher = Teacher("John")
department = Department("CSE", teacher)
```

The `Teacher` already exists before the `Department` receives it.

---

# 5. Real-Life Example

Consider a:

```text
University → Professor
```

A university has professors.

```text
University
     │
     ├── Professor
     ├── Professor
     └── Professor
```

But a professor can exist independently of one particular university.

For example, a professor may:

* change universities
* work at another institution
* exist as an object independently

Therefore, this can be modeled as **Aggregation**.

```python
class Professor:
    def __init__(self, name):
        self.name = name


class University:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def show_professors(self):
        for professor in self.professors:
            print(professor.name)


professor1 = Professor("John")
professor2 = Professor("David")

university = University(
    "ABC University"
)

university.add_professor(professor1)
university.add_professor(professor2)

university.show_professors()
```

### Output

```text
John
David
```

The important point is:

```python
professor1 = Professor("John")
professor2 = Professor("David")
```

The professors are created independently.

Then:

```python
university.add_professor(professor1)
university.add_professor(professor2)
```

The university simply references them.

---

# 6. Aggregation Does Not Mean Strong Ownership

This is one of the most important concepts.

Consider:

```python
professor = Professor("John")
university = University("ABC University")

university.add_professor(professor)
```

The university has a reference to the professor.

But the professor is not necessarily owned exclusively by the university.

For example:

```python
another_university = University("XYZ University")

another_university.add_professor(professor)
```

The same professor object can potentially be referenced elsewhere.

Conceptually:

```text
             ┌── University A
             │
Professor ───┤
             │
             └── University B
```

This illustrates the idea of **shared/independent existence**.

---

# 7. Aggregation with Multiple Objects

Aggregation can involve multiple parts.

Example:

```text
Team
 │
 ├── Player
 ├── Player
 ├── Player
 └── Player
```

A team has players.

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

Here:

```text
Team
 │
 ├── Player
 ├── Player
 └── Player
```

The players are created separately.

Therefore, this can represent **Aggregation**.

---

# 8. Aggregation vs Association

These two concepts are closely related.

## Association

Association means:

```text
A interacts with B
```

Example:

```text
Doctor ───── Patient
```

```python
doctor.treat(patient)
```

The doctor interacts with the patient.

There is no required whole-part relationship.

---

## Aggregation

Aggregation means:

```text
A HAS-A B
```

Example:

```text
Department ───── Teacher
```

The department contains/references teachers as parts of its organizational structure.

So:

```text
Association
    ↓
General relationship
```

while:

```text
Aggregation
    ↓
Whole-Part / HAS-A relationship
    ↓
Independent existence
```

---

# 9. Aggregation vs Composition

This is extremely important.

Both represent a **HAS-A / whole-part** relationship, but their lifecycle semantics differ.

## Aggregation

```text
Department
     │
     └──── Teacher
```

Teacher can exist independently.

```text
Department deleted
        ↓
Teacher can still exist
```

Therefore:

```text
Aggregation
```

---

## Composition

Consider:

```text
House
  │
  ├── Room
  ├── Room
  └── Room
```

If the domain model says that those rooms are inseparable parts of that particular house and their lifecycle is controlled by the house, this is **Composition**.

Conceptually:

```text
House
  │
  └──── Room
```

If the house is destroyed:

```text
House destroyed
       ↓
Its Rooms cease to exist
       ↓
Strong lifecycle dependency
```

Therefore:

```text
Composition
```

---

# 10. Important Difference

| Feature              | Aggregation          | Composition       |
| -------------------- | -------------------- | ----------------- |
| Relationship         | HAS-A                | Strong HAS-A      |
| Whole-Part           | Yes                  | Yes               |
| Ownership            | Weak/shared          | Strong            |
| Part independent?    | Generally yes        | Generally no      |
| Lifecycle dependency | Weak/no dependency   | Strong dependency |
| Example              | Department → Teacher | House → Room      |
| UML symbol           | Hollow diamond ◇     | Filled diamond ◆  |

Conceptually:

```text
Aggregation:

Department ◇──── Teacher
```

```text
Composition:

House ◆──── Room
```

---

# 11. Python Example: Aggregation

```python
class Engine:
    def __init__(self, model):
        self.model = model


class Car:
    def __init__(self, engine):
        self.engine = engine


engine = Engine("V8")

car = Car(engine)
```

Here the `Engine` is created separately:

```python
engine = Engine("V8")
```

Then passed into:

```python
car = Car(engine)
```

Depending on the intended domain semantics, this can represent aggregation because the `Car` receives an independently created object.

The important lesson is:

> **Python syntax alone does not determine whether a relationship is aggregation or composition. The intended lifecycle and ownership semantics matter.**

---

# 12. Python Example: Composition

Compare the previous example with:

```python
class Engine:
    def __init__(self, model):
        self.model = model


class Car:
    def __init__(self):
        self.engine = Engine("V8")
```

Here:

```python
car = Car()
```

creates the engine as part of constructing the car.

Conceptually:

```text
Car
 │
 └── Engine
```

This may represent **Composition** when the domain model intends the engine to be a strongly owned part of that car.

Again, simply creating an object inside `__init__` does not mathematically force UML composition; **lifecycle and ownership semantics are the important part**.

---

# 13. Very Important: Aggregation Is About Semantics

This is an important interview concept.

Consider:

```python
class Department:
    def __init__(self, teacher):
        self.teacher = teacher
```

Python itself does not have a special:

```python
aggregation
```

keyword.

Python only provides mechanisms such as:

* object references
* attributes
* lists
* constructors
* methods

Whether a relationship is considered:

```text
Association
Aggregation
Composition
```

depends on the **design semantics of the system**.

For example:

```python
self.teacher = teacher
```

only means:

> The `Department` object has a reference to a `Teacher` object.

The programmer/design determines what that relationship means.

---

# 14. Aggregation in UML

In UML, aggregation is represented using a **hollow diamond**.

```text
Department ◇──────── Teacher
```

The diamond is placed on the **whole/container side**.

For example:

```text
Department ◇──── Teacher
```

means:

```text
Department
    ↓
Whole

Teacher
    ↓
Part
```

Composition uses a filled diamond:

```text
House ◆──── Room
```

---

# 15. Association, Aggregation and Composition

Think about these three relationships:

### Association

```text
Teacher ───── Student
```

Meaning:

```text
Teacher interacts with Student
```

---

### Aggregation

```text
Department ◇──── Teacher
```

Meaning:

```text
Department HAS-A Teacher
```

but:

```text
Teacher can exist independently
```

---

### Composition

```text
House ◆──── Room
```

Meaning:

```text
House strongly contains Room
```

with lifecycle dependency.

---

# 16. Easy Way to Remember

Use this:

```text
Association
     ↓
USES
     ↓
Teacher ───── Student
```

```text
Aggregation
     ↓
HAS-A
     ↓
WEAK WHOLE-PART
     ↓
Department ◇──── Teacher
```

```text
Composition
     ↓
STRONG HAS-A
     ↓
STRONG WHOLE-PART
     ↓
House ◆──── Room
```

---

# 17. Real-Life Comparison

Let's use a company example.

## Association

```text
Manager ───── Employee
```

Manager communicates with employee.

```text
Interaction
```

---

## Aggregation

```text
Company ◇──── Employee
```

Company has employees, but employees can exist independently and may move to another company.

```text
Weak Whole-Part
```

---

## Composition

Consider:

```text
Company ◆──── Department
```

If the domain model defines a department as a lifecycle-dependent part of that specific company, then it can be modeled as composition.

```text
Strong Whole-Part
```

The exact relationship depends on the domain model.

---

# 18. Aggregation and Object Lifetime

Suppose:

```python
teacher = Teacher("John")

department = Department(
    "CSE",
    teacher
)
```

Now imagine the department object is deleted:

```python
del department
```

The `teacher` reference can still exist:

```python
print(teacher.name)
```

Output:

```text
John
```

This demonstrates the conceptual idea of independent existence.

---

# 19. Example with List

A common aggregation design is a class containing a collection of independently created objects.

```python
class Student:
    def __init__(self, name):
        self.name = name


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


student1 = Student("John")
student2 = Student("David")

classroom = Classroom()

classroom.add_student(student1)
classroom.add_student(student2)
```

Conceptually:

```text
Classroom
   │
   ├── Student 1
   └── Student 2
```

The students were created independently.

Therefore, this can represent an aggregation-style relationship.

---

# 20. Common Interview Question

### Q: What is Aggregation in Python?

A good answer:

> **Aggregation is a type of HAS-A relationship where one class contains or references objects of another class, but the contained objects can exist independently of the container. For example, a Department can have Teachers, while Teachers can exist independently of the Department.**

---

# 21. Another Interview Question

### Q: What is the difference between Aggregation and Composition?

Answer:

> **Both are whole-part relationships. In aggregation, the part can exist independently of the whole, while in composition, the part has a strong lifecycle dependency on the whole. For example, a Department and Teacher can represent aggregation, whereas a House and its Rooms may represent composition when the rooms' lifecycle is tied to that house.**

---

# 22. Another Interview Question

### Q: Is Aggregation a Python-specific feature?

No.

Aggregation is an **OOP/design concept**, not a special Python language feature.

Python does not have a keyword such as:

```python
aggregation
```

Instead, aggregation is implemented using normal object references.

Example:

```python
class Department:
    def __init__(self, teacher):
        self.teacher = teacher
```

The relationship is interpreted from the design semantics.

---

# 23. Aggregation vs Inheritance

Do not confuse these two.

## Aggregation

```text
Department ───── Teacher
```

Means:

```text
Department HAS-A Teacher
```

---

## Inheritance

```text
Dog ───── Animal
```

Means:

```text
Dog IS-A Animal
```

Example:

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

Therefore:

```text
Aggregation → HAS-A
Inheritance → IS-A
```

---

# 24. Four Important OOP Relationships

Remember:

```text
┌─────────────────────────────────────────┐
│             OOP RELATIONSHIPS           │
├─────────────────────────────────────────┤
│                                         │
│ Association                             │
│     ↓                                   │
│ USES / INTERACTS WITH                   │
│ Teacher ───── Student                   │
│                                         │
│ Aggregation                             │
│     ↓                                   │
│ WEAK HAS-A / WHOLE-PART                 │
│ Department ◇──── Teacher                │
│                                         │
│ Composition                             │
│     ↓                                   │
│ STRONG HAS-A / WHOLE-PART               │
│ House ◆──── Room                        │
│                                         │
│ Inheritance                             │
│     ↓                                   │
│ IS-A                                    │
│ Dog ───── Animal                        │
│                                         │
└─────────────────────────────────────────┘
```

---

# 25. Final Cheat Sheet

```text
Association
    ↓
General relationship
    ↓
A interacts with B
    ↓
Teacher ───── Student
```

```text
Aggregation
    ↓
HAS-A
    ↓
Weak Whole-Part
    ↓
Part can exist independently
    ↓
Department ◇──── Teacher
```

```text
Composition
    ↓
Strong HAS-A
    ↓
Strong Whole-Part
    ↓
Part's lifecycle is tied to Whole
    ↓
House ◆──── Room
```

```text
Inheritance
    ↓
IS-A
    ↓
Dog ───── Animal
```

## One Sentence to Remember

> **Aggregation = “I have you, but you can exist independently.”**

### The key formula

```text
Aggregation
    =
HAS-A
+
Whole-Part Relationship
+
Independent Part
```

And remember:

```text
Association  →  Uses
Aggregation  →  Has (independent)
Composition  →  Has (dependent)
Inheritance  →  Is-A
```

"""