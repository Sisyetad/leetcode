class Solution:
    def twoSum(self,nums,target):
        prevMap = {}
        for i, n in enumerate(nums):
            check = target - n
            if check in prevMap:
                return [prevMap[check],i]
            prevMap[n]=i
        return