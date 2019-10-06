
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
        ans = None
        prev = None
        for digit in num:
            node = ListNode(int(digit))
            if prev:
                prev.next = node
            prev = node
            if not ans:
                ans = prev

        return ans

    def convertListToNum(self, head):
        num = []
        while head:
            num.append(str(head.val))
            head = head.next
        return int(''.join(num[::-1]))





