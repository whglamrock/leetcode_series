
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


# no extra space solution. idea came from: https://discuss.leetcode.com/topic/43858/python-o-n-no-extra-space-with-mathematical-explanation

class Solution(object):
    def detectCycle(self, head):

        slow = fast = head  # remember this define method

        while fast is not None:
            fast = fast.next
            if (not fast):
                return None
            fast = fast.next
            slow = slow.next
            if slow == fast:
                break

        if (not fast):
            return None

        slow = head    # see explanantion below
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

# The 'pivot' is where the cycle starts. Let's assume the length of left part = l, the length of right part(cycle)
# = r, after the first while loop, 'slow' stops at n.

# The 'fast' goes through 2*n steps. By its actual trail, u can tell it went beyond the 'slow' few cycles. So after
# tried so many cases, we have: n = k*r (k is a positive integer).

# In the above solution, we need to prove l = p*r + (r+l-n) to explain the second while loop. p is a positive integer,
# r+l-n is the length after the stop position of 'slow' in the first while loop.

# And... n = l + (n-l)  ->  k*r = l + (n-l)  ->  l = (k-1)*r + (l+r-n). It doesn't matter whether p == k-1, because
# even if the new 'slow' (in the 2nd while loop) goes through more or fewer cycles, it will still meet the
# 'fast' at the cycle start point.



'''
# o(1) space. Not sure if this counts as 'no extra space'?
class Solution(object):
    def detectCycle(self, head):

        if (not head):
            return
        if head.next == head:
            return head

        slow = fast = head
        countslow, countfast, cycle = 0, 0, 0
        while (fast and fast.next):
            fast = fast.next.next
            countfast += 2
            slow = slow.next
            countslow += 1
            if slow == fast:
                cycle = countfast - countslow
                break

        if cycle == 0:
            return

        redo, compare = head, head
        for i in xrange(cycle):
            compare = compare.next

        while redo:
            if redo == compare:
                return redo
            else:
                redo = redo.next
                compare = compare.next
'''