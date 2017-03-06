# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):

        if (not head) or (not head.next):
            return True

        def reverseList(root):
            tail = root
            while tail.next:
                tail = tail.next

            curr = root
            prev = ListNode(None)
            prev.next = curr
            while curr != tail:
                if curr == root:
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

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = reverseList(slow.next)
        slow = slow.next

        while head and slow:
            if head.val != slow.val:
                return False
            head, slow = head.next, slow.next

        return True

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(2)
f = ListNode(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

Sol = Solution()
print(Sol.isPalindrome(a))








