from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        traversal = []
        currLevel = [root]
        # level order traversal to get nodes in each level, from left to right
        while currLevel:
            traversal.append(currLevel)
            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel = nextLevel

        for i, level in enumerate(traversal):
            # even level
            if i % 2 == 0:
                for j in range(len(level)):
                    # no strictly increasing
                    if j < len(level) - 1 and not (level[j].val < level[j + 1].val):
                        return False
                    # node value is not odd value
                    if level[j].val % 2 == 0:
                        return False
            # odd level
            else:
                for j in range(len(level)):
                    # no strictly decreasing
                    if j < len(level) - 1 and not (level[j].val > level[j + 1].val):
                        return False
                    # node value is not even value
                    if level[j].val % 2 != 0:
                        return False

        return True
