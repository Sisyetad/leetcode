class Solution:
    def lengthOfLastWord(self,s):
        s = s.split()
        
        return len(s[-1])
