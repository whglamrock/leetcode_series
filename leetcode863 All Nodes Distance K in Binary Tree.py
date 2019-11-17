
from collections import defaultdict

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# consider the tree as a bi-directional graph is easiest way
# O(N) time complexity where N == number of nodes

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root:
            return []
        if k == 0:
            return [target.val]

        graph = defaultdict(set)
        self.buildGraph(root, graph)

        ans = []
        self.dfs(target, graph, set(), 0, k, ans)
        return ans

    def dfs(self, node, graph, visited, distance, k, ans):
        visited.add(node)
        if distance == k:
            ans.append(node.val)
            return
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, graph, visited, distance + 1, k, ans)

    def buildGraph(self, node, graph):
        if node.left:
            graph[node.left].add(node)
            graph[node].add(node.left)
            self.buildGraph(node.left, graph)
        if node.right:
            graph[node.right].add(node)
            graph[node].add(node.right)
            self.buildGraph(node.right, graph)
