class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        r=n-1
        l=0
        while(l<=r):
            m=(r+l)//2
            if(nums[m]<target):
                l=m+1
            elif(nums[m]>target):
                r=m-1
            else:
                return m
        return l