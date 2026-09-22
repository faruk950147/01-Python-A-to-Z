# =============== Class Space =================
class Test:
    def __init__(self):
        self.num = 10

    def display(self):
        print(f"Class Scope: {dir(self)}")

# =============== Global Space =================
print(f"Global Scope: {dir()}")
test = Test()
test.display()
print(f"Global Scope: {dir()}")


# =============== Function Space =================
# print(f"Initial Scope: {dir()}")
# def test():
#     print(f"Function Scope: {dir()}")

# test()
# print(f"Initial Scope: {dir()}")


# =============== Global Space =================
print(f"Global Scope: {dir()}")

num = 10 # num is global variable

def test():
    num2 = 20 # num2 is local variable
    print(f"inside Function Scope: {dir()}")
    print(num2)
test()
print(f"outside Function Scope: {dir()}")

