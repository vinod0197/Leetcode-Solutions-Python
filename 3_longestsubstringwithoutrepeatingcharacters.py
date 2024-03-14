class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Dictionary to store the index of the most recent occurrence of each character
        max_length = 0  # Variable to store the length of the longest substring
        start = 0  # Start index of the current substring
        
        # Iterate through the string
        for i, char in enumerate(s):
            # Update the start index of the current substring
            start = max(start, char_index.get(char, -1) + 1)
            
            # Update the index of the most recent occurrence of the current character
            char_index[char] = i
            
            # Update the length of the longest substring if needed
            max_length = max(max_length, i - start + 1)
        
        return max_length
