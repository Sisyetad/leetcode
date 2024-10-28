class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)  # Convert nums to a set for O(1) lookups
        longest_streak = 0
        
        for num in nums:
            current_num = num
            current_streak = 0
            
            # Keep finding squares in the set
            while current_num in num_set:
                current_streak += 1
                current_num = current_num ** 2  # Move to the next square
                
            longest_streak = max(longest_streak, current_streak)
        
        return longest_streak if longest_streak > 1 else -1
