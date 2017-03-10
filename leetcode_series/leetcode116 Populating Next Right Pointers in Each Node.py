# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        while root:
            cur = root
            while cur:
                # no need to check cur.right because of the problem settings
                if cur.left:
                    cur.left.next = cur.right
                # we needa check both next and right
                if cur.next and cur.right:
                    cur.right.next = cur.next.left
                cur = cur.next
            root = root.left

