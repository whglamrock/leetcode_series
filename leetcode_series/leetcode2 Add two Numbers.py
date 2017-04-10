
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        if not l1 or not l2:
            return None

        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num1 = num1[::-1]
        num2 = num2[::-1]

        num = int(num1) + int(num2)
        res = ListNode(0)
        if num == 0: return res
        temp = res
        while num:
            newnode = ListNode(num % 10)
            num /= 10
            temp.next = newnode
            temp = temp.next

        return res.next



a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)
d.next = e
e.next = f

Sol = Solution()
g = Sol.addTwoNumbers(a,d)
print g.val
print g.next.val
print g.next.next.val





