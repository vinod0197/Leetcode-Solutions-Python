class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Initialize the result
        reversed_x = 0
        
        # Determine if x is negative
        is_negative = x < 0
        if is_negative:
            x = -x
        
        # Reverse the digits
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for integer overflow
            if reversed_x > (INT_MAX - digit) // 10:
                return 0
            
            reversed_x = reversed_x * 10 + digit
        
        # Restore the sign if necessary
        if is_negative:
            reversed_x = -reversed_x
        
        return reversed_x
