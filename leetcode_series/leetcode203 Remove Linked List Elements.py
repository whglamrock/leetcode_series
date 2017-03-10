# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):

        if not head:
            return head
        prev = ListNode(None)
        curr = head
        prev.next = curr
        res = prev
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
                continue
            else:
                curr = curr.next
                prev = prev.next

        return res.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(1)
d = ListNode(4)
e = ListNode(6)
f = ListNode(6)
g = ListNode(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

Sol = Solution()
ans = Sol.removeElements(a,7)
print ans.val
print ans.next.val
print ans.next.next.val
print ans.next.next.next.val
print ans.next.next.next.next.val

