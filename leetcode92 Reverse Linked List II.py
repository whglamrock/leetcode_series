from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        # leftPrev is the last node of the non-reverse prefix
        leftPrev = ListNode(0, head)
        dummy = leftPrev
        for i in range(left - 1):
            leftPrev = start
            start = start.next

        curr = start
        # firstReversedNode records the head of the reversing part
        firstReversedNode = curr
        for i in range(right - left):
            next = curr.next
            nextNext = next.next
            # the 'next' node is we are moving. remove it from the list first
            curr.next, next.next = nextNext, None
            # moving the 'next' node to the front of the reversing part
            leftPrev.next = next
            next.next = firstReversedNode
            # reset the firstReversedNode
            firstReversedNode = next

        return dummy.next
