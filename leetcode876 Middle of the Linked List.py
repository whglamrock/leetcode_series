
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# cleanest solution

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow



'''
# practice

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(None)
        dummyHead.next = head
        slow, fast = dummyHead, dummyHead

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        # clean up the linkedList if neccesary
        # dummyHead.next = None
        return slow
'''