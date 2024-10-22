from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1  # If the tree is empty, there's no valid sum

        # BFS: Use a queue to perform level-order traversal
        queue = deque([root])
        level_sums = []
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Store the sum of the current level
            level_sums.append(level_sum)
        
        # Sort the sums in descending order
        level_sums.sort(reverse=True)
        
        # Return the k-th largest sum if possible
        if k <= len(level_sums):
            return level_sums[k - 1]
        else:
            return -1  # If k is larger than the number of levels
