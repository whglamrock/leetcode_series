
'''
One of the most stupid question. The truth is you can only replace the value but not actually delete the node.
'''

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):

        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):

        node.val = node.next.val
        node.next = node.next.next
        # the leecode asks for returning nothing. modify in-place