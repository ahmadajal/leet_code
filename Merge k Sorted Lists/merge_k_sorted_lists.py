# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        print(lists)
        ans = ListNode(0)
        prev = ans
        while None in lists:
            lists.remove(None)
        while len(lists) > 0:
            temp = []
            for ll in lists:
                temp.append(ll.val)
            min_num = min(temp)
            min_ind = temp.index(min_num)
            # print(min_ind)
            prev.next = ListNode(min_num)
            prev = prev.next
            lists[min_ind] = lists[min_ind].next
            if None in lists:
                lists.remove(None)
        return ans.next

ll = ListNode(val=1, next=ListNode(4, next=ListNode(5)))
lists = []
lists.append(ll)
ll = ListNode(val=1, next=ListNode(3, next=ListNode(4)))
lists.append(ll)
s = Solution()
print(s.mergeKLists([lists]))
