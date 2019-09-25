class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        res = dummy = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                res.next = l2
                l2 = l2.next
            else:
                res.next = l1
                l1 = l1.next
            res = res.next
        res.next = l1 or l2
        return dummy.next