"""
# Composition in Python

## 1. What is Composition?

**Composition** is an object-oriented programming concept where one class **contains an object of another class** as a part of its implementation.

It represents a strong **HAS-A relationship**.

### Simple Definition

> **Composition means creating an object of one class inside another class and using that object to provide functionality.**

### Example

A **Car HAS-A Engine**.

```text
Car
 └── Engine
```

Here, `Car` contains an `Engine` object.

---

# 2. Basic Example: Car HAS-A Engine

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


if __name__ == "__main__":
    car = Car()
    car.start()
```

### Output

```text
Engine started
```

### Explanation

```python
self.engine = Engine()
```

Here, an object of the `Engine` class is created inside the `Car` class.

Therefore:

```text
Car HAS-A Engine
```

The `Car` object uses the `Engine` object to perform the `start()` operation.

---

# 3. Another Example: Company HAS-A Employee

```python
class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display(self):
        print(
            f"ID: {self.employee_id}, "
            f"Name: {self.name}, "
            f"Salary: {self.salary}"
        )


class Company:
    def __init__(self, name):
        self.name = name

        # Composition:
        # Company contains an Employee object.
        self.employee = Employee(123, "John", 5000)

    def display(self):
        print(f"Company: {self.name}")

        # Using the Employee object
        self.employee.display()


if __name__ == "__main__":
    company = Company("ABC")
    company.display()
```

### Output

```text
Company: ABC
ID: 123, Name: John, Salary: 5000
```

### Relationship

```text
Company
   │
   └── Employee
```

So:

> **Company HAS-A Employee**

The important part is:

```python
self.employee = Employee(123, "John", 5000)
```

An `Employee` object is stored as an attribute of the `Company` object.

---

# 4. Simple Example with Class A and Class B

```python
class A:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


class B:
    def __init__(self, age):
        self.age = age

        # Composition:
        # B contains an object of A.
        self.a = A("John")

    def display(self):
        print(self.age)

        # Using the A object
        self.a.display()


if __name__ == "__main__":
    b = B(25)
    b.display()
```

### Output

```text
25
John
```

Here:

```python
self.a = A("John")
```

means that class `B` contains an object of class `A`.

Therefore:

```text
B HAS-A A
```

---

# 5. Composition = HAS-A Relationship

Composition represents a **HAS-A** relationship.

### Examples

```text
Car HAS-A Engine

Company HAS-A Employee

Computer HAS-A CPU

House HAS-A Room

Department HAS-A Employee
```

For example:

```python
class CPU:
    def process(self):
        print("Processing...")


class Computer:
    def __init__(self):
        self.cpu = CPU()

    def run(self):
        self.cpu.process()
```

Here:

```text
Computer HAS-A CPU
```

---

# 6. Composition vs Inheritance

Composition and inheritance are different ways of creating relationships between classes.

## Composition

Composition represents:

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

Inheritance represents:

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

Here, `Dog` inherits from `Animal`.

Therefore:

```text
Dog IS-A Animal
```

---

# 7. Composition vs Inheritance Example

### Inheritance

```python
class Engine:
    def start(self):
        print("Engine started")


class Car(Engine):
    pass
```

This says:

```text
Car IS-A Engine
```

That doesn't make sense conceptually because a car is **not** an engine.

---

### Composition

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
```

This says:

```text
Car HAS-A Engine
```

This relationship makes conceptual sense.

---

# 8. Why Use Composition?

Composition helps us build classes by **combining smaller, independent objects**.

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

Now we can provide different engine implementations.

```python
engine = Engine()
car = Car(engine)

car.start()
```

This makes the design more flexible.

---

# 9. Composition and Loose Coupling

Composition can help achieve **loose coupling**, especially when dependencies are passed into a class rather than created directly inside it.

For example:

```python
class PetrolEngine:
    def start(self):
        print("Petrol engine started")


class ElectricEngine:
    def start(self):
        print("Electric engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

Now the `Car` does not need to know exactly which type of engine it is using.

```python
petrol_car = Car(PetrolEngine())
petrol_car.start()

electric_car = Car(ElectricEngine())
electric_car.start()
```

### Output

```text
Petrol engine started
Electric engine started
```

This is a major advantage of composition.

---

# 10. Composition vs Inheritance — Interview Point

A common design principle is:

> **"Favor composition over inheritance."**

This does **not** mean that composition is always better than inheritance.

Instead, it means:

* Use **inheritance** when there is a genuine **IS-A** relationship.
* Use **composition** when there is a **HAS-A** relationship or when you want to combine behaviors flexibly.

### Inheritance

```text
IS-A
```

Example:

```text
Dog IS-A Animal
```

### Composition

```text
HAS-A
```

Example:

```text
Car HAS-A Engine
```

---

# 11. Key Differences

| Feature          | Composition             | Inheritance             |
| ---------------- | ----------------------- | ----------------------- |
| Relationship     | HAS-A                   | IS-A                    |
| Main idea        | Contains another object | Extends another class   |
| Coupling         | Often more flexible     | Generally tighter       |
| Reusability      | Through objects         | Through class hierarchy |
| Flexibility      | High                    | Comparatively lower     |
| Example          | Car HAS-A Engine        | Dog IS-A Animal         |
| Python mechanism | Object attribute        | Class inheritance       |

---

# 12. Important Interview Notes

### Composition

```text
Composition = HAS-A
```

Example:

```python
self.engine = Engine()
```

### Inheritance

```text
Inheritance = IS-A
```

Example:

```python
class Dog(Animal):
    pass
```

### Remember

```text
Car HAS-A Engine
        ↓
Composition


Dog IS-A Animal
        ↓
Inheritance
```

---

# 13. One-Line Interview Answer

If an interviewer asks:

**"What is composition in Python?"**

You can answer:

> **Composition is an OOP technique where a class contains an object of another class and uses that object to provide functionality. It represents a HAS-A relationship and can help create flexible and loosely coupled designs.**

---

# 14. Final Summary

```text
Composition
     ↓
HAS-A Relationship
     ↓
One class contains an object of another class
     ↓
Example: Car HAS-A Engine
     ↓
Usually provides flexible object-based design
```

### Most important points

```text
✔ Composition = HAS-A relationship
✔ One class contains an object of another class
✔ Example: Car HAS-A Engine
✔ It promotes object composition and reuse
✔ It can reduce coupling when dependencies are injected
✔ "Favor composition over inheritance" is a design guideline,
  not an absolute rule
✔ Inheritance = IS-A relationship
```

"""