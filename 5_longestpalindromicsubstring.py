class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        # Initialize a table to store whether substrings are palindromes
        dp = [[False] * n for _ in range(n)]
        # Initialize variables to track the longest palindrome substring
        max_length = 1
        start_index = 0
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start_index = i
                max_length = 2
        # Check for substrings of length greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        start_index = i
                        max_length = length
        return s[start_index:start_index + max_length]
# Example usage:
s = "babad"
solution = Solution()
print(solution.longestPalindrome(s))  # Output: "bab" or "aba"
