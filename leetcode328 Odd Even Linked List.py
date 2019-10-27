
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



# the idea is use 2 pointers to represent the odd and even list, then connect the odd tail with even head

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        oddDummy, evenDummy = ListNode(None), ListNode(None)
        odd, even = oddDummy, evenDummy
        curr = head

        while curr:
            odd.next = curr
            if not curr.next:
                # don't forget about this step because the position of odd is very important for
                    # connecting the odd list and even list
                odd = odd.next
                break
            even.next = curr.next

            # disconnect the node at even position
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = None

            odd = odd.next
            even = even.next
            curr = curr.next

        odd.next = evenDummy.next
        return head  # can also return oddDummy.next



head = ListNode(None)
node = head
for i in xrange(1, 8):
    node.next = ListNode(i)
    node = node.next
head = head.next

curr = Solution().oddEvenList(head)
while curr:
    print curr.val
    curr = curr.next
