from collections import deque
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        if (not l1): return l2
        if (not l2): return l1

        head1, head2 = l1, l2
        len1, len2 = 0, 0
        while head1 and head2:
            head1 = head1.next
            head2 = head2.next
            len1 += 1
            len2 += 1

        if head1 == None:   # linkedlist1 is shorter
            while head2:
                head2 = head2.next
                len2 += 1
            l1, l2 = l2, l1
            len1, len2 = len2, len1
        else:
            while head1:
                head1 = head1.next
                len1 += 1

        stack, queue = [], deque()
        head1, head2 = l1, l2
        for i in xrange(len1 - len2):
            stack.append(head1.val)
            head1 = head1.next

        carry, digit = 0, 0
        for i in xrange(len2):
            digit = (head1.val + head2.val) % 10
            carry = (head1.val + head2.val) / 10
            if carry == 0:
                stack.append(digit)
            else:
                queue.appendleft(digit)
                while stack and carry:
                    last = stack.pop()
                    digit = (last + carry) % 10
                    carry = (last + carry) / 10
                    queue.appendleft(digit)
                if carry:   # stack is empty
                    stack.append(carry)
                while queue:
                    stack.append(queue.popleft())
            head1 = head1.next
            head2 = head2.next

        ans = ListNode(stack[0])
        res = ans
        for i in xrange(1, len(stack)):
            newnode = ListNode(stack[i])
            ans.next = newnode
            ans = ans.next

        return res