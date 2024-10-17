class Solution:
    def myAtoi(self, s: str) -> int:
        # Define the 32-bit signed integer limits
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        i = 0
        n = len(s)
        result = 0
        sign = 1

        # Step 1: Ignore leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for an optional sign (+ or -)
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Convert the following digits into an integer
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow and clamp if necessary
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        # Step 4: Apply the sign to the result and return
        return sign * result
