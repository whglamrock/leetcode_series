
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



# no extra space solution. see floyd's algorithm explanation from:
    # https://www.youtube.com/watch?time_continue=2&v=zbozWoMgKW0

# the idea is when slow & fast pointers meet, distance(head, cycleStartingPoint) = distance(fast, cycleStartingPoint),
    # assuming we go around the cycle clockwise

class Solution(object):
    def detectCycle(self, head):

        if not head:
            return None

        fast = self.hasCycle(head)
        if not fast:
            return None

        slow = head    # see explanation below
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    # from lc141
    def hasCycle(self, head):

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return fast

        return None

