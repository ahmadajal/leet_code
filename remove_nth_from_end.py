# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        node_to_remove = head
        prev_removed = None
        i = 1
        while temp.next:
            if i < n:
                temp = temp.next
                i += 1
            else:
                if node_to_remove:
                    prev_removed = node_to_remove
                    node_to_remove = node_to_remove.next
                else:
                    node_to_remove = head
                temp = temp.next
        if node_to_remove == head:
            return head.next
        else:
            prev_removed.next = node_to_remove.next
            return head


