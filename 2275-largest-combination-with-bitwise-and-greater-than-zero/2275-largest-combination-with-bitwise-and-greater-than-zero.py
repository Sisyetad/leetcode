class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_count = [0] * 32
        for num in candidates:
            for i in range(32):
                if num & (1 << i):
                    bit_count[i] += 1
        return max(bit_count)

    