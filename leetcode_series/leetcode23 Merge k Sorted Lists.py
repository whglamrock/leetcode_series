# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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










