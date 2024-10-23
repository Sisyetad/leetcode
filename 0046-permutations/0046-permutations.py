class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # Backtracking function
        def backtrack(start=0):
            # Base case: if we've created a valid permutation
            if start == len(nums):
                result.append(nums[:])  # Append a copy of nums
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the starting element
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recurse to generate permutations for the next index
                backtrack(start + 1)
                
                # Backtrack: undo the swap
                nums[start], nums[i] = nums[i], nums[start]
        
        # Start the backtracking process
        backtrack()
        return result
