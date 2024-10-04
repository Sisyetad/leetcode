class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j=0
        n=len(arr)
        res=[0]*n
        for i in range(0,n):
            res[j]=arr[i]
            j+=1
            if(j==n):
                break
            if (arr[i]==0):
                j+=1
                if(j==n):
                    break
                res[j-1]=0


        for i in range(0,n):
            arr[i]=res[i]