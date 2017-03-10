
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        temp1 = l1
        temp2 = l2
        str1 = ''
        str2 = ''
        while temp1 or temp2:
            if temp1:
                str1 += str(temp1.val)
                temp1 = temp1.next
            if temp2:
                str2 += str(temp2.val)
                temp2 = temp2.next
        num1 = int(str1[::-1])
        num2 = int(str2[::-1])
        num = num1 + num2
        m = ListNode(0)
        temp = m
        if num == 0:
            return m
        while num > 0:
            digit = num % 10
            num = int(num/10)
            newnode = ListNode(digit)
            temp.next = newnode
            temp = temp.next

        return m.next



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





