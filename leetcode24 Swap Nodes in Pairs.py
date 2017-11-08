
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):

        res = head
        if not res or not res.next:
            return res

        newres = res.next
        res.next = res.next.next
        newres.next = res
        res = newres

        pre = res.next
        a = pre.next
        b = a.next if a else None

        while a and b:
            a.next = b.next
            b.next = a
            pre.next = b
            pre = a
            a = pre.next if pre else None
            b = a.next if a else None

        return res



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

Sol = Solution()
res = Sol.swapPairs(a)
print res.val
print res.next.val
print res.next.next.val
print res.next.next.next.val
print res.next.next.next.next.val









