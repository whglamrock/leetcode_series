from typing import Optional, Tuple, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevTail = None
        ans = None
        curr = head

        while curr:
            currHead = curr
            lengthOfChunk = 0
            for i in range(k - 1):
                if not curr:
                    break
                curr = curr.next
                lengthOfChunk += 1
            # point curr to the head of next k chunk
            tail = curr
            # there are k nodes
            if curr:
                curr = curr.next
                lengthOfChunk += 1
                tail.next = None
                # cut the head the k chunk we are trying to reverse from prevTail
                if prevTail:
                    prevTail.next = None

            if lengthOfChunk == k:
                # we make sure the k chunk we are trying to reverse
                # is cut from its previous node and k + 1 node (i.e., curr)
                newHead, newTail = self.reverseLinkedList(currHead)
                # just in case next chunk has < k nodes
                newTail.next = curr
                if not ans:
                    ans = newHead
                if prevTail:
                    prevTail.next = newHead
                prevTail = newTail

        return ans

    def reverseLinkedList(self, head: ListNode) -> Tuple[ListNode, ListNode]:
        dummy = ListNode()
        curr = head

        while curr:
            # cut the current head from the original list
            nextNode = curr.next
            curr.next = None

            headOfReversed = dummy.next
            if headOfReversed:
                curr.next = headOfReversed
            dummy.next = curr

            curr = nextNode

        newHead = dummy.next
        dummy.next = None
        return newHead, head


def buildList(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        curr.next = node
        curr = curr.next

    return head

def traverseList(head: Optional[ListNode]):
    if not head:
        return
    nums = []
    curr = head
    while curr:
        nums.append(curr.val)
        curr = curr.next
    print(nums)


head = buildList([1, 2, 3, 4, 5, 6, 7, 8])
traverseList(Solution().reverseKGroup(head, 6))
head = buildList([1, 2, 3, 4, 5, 6])
traverseList(Solution().reverseKGroup(head, 3))
head = buildList([1])
traverseList(Solution().reverseKGroup(head, 1))
