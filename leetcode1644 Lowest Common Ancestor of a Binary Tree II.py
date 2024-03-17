from typing import Dict, Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional[TreeNode]:
        nodeToDepth, nodeToParent = {}, {}
        nodeToParent[root] = root
        self.traverseTree(root, nodeToDepth, nodeToParent, 0)

        if p not in nodeToDepth or q not in nodeToDepth:
            return None

        # make sure p is lower (has a bigger depth)
        if nodeToDepth[p] < nodeToDepth[q]:
            p, q = q, p
        # move p to same level as q
        while nodeToDepth[p] > nodeToDepth[q]:
            p = nodeToParent[p]

        if p.val == q.val:
            return p

        # start searching upwards
        todo = {p, q}
        ans = None
        while todo:
            nextTodo = set()
            for node in todo:
                nextTodo.add(nodeToParent[node])
            if len(nextTodo) == 1:
                ans = list(nextTodo)[0]
                break
            todo = nextTodo

        return ans

    def traverseTree(self, node: 'TreeNode', nodeToDepth: Dict['TreeNode', int], nodeToParent: Dict['TreeNode', 'TreeNode'], depth: int):
        nodeToDepth[node] = depth
        if node.left:
            nodeToParent[node.left] = node
            self.traverseTree(node.left, nodeToDepth, nodeToParent, depth + 1)
        if node.right:
            nodeToParent[node.right] = node
            self.traverseTree(node.right, nodeToDepth, nodeToParent, depth + 1)
