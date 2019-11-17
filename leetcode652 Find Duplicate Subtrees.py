
from collections import defaultdict

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        strFormatToNodes = defaultdict(list)
        self.preOrderTraversal(root, strFormatToNodes)

        ans = []
        for nodes in strFormatToNodes.values():
            if len(nodes) >= 2:
                ans.append(nodes[0])

        return ans

    def preOrderTraversal(self, node, strFormatToNodes):
        if not node:
            return 'None'
        strFormat = str(node.val) + ',' + self.preOrderTraversal(node.left, strFormatToNodes) + ',' \
                    + self.preOrderTraversal(node.right, strFormatToNodes)
        strFormatToNodes[strFormat].append(node)
        return strFormat