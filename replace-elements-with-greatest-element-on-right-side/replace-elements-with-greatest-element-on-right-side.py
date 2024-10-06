class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        temp=arr[n-1]
        tem=arr[n-1]
        for i in range(n-2,-1,-1):
            temp=max(temp,tem)
            tem=arr[i]
            arr[i]=temp
        arr[n-1]=-1
        return arr