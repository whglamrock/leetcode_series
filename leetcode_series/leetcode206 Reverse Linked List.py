
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):

        if (not head) or head.next == None:
            return head

        tail = head
        while tail.next:
            tail = tail.next

        curr = head
        prev = ListNode(None)
        prev.next = curr
        while curr != tail:
            if curr == head:
                prev.next = curr.next
                tail.next = curr
                curr.next = None
                curr = prev.next
            else:
                prev.next = curr.next
                curr.next = tail.next
                tail.next = curr
                curr = prev.next

        return tail



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
# recursive solution:

class Solution(object):
    def reverseList(self, head):

        if (not head) or head.next == None:
            return head

        tail = head
        length = 0
        while tail.next:
            tail = tail.next
            length += 1

        def recursive(root, currhead, iteration):
            if iteration == length:
                return currhead

            prev = root
            curr = prev.next
            prev.next = curr.next
            curr.next = currhead

            return recursive(prev,curr,iteration+1)

        return recursive(head,head,0)
'''









