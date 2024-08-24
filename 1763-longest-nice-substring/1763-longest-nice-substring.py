class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(substring):
            for char in substring:
                if char.lower() not in substring or char.upper() not in substring:
                    return False
            return True

        longest = ""
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > len(longest):
                    longest = substring

        return longest
