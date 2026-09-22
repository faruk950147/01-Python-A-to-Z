"""
    # Python Closure

    Closure হলো এমন একটি function যা তার বাইরের (enclosing) scope-এর
    variable-কে মনে রাখে, এমনকি outer function execution শেষ হয়ে গেলেও।

    Closure মূলত function-based concept।

    --------------------------------------------------
    # Simple Closure Example
    --------------------------------------------------

    def calculator(n):

        def add(x):
            return x + n   # n is remembered by the closure

        return add


    add5 = calculator(5)

    print(add5(10))  # 15

    # এখানে add() function তার enclosing scope-এর n = 5
    # মনে রাখছে।

    # তাই add() একটি closure।

    --------------------------------------------------
    # Closure কীভাবে কাজ করে?
    --------------------------------------------------

    calculator(5)
        |
        | creates
        v
        add()
        |
        | remembers
        v
        n = 5

    add5(10)
    |
    v
    10 + 5
    |
    v
    15

    --------------------------------------------------
    # Why is Closure different from Class?
    --------------------------------------------------

    Closure:
        function + enclosing scope-এর variable

    Class:
        object + attributes + methods

    দুটোতেই state রাখা যায়, কিন্তু state রাখার পদ্ধতি আলাদা।

    --------------------------------------------------
    # Class with Same Behaviour
    --------------------------------------------------

    class Calculator:

        def __init__(self, n):
            self.n = n

        def add(self, x):
            return x + self.n


    calc = Calculator(5)

    print(calc.add(10))  # 15

    # এখানে n object-এর attribute হিসেবে stored আছে।
    # এটি class-based state বা OOP approach।
    # এটি closure নয়।

    --------------------------------------------------
    # Key Difference
    --------------------------------------------------

    Closure
        -> function-based
        -> enclosing variable মনে রাখে
        -> আলাদা class/object তৈরি করতে হয় না
        -> সাধারণত ছোট ও focused behaviour-এর জন্য useful

    Class
        -> object-oriented
        -> state object-এর attribute-এ রাখে
        -> object তৈরি হয়
        -> multiple attributes এবং methods রাখা যায়

    --------------------------------------------------
    # Important Point
    --------------------------------------------------

    Closure এবং class একই ধরনের behaviour implement করতে পারে।

    যেমন:

    Closure:
        calculator(5) -> add5(10) -> 15

    Class:
        Calculator(5) -> calc.add(10) -> 15

    কিন্তু implementation mechanism আলাদা।

    --------------------------------------------------
    # Final Answer
    --------------------------------------------------

    Python Closure হলো function-based concept।

    একটি closure হলো এমন function যা তার enclosing
    scope-এর variable-কে remember করে।

    Class closure নয়; তবে class ব্যবহার করে closure-এর
    মতো একই ধরনের stateful behaviour তৈরি করা যায়।
"""
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_10 = outer_function(10)

print(add_10(5))            # Output: 15
print(add_10.__closure__)   # Check closure info
print(add_10.__closure__[0].cell_contents) # Check closure value details

# Class-based approach same behavior but not closure
class Calculator:
    def __init__(self, n):
        self.n = n
    def add(self, x):
        return x + self.n

calc = Calculator(5).add
print(calc(10))  # 15
print(calc.__closure__)   # Check closure (None for class-based)