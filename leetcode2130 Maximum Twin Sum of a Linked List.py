from collections import deque
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        vals = deque()
        while curr:
            vals.append(curr.val)
            curr = curr.next

        ans = 0
        while vals:
            twinSum = vals.popleft()
            if vals:
                twinSum += vals.pop()
            ans = max(ans, twinSum)

        return ans
