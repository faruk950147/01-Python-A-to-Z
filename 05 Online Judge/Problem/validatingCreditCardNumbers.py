import re

# pat1 is a regular expression to match a valid credit card number pattern
# Starts with 4, 5, or 6, followed by 3 digits, then three groups of 4 digits (optional dashes in between)
pat1 = r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$'

# pat2 is a regular expression to match repeated digits (e.g., 1111, 2222, etc.)
# It checks for any digit that repeats 3 or more times in a row
pat2 = r'(\d)\1{3,}'

# n is the number of credit card numbers to validate
n = int(input())

# Loop through each credit card number input
for i in range(n):  
    # Input the credit card number
    nums = input().strip()

    # Remove any dashes from the input number
    check = re.sub(r'-', "", nums) 

    # num1 checks if the number matches the pat1 pattern (valid format)
    num1 = re.match(pat1, nums) is not None  

    # num2 checks if the number does not contain any digit repeated 3 or more times
    num2 = re.search(pat2, check) is None  

    # If both num1 and num2 are valid, print 'Valid', otherwise print 'Invalid'
    print('Valid' if all([num1, num2]) else 'Invalid')
    
def validate_credit_card_number(nums):
    check = re.sub(r'-', "", nums) 
    num1 = re.match(pat1, nums) is not None  
    num2 = re.search(pat2, check) is None  
    return 'Valid' if all([num1, num2]) else 'Invalid'

print(validate_credit_card_number("4123456789123456"))