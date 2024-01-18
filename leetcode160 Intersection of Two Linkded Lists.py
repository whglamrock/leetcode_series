from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        lengthOfA = 0
        while currA:
            lengthOfA += 1
            currA = currA.next
        currB = headB
        lengthOfB = 0
        while currB:
            lengthOfB += 1
            currB = currB.next
        if lengthOfA < lengthOfB:
            headA, headB = headB, headA
            lengthOfA, lengthOfB = lengthOfB, lengthOfA

        for i in range(lengthOfA - lengthOfB):
            headA = headA.next

        currA, currB = headA, headB
        while currA:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next

        return None
