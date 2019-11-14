
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None



# should have been an easy question

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.convertListToNum(l1)
        num2 = self.convertListToNum(l2)
        num = str(num1 + num2)[::-1]

        dummy = ListNode(None)
        curr = dummy
        for digit in num:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next

    def convertListToNum(self, head):
        num = []
        while head:
            num.append(str(head.val))
            head = head.next
        return int(''.join(num[::-1]))





