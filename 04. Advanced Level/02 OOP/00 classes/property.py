"""
# Python Property, Getter, Setter, and Deleter

## What is `property` in Python?

`property` is a built-in Python mechanism that allows a method to be accessed like an attribute.

It is commonly used to control how an attribute is:

* Read → **Getter**
* Modified → **Setter**
* Deleted → **Deleter**

Instead of calling methods like:

```python
employee.getSalary()
employee.setSalary(60000)
```

we can write:

```python
employee.salary
employee.salary = 60000
```

This makes the class interface cleaner while still allowing validation and controlled access.

---

# 1. Without Using `property`

Without `property`, we can calculate and store a value directly as an instance attribute.

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.percentage = self.marks / 500 * 100


if __name__ == "__main__":

    s = Student("Faruk", 400)

    print("Without using property:", s.percentage)
```

### Output

```text
Without using property: 80.0
```

Here:

```python
s.percentage
```

is a normal instance attribute.

If `marks` changes later:

```python
s.marks = 450
```

the previously calculated:

```python
s.percentage
```

does not automatically update.

---

# 2. Using `property`

A property allows us to make a method behave like an attribute.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary
```

Now we can write:

```python
e = Employee("Faruk", 50000)

print(e.salary)
```

instead of:

```python
e.salary()
```

The method:

```python
def salary(self):
```

is accessed like an attribute because of:

```python
@property
```

---

# 3. Why Is `salary` Used Multiple Times?

You may notice:

```python
@property
def salary(self):
    ...
```

and:

```python
@salary.setter
def salary(self, value):
    ...
```

and:

```python
@salary.deleter
def salary(self):
    ...
```

The same name is used because all three methods belong to the **same property**.

Think of `salary` as one property with three operations:

```text
salary
  │
  ├── Getter  → Read salary
  │
  ├── Setter  → Change salary
  │
  └── Deleter → Delete salary
```

So:

```python
@property
def salary(self):
```

creates the property.

Then:

```python
@salary.setter
def salary(self, value):
```

adds a setter to that existing property.

Finally:

```python
@salary.deleter
def salary(self):
```

adds a deleter.

---

# 4. Getter

A **getter** controls how a property is read.

It is created using:

```python
@property
```

### Example

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
```

Now:

```python
e = Employee(50000)

print(e.salary)
```

automatically calls:

```python
salary(self)
```

Conceptually:

```text
e.salary
   ↓
@property
   ↓
salary(self)
   ↓
return self._salary
```

---

# 5. Setter

A **setter** controls how a property is modified.

It is created using:

```python
@property_name.setter
```

Example:

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
```

Now:

```python
e = Employee(50000)

e.salary = 60000
```

automatically calls the setter.

Conceptually:

```text
e.salary = 60000
        ↓
@salary.setter
        ↓
salary(self, 60000)
        ↓
self._salary = 60000
```

---

# 6. Why Use a Setter?

The main advantage of a setter is **validation and controlled modification**.

Example:

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value < 0:
            raise ValueError("Salary cannot be negative!")

        self._salary = value
```

Now:

```python
e = Employee(50000)

e.salary = 60000

print(e.salary)
```

Output:

```text
60000
```

But:

```python
e.salary = -5000
```

raises:

```text
ValueError: Salary cannot be negative!
```

This allows us to protect the object's state through controlled assignment.

---

# 7. Deleter

A **deleter** controls what happens when a property is deleted.

It is created using:

```python
@property_name.deleter
```

Example:

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.deleter
    def salary(self):
        print("Deleting salary...")
        del self._salary
```

Now:

```python
e = Employee(50000)

del e.salary
```

automatically calls the deleter.

Conceptually:

```text
del e.salary
      ↓
@salary.deleter
      ↓
salary(self)
      ↓
del self._salary
```

---

# 8. Complete Property Example

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    # Getter
    @property
    def salary(self):
        if self._salary is None:
            return "Salary is not set!"

        return self._salary

    # Setter
    @salary.setter
    def salary(self, value):

        if value < 0:
            raise ValueError("Salary cannot be negative!")

        self._salary = value

    # Deleter
    @salary.deleter
    def salary(self):

        if hasattr(self, "_salary"):
            print("Deleting salary...")
            del self._salary


if __name__ == "__main__":

    e = Employee("Faruk", 50000)

    # Getter
    print("Using property:", e.salary)

    # Setter
    e.salary = 60000
    print("Using property:", e.salary)

    # Deleter
    del e.salary
```

### Output

```text
Using property: 50000
Using property: 60000
Deleting salary...
```

---

# 9. What Happens Internally?

When we write:

```python
e.salary
```

Python uses the property's getter.

```text
e.salary
   ↓
property getter
   ↓
salary(self)
   ↓
self._salary
```

When we write:

```python
e.salary = 60000
```

Python uses the setter.

```text
e.salary = 60000
        ↓
property setter
        ↓
salary(self, 60000)
        ↓
self._salary = 60000
```

When we write:

```python
del e.salary
```

Python uses the deleter.

```text
del e.salary
      ↓
property deleter
      ↓
salary(self)
      ↓
del self._salary
```

---

# 10. Getter, Setter, and Deleter Structure

The complete structure is:

```python
class Employee:

    @property
    def salary(self):
        # Getter
        return self._salary

    @salary.setter
    def salary(self, value):
        # Setter
        self._salary = value

    @salary.deleter
    def salary(self):
        # Deleter
        del self._salary
```

The three methods are associated with one property:

```text
              salary
                │
       ┌────────┼────────┐
       ↓        ↓        ↓
    Getter    Setter   Deleter
       │        │        │
    Read      Write    Delete
```

---

# 11. Why Use `_salary`?

You may see:

```python
self._salary
```

instead of:

```python
self.salary
```

The single underscore:

```python
_
```

is a **naming convention**.

It generally means:

> This attribute is intended for internal use and should not normally be accessed directly from outside the class.

It is important to understand that `_salary` is **not truly protected**.

Python does not prevent this:

```python
e._salary = 10000
```

So `_salary` is a convention, not a strict access-control mechanism.

---

# 12. Why Not Use `self.salary` Inside the Getter?

Consider:

```python
@property
def salary(self):
    return self._salary
```

This is correct.

We use `_salary` as the underlying storage attribute.

If we wrote:

```python
@property
def salary(self):
    return self.salary
```

the getter would call itself repeatedly, resulting in recursive calls.

Therefore, the common pattern is:

```text
Public property
     ↓
   salary
     ↓
Underlying attribute
     ↓
  _salary
```

---

# 13. Property vs Normal Attribute

### Normal Attribute

```python
class Employee:

    def __init__(self, salary):
        self.salary = salary
```

Access:

```python
e.salary
```

There is no automatic validation when assigning:

```python
e.salary = -5000
```

---

### Property

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value < 0:
            raise ValueError("Salary cannot be negative!")

        self._salary = value
```

Now:

```python
e.salary = -5000
```

can be controlled and rejected.

---

# 14. Property and Encapsulation

Properties are commonly used as part of **encapsulation**.

Without a property:

```python
e.salary = -5000
```

can directly modify the attribute.

With a property:

```python
e.salary = -5000
```

passes through the setter.

```text
Outside Code
     │
     ↓
e.salary = value
     │
     ↓
Property Setter
     │
     ↓
Validation
     │
     ↓
_salary
```

This allows the class to control how its data is changed.

---

# 15. Read-Only Property

A property can also be made read-only by defining only a getter.

```python
class Employee:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

Now:

```python
e = Employee("Faruk")

print(e.name)
```

works.

But:

```python
e.name = "John"
```

raises an `AttributeError` because no setter was defined.

So:

```text
Getter only
     ↓
Read-only property
```

---

# 16. Property with Computed Value

Properties are also useful for calculated values.

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    @property
    def percentage(self):
        return self.marks / 500 * 100
```

Now:

```python
s = Student(400)

print(s.percentage)
```

Output:

```text
80.0
```

Notice that `percentage` is calculated when accessed.

If:

```python
s.marks = 450
```

then:

```python
print(s.percentage)
```

returns:

```text
90.0
```

because the property calculates the value from the current `marks`.

---

# 17. Important Difference: Method vs Property

### Normal Method

```python
class Student:

    def percentage(self):
        return 80
```

Call it using:

```python
student.percentage()
```

### Property

```python
class Student:

    @property
    def percentage(self):
        return 80
```

Access it using:

```python
student.percentage
```

The property gives a method **attribute-like syntax**.

---

# 18. Property Does Not Mean "Binding a Method to an Object"

A common misunderstanding is:

```text
property = binding a method to an object
```

That is not the best way to describe it.

A property is a **descriptor** that controls attribute access.

For example:

```python
@property
def salary(self):
    return self._salary
```

creates a property object on the class.

When you access:

```python
e.salary
```

Python invokes the property's getter with `e` as the instance.

So the better mental model is:

```text
@property
    ↓
Creates a property descriptor
    ↓
Attribute access triggers getter/setter/deleter
```

---

# 19. Complete Mental Model

```text
Employee
   │
   ├── name
   │
   ├── _salary
   │
   └── salary property
          │
          ├── Getter
          │     ↓
          │   e.salary
          │
          ├── Setter
          │     ↓
          │   e.salary = value
          │
          └── Deleter
                ↓
              del e.salary
```

---

# 20. Quick Summary

| Feature           | Syntax              | Purpose                        |
| ----------------- | ------------------- | ------------------------------ |
| Getter            | `@property`         | Read a value                   |
| Setter            | `@salary.setter`    | Modify a value                 |
| Deleter           | `@salary.deleter`   | Delete a value                 |
| `_salary`         | Single underscore   | Internal-use naming convention |
| Property          | `e.salary`          | Attribute-like access          |
| Setter validation | `if ...: raise ...` | Control invalid values         |

## Final Memory Map

```text
@property
    ↓
Getter
    ↓
Read

@salary.setter
    ↓
Setter
    ↓
Write / Validate

@salary.deleter
    ↓
Deleter
    ↓
Delete
```

And the most important pattern is:

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary
```

Usage:

```python
e = Employee(50000)

print(e.salary)      # Getter

e.salary = 60000     # Setter

print(e.salary)      # Getter

del e.salary         # Deleter
```

"""