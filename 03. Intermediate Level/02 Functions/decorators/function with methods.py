# ============================= Function with Methods =============================

# Function with methods
# def check_user_name(method):
#     def wrapper(self):
#         if self.name == "John":
#             return "Hey my name is same also " + method(self)
#         else:
#             return "You entered name is " + self.name + " " + method(self)
#     return wrapper

def check_user_name(method):
    def wrapper(*args, **kwargs):
        if args[0] == "John":
            return "Hey my name is same also " + method(*args, **kwargs)
        else:
            return "You entered name is " + " " + method(*args, **kwargs)
    return wrapper
class Printing:
    def __init__(self, name):
        self.name = name
        
    @check_user_name
    def display(self):
        return "Entered name is " + self.name + " is printing"
    
if __name__ == "__main__":
    p = Printing("John")
    print(p.display())