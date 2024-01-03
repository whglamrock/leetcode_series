from collections import defaultdict
from typing import List, Dict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        components = []
        visited = set()

        for i in range(1, n + 1):
            if i in visited:
                continue

            # do bfs to find connected components
            currLevel = {i}
            visitedInBfs = {i}
            while currLevel:
                nextLevel = set()
                for node in currLevel:
                    for connectedNode in graph[node]:
                        if connectedNode in visitedInBfs:
                            continue
                        visitedInBfs.add(connectedNode)
                        nextLevel.add(connectedNode)
                currLevel = nextLevel
            components.append(visitedInBfs)
            visited = visited.union(visitedInBfs)

        longest = [-1] * len(components)
        for i, component in enumerate(components):
            for node in component:
                longest[i] = max(longest[i], self.bfs(graph, node))
        if min(longest) < 0:
            return -1
        return sum(longest)

    def bfs(self, graph: Dict[int, List[int]], i: int):
        currLevel = {i}
        visited = {i}
        numOfGroups = 0

        while currLevel:
            numOfGroups += 1
            nextLevel = set()
            for node in currLevel:
                for connectedNode in graph[node]:
                    # 1. checks against cycle first before checking against visited
                    # 2. if the node we wanna add to the next level exists in level - 1 it means this bfs doesn't work
                    # 3. this also find out the cycle with odd length
                    if connectedNode in currLevel:
                        return -1
                    if connectedNode in visited:
                        continue
                    visited.add(connectedNode)
                    nextLevel.add(connectedNode)
            currLevel = nextLevel

        return numOfGroups


print(Solution().magnificentSets(n=6, edges=[[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]))
print(Solution().magnificentSets(n=3, edges=[[1, 2], [2, 3], [3, 1]]))
