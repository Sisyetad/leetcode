class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self,x):
        sum=0
        for i in str(x):
            sum += int(i)
        if x%sum==0:
            return sum
        else: 
            return -1
