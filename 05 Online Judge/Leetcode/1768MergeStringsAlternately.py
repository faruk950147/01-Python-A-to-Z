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

# Test locally
sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))  # Output: apbqcr

