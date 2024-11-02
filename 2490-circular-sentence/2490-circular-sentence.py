class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into words
        words = sentence.split()

        # Check each word in relation to the next word
        for i in range(len(words)):
            # The last character of the current word should match the first character of the next word
            if words[i][-1] != words[(i + 1) % len(words)][0]:
                return False

        # If all conditions are satisfied, the sentence is circular
        return True
