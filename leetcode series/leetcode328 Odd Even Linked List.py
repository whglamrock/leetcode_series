# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):

        if (not head) or (not head.next) or (not head.next.next):
            return head

        even = head.next
        odd = even.next
        mark = head

        while odd and even: # set 2 pointers (one odd, one even)
            even.next = odd.next
            odd.next = mark.next
            mark.next = odd

            mark = mark.next
            even = even.next
            if (not even): break
            odd = even.next
        # after each while loop, the off number will be ripped off and there are two
        # consecutive even numbers.

        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
#g = ListNode(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
#f.next = g

Sol = Solution()
value = Sol.oddEvenList(a)
while value:
    print value.val
    value = value.next
