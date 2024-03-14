class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        # Create an empty list to store characters in each row
        rows = [''] * numRows
        # Initialize variables for tracking current row and direction
        current_row = 0
        direction = 1  # 1 for moving down, -1 for moving up
        # Iterate through the string
        for char in s:
            rows[current_row] += char
            # Update current_row and direction based on zigzag pattern
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction
        # Concatenate characters from each row
        return ''.join(rows)
# Example usage:
s = "PAYPALISHIRING"
numRows = 3
solution = Solution()
print(solution.convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"
