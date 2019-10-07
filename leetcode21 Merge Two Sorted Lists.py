
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(None)
        tmp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        if l1:
            tmp.next = l1
        # l2 can be None and it's covered
        else:
            tmp.next = l2

        return dummy.next



'''
# the following solution actually makes a new list instead of connecting the original two. In real interview, we
    # need to clearly ask what they want
    
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(None)
        tmp = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
            tmp = tmp.next
            
        while l1:
            tmp.next = ListNode(l1.val)
            l1 = l1.next 
            tmp = tmp.next
        while l2:
            tmp.next = ListNode(l2.val)
            l2 = l2.next    
            tmp = tmp.next
        
        return dummy.next
'''
