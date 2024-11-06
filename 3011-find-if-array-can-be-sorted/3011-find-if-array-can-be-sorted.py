class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pre_mx = float('-inf')
        i, n = 0, len(nums)
        
        while i < n:
            j = i + 1
            count_bits = bin(nums[i]).count('1')
            min_val = max_val = nums[i]
            
            while j < n and bin(nums[j]).count('1') == count_bits:
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                j += 1
                
            if pre_mx > min_val:
                return False
            pre_mx = max_val
            i = j
            
        return True
