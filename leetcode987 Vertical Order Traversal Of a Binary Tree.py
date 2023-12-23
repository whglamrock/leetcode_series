from heapq import *
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        columnToNodes = defaultdict(list)
        self.generateColumnToNodes(root, columnToNodes, 0, 0)
        minColumn = min(columnToNodes.keys())
        maxColumn = max(columnToNodes.keys())

        ans = []
        for column in range(minColumn, maxColumn + 1):
            nodeList = []
            nodesInColumn = columnToNodes[column]
            while nodesInColumn:
                row, val, node = heappop(nodesInColumn)
                nodeList.append(val)
            ans.append(nodeList)

        return ans

    # generates: column index to node, and (row, col) index to node
    def generateColumnToNodes(self, root, columnToNodes, row, column):
        if not root:
            return
        heappush(columnToNodes[column], [row, root.val, root])
        if root.left:
            self.generateColumnToNodes(root.left, columnToNodes, row + 1, column - 1)
        if root.right:
            self.generateColumnToNodes(root.right, columnToNodes, row + 1, column + 1)


def bfsGenerateTreeFromValArray(vals):
    if not vals:
        return None

    vals = deque(vals)
    root = TreeNode(vals.popleft())
    row = [root]

    while vals:
        nextRow = []
        for node in row:
            if vals:
                val = vals.popleft()
                if val is not None:
                    leftNode = TreeNode(val)
                    node.left = leftNode
                    nextRow.append(leftNode)
            if vals:
                val = vals.popleft()
                if val is not None:
                    rightNode = TreeNode(val)
                    node.right = rightNode
                    nextRow.append(rightNode)
        row = nextRow

    return root


def printTree(root):
    vals = []
    todo = [root]

    while todo:
        nextTodo = []
        for node in todo:
            if node is None:
                vals.append(None)
                continue
            vals.append(node.val)
            if not node.left:
                nextTodo.append(None)
            else:
                nextTodo.append(node.left)
            if not node.right:
                nextTodo.append(None)
            else:
                nextTodo.append(node.right)
        todo = nextTodo

    while vals and vals[-1] is None:
        vals.pop()

    print(vals)


root1 = bfsGenerateTreeFromValArray([3, 9, 20, None, None, 15, 7])
printTree(root1)
print(Solution().verticalTraversal(root1))
root2 = bfsGenerateTreeFromValArray([1, 2, 3, 4, 5, 6, 7])
printTree(root2)
print(Solution().verticalTraversal(root2))

