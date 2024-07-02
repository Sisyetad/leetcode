class Solution(object):
    def minSteps(self, s, t):
        # Initialize a dictionary to store the frequency of characters in both strings
        char_freq = {}

        # Count the frequency of characters in string s
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        # Count the frequency of characters in string t and subtract the counts from char_freq
        for char in t:
            if char in char_freq and char_freq[char] > 0:
                char_freq[char] -= 1
            else:
                # If char is not in char_freq or its count is already 0, it means we need to add a step
                # Because there is no corresponding character in s for this character in t
                # Alternatively, you can increment a variable to count the number of steps here
                pass

        # Sum up the remaining counts in char_freq dictionary, which represents the number of steps needed
        return sum(char_freq.values())

# Test the function with given inputs
s = "anagram"
t = "mangaar"
ob = Solution()
ob.minSteps(s, t)  # Output: 1
