class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.maxDiameter = 0
        self.dfs(root)
        return max(self.maxDiameter - 1, 0)

    def dfs(self, node: 'Node') -> int:
        if not node.children:
            return 1

        depthsFromChildren = []
        for child in node.children:
            depthsFromChildren.append(self.dfs(child))

        maxDepth, secondMaxDepth = 0, 0
        for depth in depthsFromChildren:
            if depth > maxDepth:
                secondMaxDepth = maxDepth
                maxDepth = depth
            elif depth > secondMaxDepth:
                secondMaxDepth = depth

        self.maxDiameter = max(self.maxDiameter, maxDepth + 1 + secondMaxDepth)
        return max(maxDepth, secondMaxDepth) + 1
