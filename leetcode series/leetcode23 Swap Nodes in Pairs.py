# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): #plz draw the linked list on the draft paper(use 1->2->3->4 as an example)
    def swapPairs(self, head):
        pre, pre.next = self, head #at first, self.next = head (which in our case, is 1)
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next #in the first round of the above while loop, the "pre.next = b" change
                         #the self.next into 2 in our case.

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









