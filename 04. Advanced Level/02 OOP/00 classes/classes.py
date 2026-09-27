
class Car  :
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        
    def display(self):
        print(self.name, self.model, self.color)

if __name__ == "__main__":
    c1 = Car("Toyota", "Corolla", "Red")
    c1.display()


class Car2(Car):
    def __init__(self, name, model, color, price):
        self.name = name
        self.model = model
        self.color = color
        self.price = price
        
    def __call__(self):
        print(self.name, self.model, self.color, self.price)
        
if __name__ == "__main__":
    c2 = Car2("Toyota", "Corolla", "Red", 20000)
    c2()

