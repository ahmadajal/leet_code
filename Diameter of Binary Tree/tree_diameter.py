from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        def depth(node):
            if node:
                r_d = depth(node.right)
                l_d = depth(node.left)
                self.dia = max(self.dia, r_d+l_d)
                return max(r_d, l_d) + 1
            else:
                return 0
        _ = depth(root)

        return self.dia
        