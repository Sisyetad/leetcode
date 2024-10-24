# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case: if both trees are empty, they are equivalent
        if not root1 and not root2:
            return True
        # If only one of the trees is empty, they are not equivalent
        if not root1 or not root2:
            return False
        # If the values of the current nodes are different, they are not equivalent
        if root1.val != root2.val:
            return False
        
        # Check the two possible ways to match the subtrees:
        # 1. Without flip: left with left, right with right
        # 2. With flip: left with right, right with left
        return (
            (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or
            (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
        )
