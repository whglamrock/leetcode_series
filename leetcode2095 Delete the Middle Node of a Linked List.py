from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        nodeToDelete = head
        prev = None
        for i in range(size // 2):
            prev = nodeToDelete
            nodeToDelete = nodeToDelete.next

        if prev:
            prev.next = nodeToDelete.next
            nodeToDelete.next = None
            return head
        else:
            return None
