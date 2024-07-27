class Solution:
    def reverseVowels(self, s: str) -> str:
        v=set("aeiouAEIOU")
        i=0
        s = list(s)
        j=len(s)-1
        while i<j:
            if s[i] not in v:
                i+=1
            
            elif(s[j] not in v ):
                j-=1

            else:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i+=1
                j-=1
        return "".join(s)
