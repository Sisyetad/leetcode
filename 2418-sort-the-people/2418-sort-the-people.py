class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            min_i=i
            for j in range(i+1,len(heights)):
                if heights[min_i]<heights[j]:
                    min_i=j
            heights[i],heights[min_i]=heights[min_i],heights[i]
            names[i],names[min_i]=names[min_i],names[i]
        return names