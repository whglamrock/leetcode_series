
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# classic BFS solution, and it's inconvenient to do DFS here

class Solution(object):
    def averageOfLevels(self, root):

        if not root:
            return []

        todo = [root]
        res = []
        while todo:
            next = []
            sumofcurrline = 0
            numofnodesincurrline = 0
            while todo:
                node = todo.pop()
                sumofcurrline += node.val
                numofnodesincurrline += 1
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            res.append(float(sumofcurrline) / numofnodesincurrline)
            todo = next

        return res
