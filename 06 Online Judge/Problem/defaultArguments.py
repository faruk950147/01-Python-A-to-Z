class Vehicle:

    def __init__(self, brand="Toyota"):
        self.brand = brand

    def show(self):
        print("Brand:", self.brand)

if __name__ == '__main__':
    v1 = Vehicle()
    v1.show()