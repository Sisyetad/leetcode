class Solution:
    def buildArray(self, nums):
        x = len(nums)
        newarr = []
        for i in range(x):
            x = nums[nums[i]]
            newarr.append(x)
        return newarr
