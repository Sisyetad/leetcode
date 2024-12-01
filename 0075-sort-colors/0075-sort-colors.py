class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count={0:0,1:0,2:0}        
        for j in nums:
            count[j]+=1
        k=0
        for i in range(3):
            for j in range(count[i]):
                nums[k]=i
                k+=1
        return nums