# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, i1=0, 1
        n2, i2=0, 1
        while l1:
            n1 += l1.val * i1
            l1 = l1.next
            i1 = i1*10
        while l2:
            n2 += l2.val * i2
            l2 = l2.next
            i2 = i2*10
        res = n1+n2
        # print(n1,n2,res)
        l_res = ListNode(res%10)
        res = res // 10
        temp = l_res
        while res>0:
            temp.next = ListNode(res % 10)
            temp = temp.next
            res = res // 10
        return l_res

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
r = s.addTwoNumbers(l1,l2)
print(r.next.next.val)

