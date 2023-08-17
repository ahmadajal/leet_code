from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        list_len = 1
        last_element = head
        while last_element.next:
            last_element = last_element.next
            list_len += 1
        new_k = k % list_len
        # circular liked list
        last_element.next = head
        temp = last_element
        answer = head
        for i in range(list_len - new_k):
            temp = temp.next
            answer = answer.next
        temp.next = None
        return answer