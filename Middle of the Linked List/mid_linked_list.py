from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        curr = head
        odd = True
        while curr.next:
            curr = curr.next
            if odd:
                mid = mid.next
            odd = not odd
        return mid