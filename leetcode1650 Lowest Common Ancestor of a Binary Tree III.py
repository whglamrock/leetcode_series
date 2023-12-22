"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        parentsOfP = set()
        parentsOfQ = set()

        while p or q:
            if p and p == q:
                return p
            if p is not None and p in parentsOfQ:
                return p
            if q is not None and q in parentsOfP:
                return q
            if p is not None:
                parentsOfP.add(p)
            if q is not None:
                parentsOfQ.add(q)
            if p is not None and p.parent:
                p = p.parent
            if q is not None and q.parent:
                q = q.parent



