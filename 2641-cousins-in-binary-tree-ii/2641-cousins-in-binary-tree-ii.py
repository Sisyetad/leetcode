from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # BFS traversal
        queue = deque([root])
        root.val = 0  # The root's value will always be 0 (no cousins for root)
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            level_nodes = []
            
            # First pass: Calculate the total sum of the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                level_nodes.append(node)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Second pass: Update each node's value with cousin sum
            for node in level_nodes:
                sibling_sum = 0
                if node.left and node.right:  # Both children exist (siblings)
                    sibling_sum = node.left.val + node.right.val
                elif node.left:  # Only left child
                    sibling_sum = node.left.val
                elif node.right:  # Only right child
                    sibling_sum = node.right.val
                
                # Update children's values to level_sum - sibling_sum
                if node.left:
                    node.left.val = level_sum - sibling_sum
                if node.right:
                    node.right.val = level_sum - sibling_sum
        
        return root
