class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(n-k):
            window_sum = window_sum - nums[i] + nums[i+k]
            max_sum = max(window_sum , max_sum)
        output = (max_sum / k) * 1.00000
        return output
