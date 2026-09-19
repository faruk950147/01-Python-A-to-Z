# 1. Question: Reverse a String
# input "Sky is blue"
# output "blue is sky"

def reverseString1(str):
    #split return list 
    str = str.split(" ") 
    #reverse list ['blue', 'is', 'Sky']
    str = str[::-1]
    #join list 'blue is sky'
    return " ".join(str).lower()

print("reverseString1('Sky is blue'):", reverseString1("Sky is blue"))

def reverseString2(str):
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev += str[i]
    return rev  
print("Reversed:",reverseString2("blue"))
# output: eulb

# 2. Question: Count the Occurrences of Each Character in a String
# str1 = "a,a,a,b,b,c,c,c"
# output = {'a': 3, 'b': 2, 'c': 3}
def count_characters(s):
    count = {}

    for chr in s.split(","):
        # get the current count of the character, defaulting to 0 if it doesn't exist, and increment it by 1
        count[chr] = count.get(chr, 0) + 1 

    return count

str1 = "a,a,a,b,b,c,c,c"
print(count_characters(str1))

# output: {'a': 3, 'b': 2, 'c': 3}

# 3. Question: Find the Longest Common Prefix
# strs = ["flower", "flow", "flight"]
# output = "fl"
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            print(f'Prefix: {prefix}')
            if not prefix:
                return ""
    
    return prefix
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))


strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))

# output: fl
