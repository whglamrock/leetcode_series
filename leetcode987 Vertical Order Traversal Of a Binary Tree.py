from collections import defaultdict, deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        colToVals = defaultdict(list)
        minCol, maxCol = 0, 0
        todo = [[root, 0]]
        while todo:
            nextTodo = []
            currColToVals = defaultdict(list)
            for node, col in todo:
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)
                currColToVals[col].append(node.val)
                if node.left:
                    nextTodo.append([node.left, col - 1])
                if node.right:
                    nextTodo.append([node.right, col + 1])
            for col, vals in currColToVals.items():
                colToVals[col].extend(sorted(vals))
            todo = nextTodo

        ans = []
        for col in range(minCol, maxCol + 1):
            ans.append(colToVals[col])
        return ans


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

