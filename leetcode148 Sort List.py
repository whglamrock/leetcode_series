
# normally use merge sort. Get familiar with 'merge sort'!

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



# O(1) space solution is pretty challenging

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # note that we need a prev variable here because we need to split the list
        # think about the case where this list only has 2 nodes: after the below while loop the slow
            # pointer will point to the second node, then we won't be able to split the list
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
            fast = fast.next

        l1 = head
        l2 = slow
        # No need to check whether prev is None because the list has >= 2 nodes at this point
        prev.next = None

        sortedL1 = self.sortList(l1)
        sortedL2 = self.sortList(l2)
        return self.merge(sortedL1, sortedL2)

    def merge(self, l1, l2):
        dummy = ListNode(None)
        tmp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                nextNode = l1.next
                l1.next = None
                l1 = nextNode
            else:
                tmp.next = l2
                nextNode = l2.next
                l2.next = None
                l2 = nextNode
            tmp = tmp.next

        if l1:
            while l1:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
        else:
            while l2:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next

        return dummy.next



dummy = ListNode(None)
curr = dummy
for i in range(10)[::-1]:
    curr.next = ListNode(i)
    curr = curr.next

ans = Solution().sortList(dummy.next)
while ans:
    print ans.val
    ans = ans.next
