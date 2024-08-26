
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        newNum = []
        subarray = nums[:k]
        subarray.sort()
        
        for i in range(len(nums)-k+1):
            ans = subarray[x-1]
            if ans < 0:
                newNum.append(ans)
            else:
                newNum.append(0)
            
            # Update the subarray by removing the first element and inserting the next element in sorted order
            remove_index = bisect_left(subarray, nums[i])
            subarray.pop(remove_index)
            if i+k < len(nums):
                insert_index = bisect_left(subarray, nums[i+k])
                subarray.insert(insert_index, nums[i+k])
        
        return newNum
