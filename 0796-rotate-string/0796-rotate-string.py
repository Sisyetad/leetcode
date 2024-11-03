class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if both strings are of the same length
        if len(s) != len(goal):
            return False
        # Check if goal is a substring of s + s
        return goal in s + s
