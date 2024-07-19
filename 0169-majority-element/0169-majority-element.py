from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = None
        count = 0
        
        # Phase 1: Find a candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Phase 2: Verify the candidate
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        else:
            return None  # This line is generally not needed as problem guarantees majority element
