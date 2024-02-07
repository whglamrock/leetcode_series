from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# remember to always update prefixSumToIndex whenever we make a change to indexesAfterRemoval
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next

        prefixSum = 0
        prefixSumToIndex = {}
        numsAfterRemoval = []
        indexesAfterRemoval = set()
        for i, num in enumerate(nums):
            prefixSum += num
            # remove all numbers
            if prefixSum == 0:
                numsAfterRemoval = []
                indexesAfterRemoval = set()
                prefixSumToIndex[prefixSum] = i
            elif prefixSum in prefixSumToIndex and prefixSumToIndex[prefixSum] in indexesAfterRemoval:
                while numsAfterRemoval and numsAfterRemoval[-1][0] > prefixSumToIndex[prefixSum]:
                    prevI, prevNum = numsAfterRemoval.pop()
                    indexesAfterRemoval.discard(prevI)
            # whenever we add an index, we need to update the prefixSumToIndex. This is to avoid missing
            # any subarray sum == 0 but we fail to pop the subarray elements due to the above while loop condition.
            else:
                numsAfterRemoval.append([i, num])
                prefixSumToIndex[prefixSum] = i
                indexesAfterRemoval.add(i)

        dummy = ListNode()
        curr = dummy
        for i, num in numsAfterRemoval:
            node = ListNode(num)
            curr.next = node
            curr = node

        return dummy.next
