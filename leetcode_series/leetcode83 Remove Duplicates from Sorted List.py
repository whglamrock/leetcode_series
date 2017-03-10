# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):

        if (not head):
            return head

        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next  # temp still at its old position, for case like
                # 3->2->2->2. Thus we don't perform temp = temp.next
            else:
                temp = temp.next

        return head


