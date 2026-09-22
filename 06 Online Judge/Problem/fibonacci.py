class Fibonacci:
    '''
        def fibList(n):
            fibList = [1, 1]           # first two values
            if n <= 2:
                return fibList[:n]     # if input is 2 or less
            fibPrev, fibCurr = 1, 1    # previous and current values
            for i in range(3, n + 1):  # from 3 to n
                # swap and calculate next
                # 1 → 1 + 1 = 2
                # 1 → 1 + 2 = 3
                # 2 → 2 + 3 = 5
                fibPrev, fibCurr = fibCurr, fibPrev + fibCurr
                fibList.append(fibCurr)   # add to list
            return fibList

            print(fibList(10))

        def fibList(n):
            fibList = [1, 1]
            if n <= 2:
                return fibList[:n]
            for i in range(2, n):
                # i starts from 2, so we can use fibList[-1] and fibList[-2]
                # fibList[-1] and fibList[-2] add
                # 1 → 1 + 1 = 2
                # 1 → 1 + 2 = 3
                # 2 → 2 + 3 = 5
                fibList += [fibList[-1] + fibList[-2]]
            return fibList

        print(fibList(10))


        # Using append
        def fibList(n):
            fibList = [1, 1]
            if n <= 2:
                return fibList[:n]
            for i in range(2, n):
                # fibList[-1] and fibList[-2] add
                # 1 → 1 + 1 = 2
                # 1 → 1 + 2 = 3
                # 2 → 2 + 3 = 5
                fibList.append(fibList[-1] + fibList[-2])
            return fibList

        print(fibList(10))
    '''
    
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