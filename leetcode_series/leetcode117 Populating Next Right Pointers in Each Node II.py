
# Definition for binary tree with next pointer.

class TreeLinkNode:
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None
        self.next = None


# the idea is using two pointers to keep track level traversal (in which the pointer of upper
#   level pointer is similar to lc116).
# Because the upper level is 'already connected' by the previous loop, so we don't save
#   the previous level traversal to reference this level's nodes (just need two pointers)

class Solution:
    def connect(self, root):

        if not root:
            return

        # used to loop through the current upper level
        curr = root

        while curr:
            # prev is the key of connection, by which we don't needa check whether the next
            #   available node is the first node of this lower level (because we initialize
            #   the prev with None).
            # head is simply to mark the start of next(lower) level
            prev, theheadofnextlevel = None, None
            while curr:
                if curr.left:
                    # then it's time to mark the start of next level
                    if not prev:
                        theheadofnextlevel = curr.left
                    else:   # prev is just a reference of the previously connected node
                        prev.next = curr.left
                    # we don't do "prev = prev.next" here since it don't fit the "if not prev" scenario
                    prev = curr.left
                if curr.right:
                    # likewise
                    if not prev:
                        theheadofnextlevel = curr.right
                    else:
                        prev.next = curr.right
                    prev = curr.right
                curr = curr.next
            # restart from the head of next level
            curr = theheadofnextlevel