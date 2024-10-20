class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around center
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        # Edge case: if the string is empty or has only one character
        if len(s) < 2:
            return s
        
        # Initialize the longest palindrome
        longest_palindrome = ""
        
        # Iterate through the string and expand around each character and each pair of characters
        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            odd_palindrome = expandAroundCenter(i, i)
            # Even-length palindromes (pair center)
            even_palindrome = expandAroundCenter(i, i + 1)
            
            # Update the longest palindrome found
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
        
        return longest_palindrome
