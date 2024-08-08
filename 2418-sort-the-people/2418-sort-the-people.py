class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = {}
        ans =[]
        for i in range(len(names)):
            res[heights[i]] = names[i]
        sn = sorted(heights, reverse=True)
        for i in sn:
            x = res[i]
            ans.append(x)
        return ans
