from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        def create_inorder(root_node):
            if not root_node.left:
                inorder.append(root_node.val)
            else:
                create_inorder(root_node.left)
                inorder.append(root_node.val)
            if root_node.right:
                create_inorder(root_node.right)

        create_inorder(root)
        return inorder[k-1] 
        