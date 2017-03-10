# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# build two new linked lists l1,l2 and connect them together.
class Solution(object):
    def partition(self, head, x):

        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next

        l2.next = None
        l1.next = h2.next
        return h1.next


'''
# my original troublesome solution that misinterprets the question
class Solution(object):
    def partition(self, head, x):

        if (not head):
            return head

        prev, small, big = ListNode(None), head, head
        prev.next = head

        tail = head
        countbig = 0
        while tail and tail.next:
            if tail.val >= x:
                countbig += 1
            tail = tail.next
        if tail.val >= x:
            countbig += 1

        while big and big.val < x:
            big = big.next
            prev = prev.next
        while small and small.val >= x:
            small = small.next

        if (not small) or (not big):
            return head
        if tail == big:    # for case like [1,2,2,3]
            return head

        newhead, mid = small, big
        while countbig > 0:
            prev.next = big.next
            tail.next = big
            big.next = None
            tail = tail.next
            countbig -= 1
            if prev.next:
                big = prev.next
            while big and big.val < x:
                big = big.next
                prev = prev.next

        return newhead
'''
