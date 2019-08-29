
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None



from heapq import *

# O(N * logK) solution, where K is len(lists), N is the total number of nodes in all lists

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        # use a dummy head to avoid checking "if not root: root = node" in the while loop
        dummy = ListNode(None)
        tmp = dummy

        pq = []
        heapify(pq)
        # initialize the pq
        for root in lists:
            # leetcode does give the corner case like [[]]
            if root:
                heappush(pq, (root.val, root))

        while pq:
            val, node = heappop(pq)
            if node.next:
                heappush(pq, (node.next.val, node.next))
            tmp.next = node
            node.next = None
            tmp = tmp.next

        return dummy.next



a = ListNode(0)
b = ListNode(3)
c = ListNode(5)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(2)
f = ListNode(4)
d.next = e
e.next = f

root = Solution().mergeKLists([a,d])
while root:
    print root.val
    root = root.next







