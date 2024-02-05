class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        depthOfP = self.findDepthOfNode(p)
        depthOfQ = self.findDepthOfNode(q)
        # make p the node with bigger depth
        if depthOfP < depthOfQ:
            p, q = q, p
            depthOfP, depthOfQ = depthOfQ, depthOfP
        while depthOfP > depthOfQ:
            p = p.parent
            depthOfP -= 1

        todo = {p, q}
        while len(todo) > 1:
            nextTodo = set()
            for node in todo:
                nextTodo.add(node.parent)
            todo = nextTodo

        return list(todo)[0]

    def findDepthOfNode(self, node: 'Node') -> int:
        depth = 0
        while node and node.parent:
            node = node.parent
            depth += 1
        return depth
