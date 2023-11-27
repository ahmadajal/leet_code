# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num_good = 0

        def traverse(node, max_so_far):
            if not node:
                return None

            if node.val >= max_so_far:
                self.num_good += 1
            if node.left:
                traverse(node.left, max(max_so_far, node.left.val))
            else:
                traverse(node.left, max_so_far)

            if node.right:    
                traverse(node.right, max(max_so_far, node.right.val))
            else:
                traverse(node.right, max_so_far)
        
        traverse(root, root.val)
        
        return self.num_good

