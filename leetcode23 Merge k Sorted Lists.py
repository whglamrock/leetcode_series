from heapq import *
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        # the reason to use this map is in python ListNode object is not comparable
        indexToCurrNode = {}
        for i, head in enumerate(lists):
            if head:
                heappush(pq, [head.val, i])
                indexToCurrNode[i] = head

        dummy = ListNode()
        curr = dummy
        while pq:
            val, i = heappop(pq)
            node = indexToCurrNode[i]
            if node.next:
                heappush(pq, [node.next.val, i])
                indexToCurrNode[i] = node.next
                node.next = None
            else:
                del indexToCurrNode[i]
            curr.next = node
            curr = curr.next

        return dummy.next


def buildList(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        curr.next = node
        curr = curr.next

    return head

def traverseList(head: Optional[ListNode]):
    if not head:
        return
    nums = []
    curr = head
    while curr:
        nums.append(curr.val)
        curr = curr.next
    print(nums)


root1 = buildList([0, 3, 5])
root2 = buildList([1, 6, 8])
root3 = buildList([1, 2, 4])
traverseList(Solution().mergeKLists([root1, root2, root3]))
