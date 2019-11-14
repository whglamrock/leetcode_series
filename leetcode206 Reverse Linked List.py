
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None



# non stack O(1) space solution

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        curr = head
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev



'''
# recursive solution

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        nextNode = head.next
        newHead = self.reverseList(nextNode)
        head.next = None
        nextNode.next = head
        
        return newHead
'''








