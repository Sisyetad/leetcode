class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = {key: 0 for key in range(max(nums)+1)}
        target_index=[]
        for i in nums:
            count[i]+=1
        k=0
        for i in count:
            for j in range(count[i]):
                nums[k]=i
                k+=1
        for i in range(len(nums)):
            if(nums[i] == target):
                target_index.append(i)
        print(nums)
        return target_index
            
            