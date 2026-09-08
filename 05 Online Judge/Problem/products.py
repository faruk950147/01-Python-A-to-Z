from collections import Counter

# Read the input string
company_name = input().strip()

# Count the frequency of each character
counter = Counter(company_name)

# Sort by frequency (in descending order) and then by character (in ascending order)
sorted_characters = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

# Print the top three most common characters along with their counts
for i in range(3):
    print(f"{sorted_characters[i][0]} {sorted_characters[i][1]}")
    
def top_three_characters(company_name):
    # Count the frequency of each character
    counter = Counter(company_name)
    
    # Sort by frequency (in descending order) and then by character (in ascending order)
    sorted_characters = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top three most common characters along with their counts
    for i in range(3):
        print(f"{sorted_characters[i][0]} {sorted_characters[i][1]}")

# Example usage
company_name = input().strip()
top_three_characters(company_name)

def top_three_characters(company_name):
    # char_count dictionary to store character frequencies
    char_count = {}
    
    # char_count dictionary to store character frequencies
    for char in company_name:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Sort the characters first by frequency (descending) and then by character (ascending)
    sorted_characters = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top three most common characters along with their counts
    for i in range(min(3, len(sorted_characters))):
        print(f"{sorted_characters[i][0]} {sorted_characters[i][1]}")

if __name__ == "__main__":
    # Example usage
    # Read the input string
    company_name = input().strip()
    top_three_characters(company_name)
