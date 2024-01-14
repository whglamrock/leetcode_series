from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        indexToNode = {}
        curr = head
        n = 0
        while curr:
            indexToNode[n] = curr
            curr = curr.next
            n += 1

        for i in range(n // 2):
            currBackNode = indexToNode[n - i - 1]
            backPrev, backNext = indexToNode[n - i - 2], currBackNode.next
            backPrev.next = backNext
            currBackNode.next = None

            currFwdNode = indexToNode[i]
            fwdNext = currFwdNode.next
            currFwdNode.next = currBackNode
            currBackNode.next = fwdNext
