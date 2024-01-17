from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        headOfRightHalf = head
        for i in range(length // 2 - 1):
            headOfRightHalf = headOfRightHalf.next
        prevNode = headOfRightHalf
        headOfRightHalf = headOfRightHalf.next
        # cut the second half
        prevNode.next = None

        # reverse the second half
        headOfRightHalf = self.reverseLinkedList(headOfRightHalf)
        currLeft, currRight = head, headOfRightHalf
        for i in range(length // 2):
            if currLeft.val != currRight.val:
                return False
            currLeft = currLeft.next
            currRight = currRight.next
        return True

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            if not nextNode:
                break
            curr = nextNode

        return curr
