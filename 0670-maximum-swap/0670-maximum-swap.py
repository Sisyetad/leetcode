class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number into a list of digits
        digits = list(str(num))
        
        # Create a dictionary to record the last position of each digit
        last_occurrence = {int(digit): i for i, digit in enumerate(digits)}
        
        # Iterate over the digits of the number
        for i, digit in enumerate(digits):
            # Try to find a larger digit to swap with, starting from 9 and going down
            for d in range(9, int(digit), -1):
                # If the larger digit exists later in the number, we swap
                if last_occurrence.get(d, -1) > i:
                    # Swap the current digit with the larger one
                    digits[i], digits[last_occurrence[d]] = digits[last_occurrence[d]], digits[i]
                    # After swapping, return the number as an integer
                    return int(''.join(digits))
        
        # If no swap was made, return the original number
        return num
