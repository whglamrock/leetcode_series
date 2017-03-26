
'''
idea came from: https://leetcode.com/discuss/86469/python-easy-iterative-and-recursive-solution
construct an BST like the one from https://en.wikipedia.org/wiki/Binary_search_tree
and go through the while loop.
'''

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):

        stack = []
        while root or stack:
            while root:
                stack.append(root)  # record the nodes, cuz they can't go up to their parent node
                root = root.left  # always goes left to find the smallest one in each branch
                # in our case, the above line does: 8->3->1; 6->4.
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right  # not from stack, but from the smallest node's right.
            # in our case when the above line makes root 3->6, this move makes sure we won't
            # overlook numbers between 3~6 (in the next while loop, 6->4, stack.append(4)).



a = TreeNode(8)
b = TreeNode(3)
c = TreeNode(10)
d = TreeNode(1)
e = TreeNode(6)
f = TreeNode(14)
g = TreeNode(4)
h = TreeNode(7)
i = TreeNode(13)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

Sol = Solution()
ans = Sol.kthSmallest(a,1)
print ans






