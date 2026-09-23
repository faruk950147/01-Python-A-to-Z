"""
    # Function with Methods in Python

    In Python, **functions and methods are both callable blocks of code**, but the main difference is **where they are defined and how they are called**.

    ## 1. Function

    A **function** is defined independently, outside a class.

    ```python
    def add(a, b):
        return a + b

    result = add(10, 20)

    print(result)
    ```

    Output:

    ```text
    30
    ```

    Here:

    ```python
    add(10, 20)
    ```

    is a **function call**.

    ---

    ## 2. Method

    A **method** is a function that is defined **inside a class** and is usually called through an object or class.

    ```python
    class Calculator:

        def add(self, a, b):
            return a + b


    calc = Calculator()

    result = calc.add(10, 20)

    print(result)
    ```

    Output:

    ```text
    30
    ```

    Here:

    ```python
    calc.add(10, 20)
    ```

    is a **method call**.

    The `add()` function is considered a method because it is defined inside the `Calculator` class.

    ---

    ## Function vs Method

    | Function                                | Method                                 |
    | --------------------------------------- | -------------------------------------- |
    | Defined outside a class                 | Defined inside a class                 |
    | Called directly                         | Usually called through an object/class |
    | `add(10, 20)`                           | `calc.add(10, 20)`                     |
    | Doesn't automatically receive an object | Instance method receives `self`        |
    | Used for general-purpose operations     | Usually works with class/object data   |

    ---

    ## Simple Structure

    ### Function

    ```python
    def function():
        pass

    function()
    ```

    ### Method

    ```python
    class MyClass:

        def method(self):
            pass


    obj = MyClass()
    obj.method()
    ```

    ---

    ## Important Concept

    You can think of it like this:

    ```text
    Function
    ↓
    Independent block of code
    ```

    ```text
    Method
    ↓
    Function + Class/Object relationship
    ```

    For example:

    ```python
    class Student:

        def show_name(self):
            print(self.name)


    student = Student()
    student.name = "Faruk"

    student.show_name()
    ```

    Here `show_name()` is a **method**, and `self` refers to the current `student` object.

    ## In Short

    > **Every method is a function defined in a class, but not every function is a method.**

"""