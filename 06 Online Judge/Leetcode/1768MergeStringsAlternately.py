class Solution:

    def mergeAlternately(self, word1, word2):
        result = []

        max_length = max(len(word1), len(word2))

        for i in range(max_length):

            if i < len(word1):
                result.append(word1[i])

            if i < len(word2):
                result.append(word2[i])

        return ''.join(result)

    def merge_the_tools(self, string, k):

        for i in range(0, len(string), k):

            # k determines the chunk size and loop step.
            # string[i:i+k] extracts up to k characters.
            part = string[i:i+k]

            # Remove duplicate characters while preserving
            # the order of their first occurrence.
            print(''.join(sorted(set(part), key=part.index)))


if __name__ == '__main__':

    # Test locally
    sol = Solution()

    print(sol.mergeAlternately("abc", "pqr"))
    # Output: apbqcr

    sol.merge_the_tools("AABCAAADA", 3)
    # Output:
    # AB
    # CA
    # AD