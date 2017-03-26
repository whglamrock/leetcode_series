
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


# use two pointer, in every round of while loop, the distance between fast & slow +1.

class Solution(object):
    def hasCycle(self, head):

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next # fast move two nodes
            slow = slow.next # slow move one node
            if slow == fast: # if there is a cycle, once the distance is appropriate it will appear.
                return True

        return False



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = c

Sol = Solution()
print Sol.hasCycle(a)



