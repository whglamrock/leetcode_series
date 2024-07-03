from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        vals = []
        indexToNode = {}
        i = 0
        while curr:
            vals.append(curr.val)
            nextNode = curr.next
            curr.next = None

            indexToNode[i] = curr
            curr = nextNode
            i += 1

        ans = deque([indexToNode[len(vals) - 1]])
        currMax = vals[-1]
        for i in range(len(vals) - 2, -1, -1):
            if vals[i] >= currMax:
                ans.appendleft(indexToNode[i])
            currMax = max(currMax, vals[i])

        for i in range(len(ans) - 1):
            currNode, nextNode = ans[i], ans[i + 1]
            currNode.next = nextNode

        return ans[0]
