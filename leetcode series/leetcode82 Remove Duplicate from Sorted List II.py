# O(n) time, O(1) space solution
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):

        if (not head): return None

        prev = ListNode(None)
        prev.next, temp = head, head
        dummy = prev

        while temp and temp.next:
            if temp.val == temp.next.val:
                while temp and temp.next and temp.val == temp.next.val:
                    temp.next = temp.next.next
                prev.next = temp.next
                temp = prev.next
            else:
                temp = temp.next
                prev = prev.next

        return dummy.next