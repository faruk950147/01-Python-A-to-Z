# Method Overloading is a feature of object-oriented programming (OOP) 
# that allows a class to have multiple methods with the same name but different parameters different parameters
# (different number or type of arguments). 
# This enables a single method name to handle different types of data or different numbers of inputs.

# Method Overloading Example

# Method Overloading Example in Python
# Python does NOT support true method overloading like Java or C++
# We use default arguments or *args to achieve similar behavior

class Calculator:
    # Using default argument to handle 2 or 3 numbers
    def add(self, a, b, c=0):
        """
        Adds 2 or 3 numbers depending on how many are provided
        """
        return a + b + c

    # Alternatively, we can use *args to add any number of numbers
    def add_multiple(self, *args):
        """
        Adds any number of numbers
        """
        return sum(args)

if __name__ == "__main__":
    calc = Calculator()

    # Using default argument method
    print("Using default arguments:")
    print(calc.add(1, 2))       # Output: 3
    print(calc.add(1, 2, 3))    # Output: 6

    # Using *args method
    print("\nUsing *args method:")
    print(calc.add_multiple(1, 2))            # Output: 3
    print(calc.add_multiple(1, 2, 3, 4, 5))  # Output: 15

