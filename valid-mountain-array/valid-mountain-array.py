class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        l,r=0,n-1
        if(n<3):
            return False
        for i in range(n-1):
            if(arr[i] >= arr[i+1]):
                l=i
                break
        for i in range(n-1,0,-1):
            if(arr[i]>=arr[i-1]):
                r=i
                break
        return l==r