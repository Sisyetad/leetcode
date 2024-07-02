class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in range(len(nums)):
            result+=(i+1-nums[i])
        return result