from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Stores the height of each node
        heights = {}
        # Stores the level of each node
        levels = {}
        # Dictionary to store the maximum heights at each level
        level_max_heights = defaultdict(list)
        
        def dfs(node, level):
            if not node:
                return -1
            
            # Recursively calculate the height of left and right children
            left_height = dfs(node.left, level + 1)
            right_height = dfs(node.right, level + 1)
            
            # Height of current node is max height of its children + 1
            height = max(left_height, right_height) + 1
            heights[node.val] = height
            levels[node.val] = level
            
            # Append height to the level's list
            level_max_heights[level].append(height)
            
            return height

        # Run DFS from the root to fill in heights and levels
        dfs(root, 0)

        # Precompute the two highest heights for each level
        level_max_two = {}
        for level, level_heights in level_max_heights.items():
            level_heights.sort(reverse=True)
            if len(level_heights) >= 2:
                level_max_two[level] = (level_heights[0], level_heights[1])
            else:
                level_max_two[level] = (level_heights[0], -1)

        # Prepare the result based on queries
        result = []
        for q in queries:
            level = levels[q]
            node_height = heights[q]

            # Check if this node's height is the highest at its level
            if node_height == level_max_two[level][0]:
                # If the node's height is the highest, use the second highest if it exists
                new_height = level + level_max_two[level][1]
            else:
                # If it's not the highest, keep the current max height for this level
                new_height = level + level_max_two[level][0]
            
            result.append(new_height)
        
        return result
