# this algorithm doesn't actually remove the leaves but makes their value '#' after
# 'stripping them off' so next time the 'stripped' leaves will be ignored.
class Solution(object):
    def findLeaves(self, root):
        def markLeaves(p, l):

            leaf = True
            if p.left and p.left.val != '#':
                leaf = False
                markLeaves(p.left, l)
            if p.right and p.right.val != '#':
                leaf = False
                markLeaves(p.right, l)
            if leaf:
                l.append(p.val)
                p.val = '#'

        res = []
        p = root
        while p and p.val != '#':
            l = []
            markLeaves(p, l)
            res.append(l)
            # p = root    # the markleaves recursion went p.left or p.right that doesn't change the p value
        return res