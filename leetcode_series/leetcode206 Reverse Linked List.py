
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


# the idea is to disconnnect the node one by one from head
#   and connect to newhead's previous, while the new linkedlist is never connected the old one

class Solution(object):
    def reverseList(self, head):

        if not head: return

        newhead = None
        while head:
            # the nextnode serves as "temp" to locate the next node to be disconnected
            nextnode = head.next
            # at this point, the head is the newly disconnected node, and need to be newhead's previous
            head.next = newhead
            # newhead points to its previous, the newly disconnected node we just connected in above line
            newhead = head
            # the head points to the residue of old linkedlist
            head = nextnode

        return newhead



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
x = Sol.reverseList(a)
while x:
    print x.val
    x = x.next



'''
# recursive solution (slow, not recommended)

class Solution(object):
    def reverseList(self, head):

        return self.moveFromOldToNew(head, None)

    def moveFromOldToNew(self, head, newhead):

        if not head:
            return newhead
        nextnode = head.next
        head.next = newhead
        newhead = head
        head = nextnode

        return self.moveFromOldToNew(head, newhead)
'''









