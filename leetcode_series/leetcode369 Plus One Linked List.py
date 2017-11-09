
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


class Solution(object):
    def plusOne(self, head):

        def add(head):
            if not head:
                return 1
            head.val += add(head.next)
            head.val, carry = head.val%10, head.val/10
            return carry

        carry = add(head)
        if carry == 1:  # the original no. is like 99,999.. that adding 1 will change the total number of digits
            addc = ListNode(1)
            addc.next = head
            return addc
        else:
            return head



'''
# my original inefficient solution

class Solution(object):
    def plusOne(self, head):

        if (not head):
            return

        value = 0
        while head:
            value = value*10+head.val
            head = head.next

        value += 1
        value = str(value)
        head = ListNode(None)
        pre = head
        for i in xrange(len(value)):
            new = ListNode(int(value[i]))
            pre.next = new
            pre = pre.next

        return head.next
'''