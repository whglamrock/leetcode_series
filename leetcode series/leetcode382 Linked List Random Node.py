# Definition for singly-linked list.
import random
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if not self.head:
            return

        count = 0
        tmp = self.head
        ans = tmp.val
        while tmp:
            if random.randint(0, count) is 0:
                ans = tmp.val
            tmp = tmp.next
            count += 1
        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()