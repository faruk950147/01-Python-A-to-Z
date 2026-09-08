class FindComplement:

    # efficient solution
    def find_complement(self, num):
        # first get num bit length
        bit_length = num.bit_length()

        # now get mask using bit_length
        mask = (1 << bit_length) - 1

        # now get complement using bitwise XOR
        return num ^ mask


    # less efficient solution or pythonic way
    def find_complement2(self, num):
        # convert binary string ('0b' remove)
        binary = bin(num)[2:]

        # using list comprehension complement create
        complement = ''.join(
            '1' if b == '0' else '0'
            for b in binary
        )

        # complement binary string to integer
        return int(complement, 2)


    # bad solution
    def find_complement3(self, num):
        binary = bin(num)[2:]
        complement = ''

        for b in binary:
            if b == '0':
                complement += '1'
            else:
                complement += '0'

        return int(complement, 2)


complement = FindComplement()

print(complement.find_complement(5))   # Output: 2

print(complement.find_complement2(5))  # Output: 2
print(complement.find_complement2(1))  # Output: 0
print(complement.find_complement2(10)) # Output: 5

print(complement.find_complement3(5))  # Output: 2