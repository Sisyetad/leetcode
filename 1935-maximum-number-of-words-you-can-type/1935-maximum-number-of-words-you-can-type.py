class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)  # Convert the string of broken letters into a set
        words = text.split()  # Split the text into words
        count = 0
        
        for word in words:  # Iterate over each word
            if not any(char in brokenLetters for char in word):  # Check if any character in the word is broken
                count += 1  # Increment count if the word can be typed without broken letters
                
        return count
