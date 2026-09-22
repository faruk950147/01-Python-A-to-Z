class Factorial:
    '''
        # Using +=
        def factList(n):
            factList = [1, 1]           # first two values
            if n <= 2:
                return factList[:n]     # if input is 2 or less
            fact = 2                    # 2! = 2
            for i in range(3, n + 1):   # from 3 to n
                fact *= i               # previous value * i
                factList += [fact]      # add to list
            return factList

        print(factList(5))

        # Using append
        def factList(n):
            factList = [1, 1]           # first two values
            if n <= 2:
                return factList[:n]     # if input is 2 or less
            fact = 2                    # 2! = 2
            for i in range(3, n + 1):   # from 3 to n
                # 2 → 2 * 3 = 6
                # 6 → 6 * 4 = 24
                # 24 → 24 * 5 = 120
                fact *= i               # previous value * i
                factList.append(fact)   # add to list
            return factList

        print(factList(10))

        def factList(n):
            factList = [1]
            if n == 0:
                return factList[:1]
            for i in range(1, n):
                # 1 → 1 * 2 = 2
                # 2 → 2 * 3 = 6
                # 6 → 6 * 4 = 24
                # 24 → 24 * 5 = 120
                factList += [factList[-1] * (i + 1)]
            return factList

        print(factList(10))

        def factList(n):
            factList = [1]  # 0! = 1
            if n == 0:
                return factList[:1]
            for i in range(1, n):  # from 1 to n
                factList.append(factList[-1] * (i + 1))  # last value * (i+1)
            return factList

        print(factList(10))

    '''
    
    # efficient
    def factorial(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers"

        fact = 1

        for i in range(2, n + 1):
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