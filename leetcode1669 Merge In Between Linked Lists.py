
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prevRemoval = None
        startOfRemoval = list1
        for i in range(a):
            prevRemoval = startOfRemoval
            startOfRemoval = startOfRemoval.next
        endOfRemoval = list1
        for i in range(b):
            endOfRemoval = endOfRemoval.next

        tailOf2 = list2
        while tailOf2.next:
            tailOf2 = tailOf2.next

        prevRemoval.next = list2
        tailOf2.next = endOfRemoval.next
        endOfRemoval.next = None
        return list1
