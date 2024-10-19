class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Function to invert a bit
        def invert(bit: str) -> str:
            return '1' if bit == '0' else '0'
        
        # Recursive function to find the k-th bit
        def findBit(n, k):
            # Base case
            if n == 1:
                return '0'
            
            length = (1 << n) - 1  # Length of S_n
            mid = (length // 2) + 1  # Middle index
            
            if k == mid:
                return '1'
            elif k < mid:
                return findBit(n - 1, k)
            else:
                return invert(findBit(n - 1, length - k + 1))
        
        return findBit(n, k)
