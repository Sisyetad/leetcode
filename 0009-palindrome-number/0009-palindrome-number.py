class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: If x is negative or if x ends with 0 (except for 0 itself), it can't be a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        # Step 2: Reverse the second half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Step 3: Check if the first half is equal to the reversed second half
        # Also handle the case where the number has odd digits by dividing reversed_half by 10
        return x == reversed_half or x == reversed_half // 10
