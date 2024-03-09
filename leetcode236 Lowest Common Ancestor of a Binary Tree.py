class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.depthOfQ = 0
        self.depthOfP = 0
        self.nodeToParent = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.depthOfP = 0
        self.depthOfQ = 0
        self.nodeToParent = {}
        self.dfs(root, p, q, 0)
        # make p always the node with bigger depth
        if self.depthOfP < self.depthOfQ:
            self.depthOfP, self.depthOfQ = self.depthOfQ, self.depthOfP
            p, q = q, p

        while self.depthOfP > self.depthOfQ:
            p = self.nodeToParent[p]
            self.depthOfP -= 1

        todo = {p, q}
        while len(todo) > 1:
            nextTodo = set()
            for node in todo:
                nextTodo.add(self.nodeToParent[node])
            todo = nextTodo

        return list(todo)[0]

    def dfs(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode', depth: int):
        if node == p:
            self.depthOfP = depth
        if node == q:
            self.depthOfQ = depth

        if node.left:
            self.nodeToParent[node.left] = node
            self.dfs(node.left, p, q, depth + 1)
        if node.right:
            self.nodeToParent[node.right] = node
            self.dfs(node.right, p, q, depth + 1)
