import math

class MathOperations:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def mod(self, a, b):
        return a % b

    def pow(self, a, b):
        return a ** b

    def sqrt(self, a):
        return a ** 0.5

    def log(self, a):
        return math.log(a)


if __name__ == '__main__':
    math_op = MathOperations()
    print(math_op.add(10, 5))
    print(math_op.sub(10, 5))
    print(math_op.mul(10, 5))
    print(math_op.div(10, 5))
    print(math_op.mod(10, 5))
    print(math_op.pow(2, 3))
    print(math_op.sqrt(25))
    print(math_op.log(10))
