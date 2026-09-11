"""
    What does 6k mean?

    6k means a number that is a multiple of 6 — in other words, it can be divided by 6 with no remainder.

    Examples:

    k    6k    Calculation
    0    0     6 × 0 = 0
    1    6     6 × 1 = 6
    2    12    6 × 2 = 12
    3    18    6 × 3 = 18
    4    24    6 × 4 = 24
    5    30    6 × 5 = 30

    So,

    6k = 0, 6, 12, 18, 24, 30, 36, 42, 48 ...

    All are multiples of 6.


    What does 6k ± 1 mean?

    Now if you take those multiples of 6 and add or subtract 1, you get numbers just one less or one more than a multiple of 6.

    k    6k    6k - 1    6k + 1
    1    6     5         7
    2    12    11        13
    3    18    17        19
    4    24    23        25
    5    30    29        31

    Look — many of these are prime numbers:

    5, 7, 11, 13, 17, 19, 23, 29, 31

    But remember:

    Not every number of the form 6k ± 1 is prime.

    For example:

    25 = 6(4) + 1

    But 25 is not prime because:

    25 = 5 × 5


    Why is this important?

    Every integer can be written as one of these six forms:

    6k
    6k + 1
    6k + 2
    6k + 3
    6k + 4
    6k + 5

    But:

    6k       → divisible by 6
    6k + 2   → divisible by 2
    6k + 3   → divisible by 3
    6k + 4   → divisible by 2

    Therefore, numbers like:

    6k, 6k + 2, 6k + 3, 6k + 4

    are divisible by 2 or 3.

    The only forms that are not automatically divisible by 2 or 3 are:

    6k - 1
    6k + 1

    Because:

    6k - 1 = 6(k - 1) + 5

    So we can think of the possible prime positions as:

    6k - 1 and 6k + 1


    Therefore:

    Every prime number greater than 3 must be of the form:

    6k - 1 or 6k + 1

    Examples:

    5  = 6(1) - 1
    7  = 6(1) + 1
    11 = 6(2) - 1
    13 = 6(2) + 1
    17 = 6(3) - 1
    19 = 6(3) + 1
    23 = 6(4) - 1
    29 = 6(5) - 1
    31 = 6(5) + 1


    Why do we check only 6k ± 1 in the prime-checking algorithm?

    Suppose n is greater than 3.

    First, we check whether n is divisible by 2 or 3.

    If it is not divisible by 2 or 3, then any possible factor greater than 3 must be of the form:

    6k - 1 or 6k + 1

    So instead of checking:

    5, 6, 7, 8, 9, 10, 11, 12, 13 ...

    we can skip unnecessary numbers and check:

    5, 7, 11, 13, 17, 19, 23, 25, 29, 31 ...

    This makes the algorithm faster.


    Why do we check up to √n?

    Suppose:

    n = a × b

    If n has a factor, at least one of its factors must be less than or equal to √n.

    For example:

    91 = 7 × 13

    √91 ≈ 9.54

    The smaller factor is 7, which is less than √91.

    Therefore, we only need to check possible factors up to √n.


    Python Code

    def is_prime(n):
        if n <= 1:  # 1 and numbers below 1 are not prime
            return False

        elif n <= 3:  # 2 and 3 are prime numbers
            return True

        elif n % 2 == 0 or n % 3 == 0:
            # If n is divisible by 2 or 3, it is not prime
            return False

        else:
            # Check possible factors in the form of 6k ± 1
            for i in range(5, int(n ** 0.5) + 1, 6):

                # Check both 6k - 1 and 6k + 1
                if n % i == 0 or n % (i + 2) == 0:
                    return False

        return True


    if is_prime(7):
        print("Prime")
    else:
        print("Not Prime")


    How the loop works:

    for i in range(5, int(n ** 0.5) + 1, 6):

    The values of i are:

    5
    11
    17
    23
    29
    35
    ...

    And:

    i + 2 gives:

    7
    13
    19
    25
    31
    37
    ...

    Together we check:

    5, 7
    11, 13
    17, 19
    23, 25
    29, 31
    35, 37
    ...

    These are numbers of the form:

    6k - 1 and 6k + 1.


    Important:

    6k ± 1 does NOT mean that every 6k ± 1 number is prime.

    For example:

    25 = 6(4) + 1

    But:

    25 = 5 × 5

    Therefore, 25 is not prime.

    The rule only says:

    Every prime number greater than 3 must be of the form 6k - 1 or 6k + 1.


    Summary:

    k → any integer

    6k → multiples of 6

    6k ± 1 → one less or one more than a multiple of 6

    Numbers of the forms 6k, 6k + 2, 6k + 3, and 6k + 4 are divisible by 2 or 3.

    Every prime number greater than 3 is of the form:

    6k - 1 or 6k + 1

    The Python algorithm uses this fact to reduce the number of divisibility checks.
"""
class IsPrime:

    def Is_Prime_Sieve(self, n):
        if n <= 1:
            return False

        elif n <= 3:
            return True

        elif (n % 2) == 0 or (n % 3) == 0:
            return False

        else:
            i = 5

            while (i * i <= n):
                if (n % i) == 0 or (n % (i + 2)) == 0:
                    return False

                i += 6

        return True


    def Is_Prime_Sieve1(self, n):

        if n <= 1:  # 1 is not a prime number
            return False

        elif n <= 3:  # 2 and 3 are prime numbers
            return True

        elif (n % 2) == 0 or (n % 3) == 0:
            # if n is divisible by 2 or 3, it's not a prime number
            return False

        else:

            for i in range(5, int(n ** 0.5) + 1, 6):
                # check for factors in the form of 6k ± 1

                if (n % i) == 0 or (n % (i + 2)) == 0:
                    # if n is divisible by any of these,
                    # it's not a prime number
                    return False

        return True


# Create object
prime = IsPrime()

# Call method
if prime.Is_Prime_Sieve1(7):
    print("Prime")
else:
    print("Not Prime")
    
def sieve(n):
    is_prime = [True] * (n + 1)

    is_prime[0] = is_prime[1] = False

    p = 2

    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

        p += 1

    return [i for i in range(n + 1) if is_prime[i]]


print(sieve(30))

# Normal
class IsPrime:

    def is_prime(self, n):
        """Check if a number is prime"""

        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):

            if n % i == 0:
                return False

        return True


# --- Program Run ---

prime_checker = IsPrime()

num = int(input("Enter a number to check if it's prime: "))

if prime_checker.is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")