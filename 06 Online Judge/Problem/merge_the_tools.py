def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        # k is int(k) and string[i:i+k] is string[i:i+k] divide string into k parts k is slcing step 
        # let k=3 
        # string = "I Love Python" AABCAAADA
        # output I L
        # ove
        # Py
        # tho
        # n
        part = string[i:i+k]
        print(''.join(sorted(set(part), key=part.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)