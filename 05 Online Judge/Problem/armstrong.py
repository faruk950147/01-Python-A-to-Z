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
        """

        original = num

        # Count the number of digits
        digits = len(str(num))

        total = 0

        while num > 0:

            # Get the last digit
            digit = num % 10

            # Add digit raised to the power of total digits
            total = total + digit ** digits

            # Remove the last digit
            num //= 10

        return original == total


a = Armstrong()

print(a.is_armstrong(153))   # True
print(a.is_armstrong(123))   # False
print(a.is_armstrong(370))   # True
print(a.is_armstrong(9474))  # True

