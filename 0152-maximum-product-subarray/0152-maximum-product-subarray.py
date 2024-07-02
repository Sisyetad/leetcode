class Solution:
    def maxProduct(self, nums):
        product = nums[0]  # Initialize product with the first element
        Min, Max = 1, 1
        for n in nums:
            if n == 0:
                Min, Max = 1, 1
                product = max(product,0)
                continue
            tmp = Max * n
            Max = max(n * Max, n * Min, n)
            Min = min(tmp, n * Min, n)
            product = max(product, Max, Min)
        return product
