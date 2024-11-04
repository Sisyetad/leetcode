class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        
        compressed = []
        count = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                # Add chunks of counts if count > 9
                while count > 9:
                    compressed.append("9" + word[i - 1])
                    count -= 9
                compressed.append(str(count) + word[i - 1])
                count = 1  # Reset count

        # Handle the last character sequence
        while count > 9:
            compressed.append("9" + word[-1])
            count -= 9
        compressed.append(str(count) + word[-1])

        return ''.join(compressed)
