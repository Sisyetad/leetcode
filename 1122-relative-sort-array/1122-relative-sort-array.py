class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        temp = []
        for i in arr2:
            count[i]=0
        for i in arr1:
            if i in count:
                count[i]+=1
            else:
                temp.append(i)
        temp.sort()
        k=0
        for i in count:
            for j in range(count[i]):
                arr1[k]=i
                k+=1
        for i in temp:
            arr1[k]=i
            k+=1
        return arr1