
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None



# O(1) space solution has to modify the original linkedList.
    # If interviewer asks for O(1) space, it's a > medium question

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True

        # tail will be the head of the reversed second half
        tail = head
        while tail.next:
            tail = tail.next

        slow, fast = head, head
        # the while condition will always make sure slow points to:
            # 1) middle point of the list if there are odd number of nodes
            # 2) last node of the first half if there are even number of nodes
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        headOfSecondHalf = slow.next
        slow.next = None
        self.reverseLinkedList(headOfSecondHalf)

        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        return True

    def reverseLinkedList(self, head):
        if not head.next:
            return head

        nextNode = head.next
        head.next = None
        reversedTail = self.reverseLinkedList(nextNode)
        reversedTail.next = head
        return head



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

print Solution().isPalindrome(a)








