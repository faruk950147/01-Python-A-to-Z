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