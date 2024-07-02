class Solution:
    def search(self, nums, target):
        left,right = 0,len(nums)-1
        while left <= right:
            m = (left + right)//2
            if target == nums[m]:
               return m
            elif nums[left] <= nums[m]:
                if target > nums[m] or target < nums[left]:
                   left = m + 1
                else:
                    right = m-1
            else:
                if target < nums[m] or target > nums[right]:
                       right = m-1
                else:
                    left = m+1
        return -1