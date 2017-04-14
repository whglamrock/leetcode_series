
# Definition for singly-linked list.

from heapq import *

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


# this way is actually much more efficient because the average size of the heap is len(lists)
#   and it is guaranteed that the nodes come into the heap in a sorted order

class Solution(object):
    def mergeKLists(self, lists):

        pq = []
        dummy = ListNode(0)
        temp = dummy

        for root in lists:
            if root:
                heappush(pq, (root.val, root))
        while pq:
            value, node = heappop(pq)
            if node.next:
                heappush(pq, (node.next.val, node.next))
            temp.next = node
            temp = temp.next

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

lst = [a,d]
Sol = Solution()
value = Sol.mergeKLists(lst)
print value.val



'''
# naive old version:

class Solution(object):
    def mergeKLists(self, lists):

        res = []
        for l in lists:
            while l:
                res.append((l.val, l))
                l = l.next

        res.sort(key=lambda tup: tup[0])

        dummy = ListNode(0)
        temp = dummy

        for l in res:
            dummy.next = l[1]
            dummy = dummy.next

        return temp.next
'''










