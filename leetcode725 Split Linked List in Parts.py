from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1
        partSize, numOfPartsWithExtra1Node = length // k, length % k

        ans = []
        curr = head
        prev = None
        while curr:
            partHead = curr
            for i in range(partSize):
                if not curr:
                    break
                prev = curr
                curr = curr.next
            if numOfPartsWithExtra1Node and curr:
                prev = curr
                curr = curr.next
                numOfPartsWithExtra1Node -= 1
            if prev:
                prev.next = None
            ans.append(partHead)

        for i in range(k - len(ans)):
            ans.append(None)
        return ans
