from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        nodes = deque()
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = None
            nodes.append(curr)
            curr = nextNode

        # leetcode does give some stupidly big value for k
        k %= len(nodes)
        for i in range(k):
            lastNode = nodes.pop()
            nodes.appendleft(lastNode)

        for i in range(len(nodes) - 1):
            currNode, nextNode = nodes[i], nodes[i + 1]
            currNode.next = nextNode

        return nodes[0]
