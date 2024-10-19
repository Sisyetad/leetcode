from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Find the maximum OR value possible
        max_or_value = 0
        for num in nums:
            max_or_value |= num  # Perform Bitwise OR with all elements
            
        # Step 2: Initialize a counter for subsets that match max OR
        self.count = 0
        
        # Step 3: Helper function to generate subsets and calculate OR value
        def backtrack(index, current_or):
            # If we've gone through all elements, check if we match max_or_value
            if index == len(nums):
                if current_or == max_or_value:
                    self.count += 1
                return
            
            # Include the current element in the subset
            backtrack(index + 1, current_or | nums[index])
            
            # Exclude the current element from the subset
            backtrack(index + 1, current_or)
        
        # Step 4: Start backtracking from the first element with OR value 0
        backtrack(0, 0)
        
        return self.count
