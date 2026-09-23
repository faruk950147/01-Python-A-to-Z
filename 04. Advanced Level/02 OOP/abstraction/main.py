from abc import ABC, abstractmethod


# ============================================================
# What is Abstraction?
# ============================================================

"""
Abstraction is the process of hiding implementation details
and showing only the necessary features to the user.

In Python, abstraction can be implemented using:
    1. ABC (Abstract Base Class)
    2. @abstractmethod

An abstract class:
    - Cannot normally be instantiated directly.
    - Can contain abstract methods.
    - Child classes must implement abstract methods.
"""


# ============================================================
# 1. Built-in Abstract Base Class (ABC)
# ============================================================

class Student(ABC):

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # Concrete method
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")

    # Abstract method
    @abstractmethod
    def calculate_result(self):
        """
        Child classes must implement this method.
        """
        pass


# ============================================================
# Concrete Class 1
# ============================================================

class CollegeStudent(Student):

    def __init__(self, name, roll, marks):
        super().__init__(name, roll)
        self.marks = marks

    # Implementing abstract method
    def calculate_result(self):

        avg = sum(self.marks) / len(self.marks)

        if avg >= 40:
            print(
                f"{self.name} passed with average: {avg:.2f}"
            )
        else:
            print(
                f"{self.name} failed with average: {avg:.2f}"
            )


# ============================================================
# Concrete Class 2
# ============================================================

class SchoolStudent(Student):

    def __init__(self, name, roll, grade):
        super().__init__(name, roll)
        self.grade = grade

    # Implementing abstract method
    def calculate_result(self):
        print(f"{self.name}'s grade is {self.grade}")


# ============================================================
# Object Creation
# ============================================================

c1 = CollegeStudent(
    "Faruk Ahmed",
    101,
    [80, 75, 90]
)

c1.show_details()
c1.calculate_result()


print("--------------")


s1 = SchoolStudent(
    "Rafi",
    55,
    "A+"
)

s1.show_details()
s1.calculate_result()


# ============================================================
# Abstract Class Cannot Be Instantiated
# ============================================================

# This will cause an error because Student
# contains an abstract method.

# student = Student("Tuhin", 303)

# TypeError:
# Can't instantiate abstract class Student
# with abstract method calculate_result


# ============================================================
# 2. Custom Abstract-Like Base Class
# ============================================================

class StudentCustom:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_info(self):
        print(
            f"Name: {self.name}, Roll: {self.roll}"
        )

    def calculate_result(self):
        raise NotImplementedError(
            "You must implement 'calculate_result()' "
            "in the subclass."
        )


# ============================================================
# Custom Subclass 1
# ============================================================

class CollegeStudentCustom(StudentCustom):

    def __init__(self, name, roll, marks):
        super().__init__(name, roll)
        self.marks = marks

    def calculate_result(self):

        avg = sum(self.marks) / len(self.marks)

        if avg >= 40:
            print(
                f"{self.name} Passed "
                f"(Average: {avg:.2f})"
            )
        else:
            print(
                f"{self.name} Failed "
                f"(Average: {avg:.2f})"
            )


# ============================================================
# Custom Subclass 2
# ============================================================

class SchoolStudentCustom(StudentCustom):

    def __init__(self, name, roll, grade):
        super().__init__(name, roll)
        self.grade = grade

    def calculate_result(self):
        print(
            f"{self.name}'s Grade: {self.grade}"
        )


# ============================================================
# Working Example
# ============================================================

c = CollegeStudentCustom(
    "Faruk Ahmed",
    101,
    [85, 78, 90]
)

c.show_info()
c.calculate_result()


print("--------------")


s = SchoolStudentCustom(
    "Rafi",
    202,
    "A+"
)

s.show_info()
s.calculate_result()


# ============================================================
# NotImplementedError Example
# ============================================================

# obj = StudentCustom("Tuhin", 303)
# obj.calculate_result()

# Output:
# NotImplementedError:
# You must implement 'calculate_result()'
# in the subclass.


# ============================================================
# 3. Abstraction Example with Car
# ============================================================

class Car(ABC):

    def __init__(self, name, color):

        self.name = name
        self.color = color

        self.speed = 0
        self.gear = 0
        self.is_started = False

    # --------------------------------------------------------
    # Abstract Methods
    # --------------------------------------------------------

    @abstractmethod
    def engine_start(self):
        pass

    @abstractmethod
    def engine_stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def change_gear(self, gear):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    # --------------------------------------------------------
    # Concrete Method
    # --------------------------------------------------------

    def current_speed(self):
        return self.speed


# ============================================================
# Concrete Class
# ============================================================

class Tesla(Car):

    def engine_start(self):

        if not self.is_started:

            self.is_started = True

            return (
                f"{self.name} engine started!"
            )

        else:

            return (
                f"{self.name} engine is already running!"
            )

    # --------------------------------------------------------

    def engine_stop(self):

        if self.is_started:

            self.is_started = False
            self.speed = 0

            return (
                f"{self.name} engine stopped!"
            )

        else:

            return (
                f"{self.name} engine is already stopped!"
            )

    # --------------------------------------------------------

    def drive(self):

        if self.is_started:

            return (
                f"{self.name} is driving at "
                f"speed {self.speed} km/h "
                f"in gear {self.gear}"
            )

        else:

            return (
                f"{self.name} cannot drive, "
                f"engine is off!"
            )

    # --------------------------------------------------------

    def change_gear(self, gear):

        if self.is_started:

            self.gear = gear

            return (
                f"{self.name} changed gear to {gear}"
            )

        else:

            return (
                f"{self.name} cannot change gear, "
                f"engine is off!"
            )

    # --------------------------------------------------------

    def accelerate(self):

        if self.is_started:

            if self.gear > 0:
                self.speed += 10 * self.gear
            else:
                self.speed += 5

            return (
                f"{self.name} accelerated to "
                f"{self.speed} km/h"
            )

        else:

            return (
                f"{self.name} cannot accelerate, "
                f"engine is off!"
            )

    # --------------------------------------------------------

    def brake(self):

        if self.speed > 0:

            self.speed -= 10

            if self.speed < 0:
                self.speed = 0

            return (
                f"{self.name} slowed down to "
                f"{self.speed} km/h"
            )

        else:

            return (
                f"{self.name} is already stopped!"
            )


# ============================================================
# Interactive Usage
# ============================================================

if __name__ == "__main__":

    my_car = Tesla(
        "Tesla Model S",
        "Red"
    )

    print(my_car.engine_start())

    print(my_car.change_gear(1))

    print(my_car.accelerate())

    print(my_car.accelerate())

    print(my_car.change_gear(2))

    print(my_car.accelerate())

    print(my_car.drive())

    print(my_car.brake())

    print(my_car.brake())

    print(my_car.engine_stop())