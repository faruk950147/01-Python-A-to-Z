class Armstrong:

    """
    A class for checking whether a number is an Armstrong number.

    An Armstrong number is a number where the sum of each digit
    raised to the power of the total number of digits is equal
    to the original number.
    """

    def is_armstrong(self, num):

        """
        Check if a number is an Armstrong number.

        Logic:
        - Store the original number.
        - Count the total number of digits.
        - Extract each digit one by one.
        - Raise each digit to the power of total digits.
        - Add all the results.
        - Compare the sum with the original number.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is an Armstrong number,
                  False otherwise.

        Example:

        n = 153

        Number of digits = 3

        Extract 3:
            3 ** 3 = 27

        Extract 5:
            5 ** 3 = 125

        Extract 1:
            1 ** 3 = 1

        Sum:
            27 + 125 + 1 = 153

        Therefore:
            153 is an Armstrong number.
            
            153 Armstrong Number — Math Wise

            Given:

            Number = 153

            Number of digits = 3


            Step 1:

            153 ÷ 10

            Quotient  = 15
            Remainder = 3

            Last digit = 3

            3³
            = 3 × 3 × 3
            = 27


            Step 2:

            15 ÷ 10

            Quotient  = 1
            Remainder = 5

            Last digit = 5

            5³
            = 5 × 5 × 5
            = 125


            Step 3:

            1 ÷ 10

            Quotient  = 0
            Remainder = 1

            Last digit = 1

            1³
            = 1 × 1 × 1
            = 1


            Final Calculation:

            3³ + 5³ + 1³

            = 27 + 125 + 1

            = 153


            Original Number = 153
            Calculated Number = 153

            153 = 153

            ∴ 153 is an Armstrong Number
            
        """

        original = num

        # Count the number of digits
        digits = len(str(num))

        total = 0

        while num > 0:

            # Get the last digit using the remainder of division
            digit = num % 10
            print(f'Extract: {digit}')

            # Add the digit raised to the power of the total number of digits
            total += digit ** digits

            # Keep the quotient the remainder (last digit) is discarded
            num //= 10
            print(f'Keep the quotient the remainder (last digit) is discarded: {num}')

        return original == total
    
    def is_armstrong1(self, num):
        original = num

        # Count digits
        digits = 0
        temp = num

        while temp:
            digits += 1
            temp //= 10

        # Calculate Armstrong sum
        total = 0
        temp = num

        while temp:
            digit = temp % 10
            total += digit ** digits
            temp //= 10

        return total == original


a = Armstrong()

print(a.is_armstrong(153))   # True
print(a.is_armstrong(123))   # False
print(a.is_armstrong(370))   # True
print(a.is_armstrong(9474))  # True

