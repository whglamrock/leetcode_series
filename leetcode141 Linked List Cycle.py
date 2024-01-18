from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next

        while slow != fast:
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next
            if not fast.next:
                return False
            fast = fast.next

        return True
