from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head
        for i in range(k - 1):
            fast = fast.next
        # at this point the distance between slow & fast is k

        left = fast
        while fast.next:
            slow = slow.next
            fast = fast.next

        right = slow
        left.val, right.val = right.val, left.val
        return head


'''
# dumbest way: storing the values --> interviewer may not be happy with it
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        k -= 1
        l, r = k, len(vals) - 1 - k
        vals[l], vals[r] = vals[r], vals[l]
        newHead = ListNode(vals[0])
        curr = newHead
        for val in vals[1:]:
            node = ListNode(val)
            curr.next = node
            curr = node

        return newHead
'''