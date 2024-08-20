class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def checkvowel(sub):
            count = 0
            vowels = "aeiou"
            for i in sub:
                if i in vowels:
                    count += 1
            return count
        
        count = 0
        max_count = 0
        vowels = "aeiou"
        
        # Calculate vowel count for the first window
        count = checkvowel(s[:k])
        max_count = count
        
        # Slide the window over the string
        for i in range(k, len(s)):
            # Remove the leftmost character and update the count
            if s[i - k] in vowels:
                count -= 1
            
            # Add the rightmost character and update the count
            if s[i] in vowels:
                count += 1
            
            # Update the maximum count
            max_count = max(max_count, count)
        
        return max_count
