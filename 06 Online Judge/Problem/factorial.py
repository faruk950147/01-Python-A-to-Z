class Factorial:

    # efficient
    def factorial(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers"

        fact = 1

        for i in range(2, n + 1):
            fact *= i

        return fact


    # iterative
    def factorial_iterative(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers"

        fact = 1

        for i in range(1, n + 1):
            fact *= i

        return fact


    # recursive
    def factorial_recursive(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers"

        if n == 0 or n == 1:
            return 1

        return n * self.factorial_recursive(n - 1)


factorial = Factorial()


print(factorial.factorial(5))

print(factorial.factorial_iterative(5))

print(factorial.factorial_recursive(5))


n = int(input("Enter a number: "))

print(factorial.factorial(n))