from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        oddDummy, evenDummy = ListNode(), ListNode()
        # odd, even refer to the current tails of 2 separate linkedLists
        odd, even = oddDummy, evenDummy
        curr = head

        # curr is always the odd node
        while curr:
            odd.next = curr
            nextEven = curr.next
            if not nextEven:
                odd = odd.next
                break

            even.next = nextEven
            curr.next = None  # cut the connection between curr and curr's next even node

            odd = odd.next
            even = nextEven
            curr = even.next
            even.next = None

        odd.next = evenDummy.next
        return head
