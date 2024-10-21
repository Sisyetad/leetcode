from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: if digits is empty, return an empty list
        if not digits:
            return []
        
        # Map of digit to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # Result to hold all possible combinations
        result = []
        
        # Helper function for backtracking
        def backtrack(index: int, current_combination: str):
            # If the current combination is the same length as the digits, add it to the result
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # For each letter, add it to the current combination and recurse for the next digit
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        # Start the backtracking process with the first digit
        backtrack(0, "")
        
        return result
