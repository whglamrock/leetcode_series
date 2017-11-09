
import random

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


class Solution(object):

    def __init__(self, head):

        self.head = head

    def getRandom(self):

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