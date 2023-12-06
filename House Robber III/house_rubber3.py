from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if hasattr(root, 'max_val'):
            return root.max_val
        max_l = self.rob(root.left)
        max_r = self.rob(root.right)
        
        if root.right or root.left:
            sum_childs = max_l + max_r
            with_root = root.val
            if root.left:
                with_root += self.rob(root.left.left) + self.rob(root.left.right)  
            if root.right:
                with_root += self.rob(root.right.left) + self.rob(root.right.right)
            
            if with_root > sum_childs:
                root.max_val = with_root
                return with_root
            else:
                root.max_val = sum_childs
                return sum_childs
        else:
            root.max_val = root.val
            return root.val