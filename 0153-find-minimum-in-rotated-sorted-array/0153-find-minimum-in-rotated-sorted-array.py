class Solution:
    def findMin(self,nums):
        result = nums[0]
        left,right=0,len(nums)-1
        while left <= right:
            if nums[left]<nums[right]:
                result=min(result,nums[left])
                break
            m=(left + right)//2
            result=min(result,nums[m])
            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1
        return result