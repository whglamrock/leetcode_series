from collections import deque
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1, nums2 = deque(), deque()
        while l1:
            nums1.appendleft(str(l1.val))
            l1 = l1.next
        while l2:
            nums2.appendleft(str(l2.val))
            l2 = l2.next

        num1 = int(''.join(nums1))
        num2 = int(''.join(nums2))
        num = str(num1 + num2)
        head = ListNode(int(num[-1]))
        prev = head
        for i in range(len(num) - 2, -1, -1):
            node = ListNode(int(num[i]))
            prev.next = node
            prev = node

        return head
