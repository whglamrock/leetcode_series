from collections import defaultdict
from copy import deepcopy
from typing import List, Dict

# Below solution actually gets TLE in the stupid leetcode. The "binary lift" or "lowest common ancestor" algorithm
# is just way too fucking meaningless for an interview.
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        edgeToWeight = {}
        for u, v, weight in edges:
            graph[u].add(v)
            graph[v].add(u)
            edgeToWeight[(min(u, v), max(u, v))] = weight

        ans = []
        for start, end in queries:
            if start == end:
                ans.append(0)
                continue

            minOperations = 2147483647
            weightCounts = self.bfs(start, end, graph, edgeToWeight)
            for weightCount in weightCounts:
                numOfOperations = sum(weightCount.values()) - max(weightCount.values())
                minOperations = min(minOperations, numOfOperations)
            if minOperations != 2147483647:
                ans.append(minOperations)
            else:
                ans.append(0)

        return ans

    # return the weight count in the path. You can add an @lru_cache(None) here to optimize but
    # it doesn't matter since the stupid leetcode still gives TLE
    def bfs(self, start: int, end: int, graph: Dict[int, set], edgeToWeight: Dict[tuple, int]) -> List[Dict[int, int]]:
        weightCounts = []
        todo = [[start, defaultdict(int)]]
        visited = set()
        while todo:
            nextTodo = []
            for node, currWeightCount in todo:
                if node in visited or node not in graph:
                    continue
                if node == end:
                    weightCounts.append(currWeightCount)
                    continue
                visited.add(node)
                for nextNode in graph[node]:
                    weight = edgeToWeight[(min(node, nextNode), max(node, nextNode))]
                    nextWeightCount = deepcopy(currWeightCount)
                    nextWeightCount[weight] += 1
                    nextTodo.append([nextNode, nextWeightCount])
            todo = nextTodo

        return weightCounts
