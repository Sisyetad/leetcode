class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower=word.lower()
        upper=word.upper()
        mydict={}
        for i in word:
            if i in lower and i.upper() in word:
                if i in mydict:
                    mydict[i] += 1
                else:
                    mydict[i] = 1
            if i in upper and i.lower() in word:
                if i in mydict:
                    mydict[i] += 1
                else:
                    mydict[i] = 1
        return len(mydict)//2