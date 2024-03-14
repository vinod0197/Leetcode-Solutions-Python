from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Create an empty hashmap to store indices
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement needed to reach target
            # Check if complement exists in the hashmap
            if complement in num_map:
                # If complement exists, return the indices of current number and its complement
                return [num_map[complement], i]
            # If complement doesn't exist, store the current number's index in the hashmap
            num_map[num] = i
        # If no solution is found, return an empty list
        return []
