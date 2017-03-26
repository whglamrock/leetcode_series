
# Definition for binary tree with next pointer.

class TreeLinkNode:
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None
        self.next = None


# the idea is using two pointers to keep track level traversal.
# Because the upper level is 'already connected' by the previous loop, so we don't save
#   the previous level traversal to reference this level's nodes (just need two pointers)

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        head = root
        while head:

            # use the curr as the level traversal pointer
            curr = head
            prev, head = None, None

            while curr:
                if curr.left:
                    # means the first node at this level hasn't been found yet
                    if not prev:
                        head = curr.left
                    else:
                        prev.next = curr.left
                    prev = curr.left
                if curr.right:
                    # likewise
                    if not prev:
                        head = curr.right
                    else:
                        prev.next = curr.right
                    prev = curr.right
                curr = curr.next