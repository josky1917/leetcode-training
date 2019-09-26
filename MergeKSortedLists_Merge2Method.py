class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def mergeKLists(self, lists):
        num = len(lists)
        zero = ListNode(0)
        if not num:
            return zero.next
        segment = 1
        while segment<num:
            for i in range(0, num-segment, segment * 2):
                lists[i] = self.Merge2Lists(lists[i],lists[i+segment])
            segment *= 2
        return lists[0]
    def Merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next