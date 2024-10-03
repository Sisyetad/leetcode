class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x=0
        y=0
        for i in nums:
            if i==1:
                x+=1
            else:
                if(x>y):
                    y=x
                x=0
        return y if y > x else x