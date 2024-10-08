class Solution:
    def removeDuplicates(self,nums):
        x=0
        n=len(nums)
        for i in range(n-1):
            if(nums[i]!=nums[i+1]):
                nums[x]=nums[i]
                x+=1
            else:
                continue
        nums[x]=nums[n-1]
        return x+1