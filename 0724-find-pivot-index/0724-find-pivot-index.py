class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        for i in range(len(nums)):
            r -=nums[i]
            if l == r:
                return i
            l +=nums[i]
        return -1
