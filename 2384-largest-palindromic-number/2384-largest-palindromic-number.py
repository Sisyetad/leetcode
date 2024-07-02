class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        # Step 1: Count occurrences of each digit and initialize left and right halves
        digit_count = [0] * 10
        left = ''
        l = ''
        r = ''
        right = ''

        for digit in num:
            digit_count[int(digit)] += 1
    
        # Step 2: Construct left and right halves of the palindrome
        for digit in range(9, -1, -1):
            if digit != 0:
                add_count = digit_count[digit] // 2
                left += str(digit) * add_count
                right = (str(digit) * add_count) + right
            else:
                add_count = digit_count[digit] // 2
                if add_count > 0:
                    l += str(digit) * add_count
                    r = (str(digit) * add_count)
        
        # Step 3: Find the middle digit (if any)
        middle_digit = ''
        for digit in range(9, -1, -1):
            if digit_count[digit] % 2 == 1:
                middle_digit = str(digit)
                break
        
        # Step 4: Check if the input consists only of zeros
        if num.count('0') == len(num):
            return '0'
        if left=='':
            l=''
            r=''
        
        # Step 5: Return the concatenation of left, middle (if any), and right
        return left + l + middle_digit + r + right

# Test cases
sol = Solution()
print(sol.largestPalindromic("444947137"))  # Output: "7449447"
print(sol.largestPalindromic("0000"))      # Output: "0"
