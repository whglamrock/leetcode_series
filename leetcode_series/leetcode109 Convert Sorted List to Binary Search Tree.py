# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# idea same with "convert sorted array into a height-balanced BST".
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return

        self.dick = []
        while head:
            self.dick.append(head.val)
            head = head.next

        l, r = 0, len(self.dick) - 1
        m = l + (r - l) / 2
        root = TreeNode(self.dick[m])
        def helper(lo, hi, node, direction):
            if lo > hi:
                return
            m = lo + (hi - lo) / 2
            newnode = TreeNode(self.dick[m])
            if direction == 'L':
                node.left = newnode
            else:
                node.right = newnode
            helper(m + 1, hi, newnode, 'R')
            helper(lo, m - 1, newnode, 'L')

        helper(l, m - 1, root, 'L')
        helper(m + 1, r, root, 'R')
        return root