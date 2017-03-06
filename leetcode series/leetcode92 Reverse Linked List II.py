# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# one pass, in-place solution
class Solution(object):
    def reverseBetween(self, head, m, n):

        if (not head) or (not head.next):
            return head

        find = ListNode(None)
        find.next = head
        dummy = find

        for i in xrange(m-1):
            find = find.next

        #if (not find.next) or (not find.next.next):    # cuz 1<=m<=n<=len(list),
            #return head        # this condition actually will not happen

        tail = find.next
        for i in xrange(n-m):
            swap = tail.next
            tail.next = swap.next
            swap.next = find.next
            find.next = swap

        return dummy.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
Sol = Solution()
ans = Sol.reverseBetween(a, 2, 5)
while ans:
    print ans.val
    ans = ans.next