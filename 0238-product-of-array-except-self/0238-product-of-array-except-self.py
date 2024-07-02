class Solution:
    def productExceptSelf( self,nums):
        product=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            product[i]=prefix
            prefix*=nums[i]
        post=1
        for i in range(len(nums)-1,-1,-1):
            product[i]*=post
            post*=nums[i]
        return product