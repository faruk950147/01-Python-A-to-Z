# ============================= class-based decorator ========================
# 1. class Decorator:
class Decorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        print("Before call")
        self.func()
        print("After call")

@Decorator
def greet_class():
    print("Hello from function")
    
greet_class()

