class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')  # Initialize with negative infinity
        for num in nums:
            # Skip if the number is already a top three candidate
            if num in [first, second, third]:
                continue

            if num > first:
                third, second, first = second, first, num
            elif num > second:
                third, second = second, num
            elif num > third:
                third = num
    
            # If third is still negative infinity, it means there are less than 3 distinct numbers
        return third if third != float('-inf') else first

    