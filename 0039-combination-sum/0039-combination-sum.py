class Solution(object):
   def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur[:])  # Use cur[:] to avoid reference issues
            return
        if i >= len(candidates) or total > target:
            return
        
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])  # Include the current candidate
        cur.pop()  # Backtrack
        dfs(i + 1, cur, total)  # Exclude the current candidate and move to the next

    dfs(0, [], 0)
    return res
