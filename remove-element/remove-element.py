class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        n=len(nums)
        r=n-1
        for i in range(n):
            if(nums[l]==val):
                nums[l]=nums[r]
                r-=1
            else:
                l+=1
        return r+1