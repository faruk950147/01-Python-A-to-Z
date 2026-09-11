import re

# Read the input
rows, cols = map(int, input().split())  # Matrix dimensions
matrix = [input() for _ in range(rows)]  # Matrix rows

# Initialize an empty string for the decoded message
combined = ''
for j in range(cols):
    for i in range(rows):
        combined += matrix[i][j]  # Append character from matrix

# Replace all non-alphanumeric characters with a single space
# Alphanumeric characters are [A-Z, a-z, 0-9]
result = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', combined)

# Print the decoded message
print(result)


def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)