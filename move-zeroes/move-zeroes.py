class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        for i in nums:
       
        """
       # n=len(nums)
        #l=0
        #while(l<n):
          #  r=l+1
           # if(nums[l]==0):
             #   temp=nums[l]
              #  nums[l]=nums[r]
               # nums[r]=temp
            #else:
               # l+=1
                
        n = len(nums)
        last_non_zero_found_at = 0
        
        # Move all non-zero elements to the beginning of the array
        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1
        
        # Fill the remaining positions with zeros
        for i in range(last_non_zero_found_at, n):
            nums[i] = 0
            