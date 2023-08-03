from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        l1_temp = l1
        while l1_temp.next:
            n1 = n1*10 + l1_temp.val
            l1_temp = l1_temp.next
        n1 = n1 = n1*10 + l1_temp.val
        
        n2 = 0
        l2_temp = l2
        while l2_temp.next:
            n2 = n2*10 + l2_temp.val
            l2_temp = l2_temp.next
        n2 = n2*10 + l2_temp.val

        res = str(n1+n2)
        print(res)
        l_res = ListNode(int(res[0]))
        if n1+n2 < 10:
            return l_res
        else:
            next_node = ListNode(int(res[1]))
            l_res.next = next_node
            if len(res) > 2:
                for d in res[2:]:
                    next_node.next = ListNode(d)
                    next_node = next_node.next
            return l_res

