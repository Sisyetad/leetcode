class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort the input to handle duplicates
        
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])  # Add a copy of the current permutation
                return
            
            for i in range(len(nums)):
                # Skip the used elements
                if used[i]:
                    continue
                # Skip duplicates: if the current number is the same as the previous one and
                # the previous one has not been used in this recursive path, skip it.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Mark the element as used
                used[i] = True
                # Recurse with the element added to the current path
                backtrack(path + [nums[i]], used)
                # Backtrack: mark the element as unused for further permutations
                used[i] = False
        
        # Initialize the used array and start backtracking
        used = [False] * len(nums)
        backtrack([], used)
        return result
