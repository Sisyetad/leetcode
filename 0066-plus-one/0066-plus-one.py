class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = ""
        for i in digits:
            new+=str(i)
        n = int(new) + 1
        y = str(n)
        newstring = [int(i) for i in y]
        return newstring
