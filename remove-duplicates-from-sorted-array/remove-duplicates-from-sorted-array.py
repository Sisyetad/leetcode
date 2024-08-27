class Solution:
    def removeDuplicates(self,nums) :
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        nums.clear()
        for i in dict:
                nums.append(i)
        return len(nums)