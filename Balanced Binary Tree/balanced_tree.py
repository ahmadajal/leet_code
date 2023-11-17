import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        def traverse_balance(node):
            if node:
                isB_l, depth_l = traverse_balance(node.left)
                isB_r, depth_r = traverse_balance(node.right)
                if (isB_l and isB_r) and (math.fabs(depth_l - depth_r) <= 1):
                    return True, max(depth_l+1 , depth_r+1)
                else:
                    return False, max(depth_l+1 , depth_r+1)
            else:
                return True, 0
         
        ans, _ = traverse_balance(root)
        return ans