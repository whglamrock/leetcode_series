
# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findTarget(self, root, k):

        valueToCount = set()
        todo = [root]

        while todo:
            next = []
            while todo:
                node = todo.pop()
                if k - node.val in valueToCount:
                    return True
                valueToCount.add(node.val)
                if node.right:
                    next.append(node.right)
                if node.left:
                    next.append(node.left)
            todo = next

        return False