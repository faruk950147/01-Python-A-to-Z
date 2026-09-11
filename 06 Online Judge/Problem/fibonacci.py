class Fibonacci:

    # efficient
    def fibonacci(self, n):
        if n <= 0:
            return 0

        a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b

        return a


    # recursive
    def fibonacci_recursive(self, n):
        if n <= 0:
            return 0

        elif n == 1:
            return 1

        else:
            return (
                self.fibonacci_recursive(n - 1)
                + self.fibonacci_recursive(n - 2)
            )


    # iterative with list
    def fibonacci_iterative(self, n):
        a, b = 0, 1

        sequence = []

        for _ in range(n):
            sequence.append(a)
            a, b = b, a + b

        return sequence


    # iterative without list
    def fibonacci_no_list(self, n):
        a, b = 0, 1

        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b


fibonacci = Fibonacci()


print(fibonacci.fibonacci(10))

print(fibonacci.fibonacci_recursive(10))

print(fibonacci.fibonacci_iterative(10))

fibonacci.fibonacci_no_list(10)