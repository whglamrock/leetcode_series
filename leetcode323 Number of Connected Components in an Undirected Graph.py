
from collections import defaultdict, deque

# BFS O(N) solution, much easier to implement than UnionFind

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        numOfComponents = 0
        visited = set()
        for i in xrange(n):
            if i not in visited:
                numOfComponents += 1
                self.bfs(i, graph, visited)

        return numOfComponents

    def bfs(self, start, graph, visited):
        if start in visited:
            return

        q = deque()
        q.append(start)
        while q:
            i = q.popleft()
            if i in visited:
                continue
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    q.append(j)



print Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]])










