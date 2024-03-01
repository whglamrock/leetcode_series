from collections import defaultdict
from heapq import *
from typing import List

# minium spanning tree (prim's algorithm) problem, rarely see in an interview. See: https://leetcode.com/problems/min-cost-to-connect-all-points/solutions/843995/python-3-min-spanning-tree-prim-s-algorithm/
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(set)
        indexPairToDist = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                graph[i].add(j)
                graph[j].add(i)
                indexPairToDist[(i, j)] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        startingNode = 0
        pq = []
        for connectedNode in graph[startingNode]:
            indexPair = (min(startingNode, connectedNode), max(startingNode, connectedNode))
            heappush(pq, [indexPairToDist[indexPair], startingNode, connectedNode])
        if not pq:
            return 0

        visited = {startingNode}
        ans = 0
        while len(visited) < n:
            dist, node, connectedNode = heappop(pq)
            if connectedNode in visited:
                continue
            visited.add(connectedNode)
            ans += dist
            if node in graph:
                graph[node].discard(connectedNode)
                if not graph[node]:
                    del graph[node]
            if connectedNode in graph:
                graph[connectedNode].discard(node)
                if not graph[connectedNode]:
                    del graph[connectedNode]
                for nextConnectedNode in graph[connectedNode]:
                    if nextConnectedNode in visited:
                        continue
                    indexPair = (min(connectedNode, nextConnectedNode), max(connectedNode, nextConnectedNode))
                    nextDist = indexPairToDist[indexPair]
                    heappush(pq, [nextDist, connectedNode, nextConnectedNode])

        return ans
