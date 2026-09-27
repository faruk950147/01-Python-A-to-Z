class MenuDrivenProgram:
    def __init__(self):
        self.menu = {
            "1": "Addition",
            "2": "Subtraction",
            "3": "Multiplication",
            "4": "Division",
        }

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    def run(self):
        while True:
            print("\nMenu:")
            for key, value in self.menu.items():
                print(f"{key}. {value}")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = self.add(a, b)
                print(f"Result: {result}")
            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = self.subtract(a, b)
                print(f"Result: {result}")
            elif choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = self.multiply(a, b)
                print(f"Result: {result}")
            elif choice == "4":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = self.divide(a, b)
                print(f"Result: {result}")
            else:
                print("Invalid choice. Please try again.")

            again = input("Do you want to perform another operation? (yes/no): ")
            if again.lower() != "yes":
                break

if __name__ == "__main__":
    program = MenuDrivenProgram()
    program.run()