class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_xor = (1 << maximumBit) - 1  # max value with 'maximumBit' bits set to 1
        prefix = 0
        result = []
        
        for num in nums:
            # Compute XOR with max possible value and current prefix
            result.append(num ^ max_xor ^ prefix)
            prefix ^= num  # Update prefix XOR
        
        return result[::-1]  # Reverse the result to match the required order
