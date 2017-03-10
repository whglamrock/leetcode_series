
from collections import defaultdict

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):

        if not root:
            return []

        self.freq = defaultdict(int)
        def helper(node):
            sumvalue = node.val
            if node.left:
                sumvalue += helper(node.left)
            if node.right:
                sumvalue += helper(node.right)
            self.freq[sumvalue] += 1
            return sumvalue

        helper(root)

        ans = []
        highestfreq = max(self.freq.values())
        for sumvalue in self.freq:
            if self.freq[sumvalue] == highestfreq:
                ans.append(sumvalue)

        return ans

