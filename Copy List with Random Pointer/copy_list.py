from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp = head
        while temp:
            temp_next = temp.next
            temp.next = Node(x=temp.val, next=temp_next)
            temp = temp_next

        # start again
        old = head
        new = head.next
        temp = new
        while old:
            if old.random:
                temp.random = old.random.next
            else:
                temp.random = None
            old = old.next.next
            if temp.next:
                temp.next = temp.next.next
            else:
                temp.next = None
            temp = temp.next
        return new

        