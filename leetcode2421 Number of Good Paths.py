from collections import defaultdict
from typing import List, Dict

# Below O(N ^ 2) solution is definitely acceptable in real interview but got TLE in the stupid leetcode.
# It seems leetcode is strictly looking for union find solutions (for more, see: https://leetcode.com/problems/number-of-good-paths/solutions/2620680/python-union-find-solution/).
class Solution:
    def __init__(self):
        self.ans = 0

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        valueToNodes = defaultdict(set)
        for i, val in enumerate(vals):
            valueToNodes[val].add(i)

        self.ans = 0
        for value in sorted(set(vals), reverse=True):
            self.bfsCountPath(graph, valueToNodes, value)
            self.cutNodesWithValue(graph, valueToNodes, value)

        return self.ans + len(vals)

    # O(N) for cutting the nodes with value
    def cutNodesWithValue(self, graph: Dict[int, set], valueToNodes: Dict[int, set], value: int):
        for node in valueToNodes[value]:
            if node not in graph:
                continue
            for connectedNode in graph[node]:
                if connectedNode not in graph:
                    continue
                graph[connectedNode].discard(node)
                if not graph[connectedNode]:
                    del graph[connectedNode]
            del graph[node]

    # O(N) for bfs. The graph may be disconnected: we find the number of connected nodes with current value
    # there can be multiple such connected groups, and we count the size of each group
    def bfsCountPath(self, graph: Dict[int, set], valueToNodes: Dict[int, set], value: int):
        visited = set()
        for node in valueToNodes[value]:
            if node in visited:
                continue
            todo = {node}
            count = 0
            while todo:
                nextTodo = set()
                for currNode in todo:
                    visited.add(currNode)
                    if currNode in valueToNodes[value]:
                        count += 1
                    if currNode not in graph:
                        continue
                    for nextNode in graph[currNode]:
                        if nextNode not in visited:
                            nextTodo.add(nextNode)
                todo = nextTodo

            self.ans += count * (count - 1) // 2
