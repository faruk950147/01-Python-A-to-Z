# class instance, class method, static method
# class_instance = "self"
# class_method = "cls"
# static_method = "no parameter"

# 01 class instsance is a object of class and it is created by class constructor
# 02 class method is a method that is bound to the class and not the instance of the class
# 03 static method is a method that is bound to the class and not the instance of the class


class Human:
    def __init__(self, name):
        self.name = name
    
    def instance_method(self, message):
        return f"Instance method called with {self.name}: {message}"
    
    @classmethod
    def class_method(cls):
        return f"Class method called with {cls.__name__}"
    
    @staticmethod
    def static_method():
        return "Static method called"
    
if __name__ == "__main__":
    human = Human("John")
    print(human.instance_method("Hello"))
    print(Human.class_method())
    print(Human.static_method())