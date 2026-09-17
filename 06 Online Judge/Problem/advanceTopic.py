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
def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for word in strs[1:]:
            if i >= len(word) or word[i] != char:
                return strs[0][:i]

    return strs[0]


strs = ["flower", "flow", "flight"]

print(longestCommonPrefix(strs))

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

# output: fl
