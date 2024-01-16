from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        # make sure list1's head is smaller
        if list1.val > list2.val:
            list1, list2 = list2, list1

        head = list1
        curr1, curr2 = list1, list2
        prev1, prev2 = None, None
        while curr1 and curr2:
            # just move the pointer in list1
            if curr1.val <= curr2.val:
                prev1 = curr1
                curr1 = curr1.next
            # need to cut the node in list2 and put it in list1
            else:
                # cut the node in list2
                next2 = curr2.next
                if prev2:
                    prev2.next = next2
                curr2.next = None

                # put curr2 before curr1
                prev1.next = curr2
                curr2.next = curr1
                prev1 = curr2
                curr2 = next2

        # we've done traversing list1 but not finished with list2
        if curr2:
            prev1.next = curr2

        return head


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


list1 = buildList([1, 2, 3, 4])
list2 = buildList([7, 8, 9, 10, 14])
print(traverseList(Solution().mergeTwoLists(list1, list2)))
