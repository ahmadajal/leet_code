from queue import Queue
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []
        if not root:
            return sol
        else:
            curr_level = Queue(1024)
            next_level = Queue(1024)
            curr_level.put(root)
            sol.append([root.val])
            first = True
            while not curr_level.empty():
                node = curr_level.get()
                if node.left and node.right:
                    if first:
                        sol.append([node.left.val, node.right.val])
                        first = False
                    else:
                        sol[-1].append(node.left.val)
                        sol[-1].append(node.right.val)
                    next_level.put(node.left)
                    next_level.put(node.right)
                elif node.left and not node.right:
                    if first:
                        sol.append([node.left.val])
                        first = False
                    else:
                        sol[-1].append(node.left.val)
                    next_level.put(node.left)
                elif not node.left and node.right:
                    if first:
                        sol.append([node.right.val])
                        first = False
                    else:
                        sol[-1].append(node.right.val)
                    next_level.put(node.right)
                else:
                    pass
                if curr_level.empty():
                    curr_level = next_level
                    first = True
                    next_level = Queue(1024)
            return sol


