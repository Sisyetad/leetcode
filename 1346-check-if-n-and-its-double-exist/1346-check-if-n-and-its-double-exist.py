class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #using iteration over by using i(0-len(arr)) and j(i+1 to len(arr))
        #by using multiplication and div case for optimazation
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if(arr[i]== 2*arr[j] or 2*arr[i]==arr[j]):
                    return True
        return False