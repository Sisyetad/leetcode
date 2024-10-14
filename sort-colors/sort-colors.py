class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts an array of numbers containing only 0, 1, and 2 in-place.
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) - 1
        
        while w <= b:
            if nums[w] == 0:
                # Swap nums[w] and nums[r] (move 0 to the left)
                nums[w], nums[r] = nums[r], nums[w]
                r += 1
                w += 1
            elif nums[w] == 1:
                # No swap needed, just move the white pointer
                w += 1
            else:  # nums[w] == 2
                # Swap nums[w] and nums[b] (move 2 to the right)
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
