from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            # level order traverse
            curr_queue = deque()
            curr_queue.append(root)
            len_level = 1
            ans = []
            while curr_queue:
                l = []
                for i in range(len_level):
                    node = curr_queue.popleft()
                    if node:
                        curr_queue.append(node.left)
                        curr_queue.append(node.right)
                        l.append(node.val)
                len_level = len(curr_queue)
                if l:
                    ans.append(l[-1])

            return ans