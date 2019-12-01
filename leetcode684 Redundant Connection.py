
# a perfect, textbook union find question

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        n = len(edges)
        parent = range(n + 1)
        for i, j in edges:
            x = find(i)
            y = find(j)
            if x == y:
                return [i, j]
            union(i, j)