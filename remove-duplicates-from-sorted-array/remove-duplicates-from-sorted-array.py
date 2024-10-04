class Solution:
    def removeDuplicates(self,nums) :
        x=0
        n=len(nums)
        for i in range(n):
            if(nums[x]==nums[i]):
                nums[x]=nums[i]
            else:
                x+=1
                nums[x]=nums[i]
        return x+1