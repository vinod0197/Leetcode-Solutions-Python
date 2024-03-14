class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Remove leading whitespace
        s = s.lstrip()
        
        # Check if the string is empty
        if not s:
            return 0
        
        # Determine sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Convert digits into integer
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        
        # Apply sign
        result *= sign
        
        # Clamp the integer to the 32-bit signed integer range
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
