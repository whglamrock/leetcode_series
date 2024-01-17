from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for i in range(n):
            fast = fast.next

        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        nodeToReturn = head
        if slow == head:
            nodeToReturn = head.next
        if prev:
            prev.next = slow.next
            if slow:
                slow.next = None

        return nodeToReturn
