from typing import Optional, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.leafNodes = set()

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.leafNodes = set()
        nodeToParent = {}
        self.dfs(root, nodeToParent)

        todo = []
        minVal = min(node.val for node in self.leafNodes)
        for node in self.leafNodes:
            if node.val == minVal:
                todo.append(node)
        ans = [self.valueToLetter(todo[0].val)]

        while todo:
            nextNodes = set()
            foundRoot = False
            for node in todo:
                # this is the root node
                if node not in nodeToParent:
                    foundRoot = True
                    break
                nextNodes.add(nodeToParent[node])

            if not nextNodes or foundRoot:
                break

            minVal = min(node.val for node in nextNodes)
            todo = []
            for node in nextNodes:
                if node.val == minVal:
                    todo.append(node)
            if todo:
                ans.append(self.valueToLetter(todo[0].val))

        return ''.join(ans)

    def dfs(self, node: Optional[TreeNode], nodeToParent: Dict[TreeNode, TreeNode]):
        if not node.left and not node.right:
            self.leafNodes.add(node)
            return

        if node.left:
            nodeToParent[node.left] = node
            self.dfs(node.left, nodeToParent)
        if node.right:
            nodeToParent[node.right] = node
            self.dfs(node.right, nodeToParent)

    def valueToLetter(self, value: int):
        return chr(ord('a') + value)
