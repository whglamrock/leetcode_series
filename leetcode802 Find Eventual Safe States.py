from collections import defaultdict
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminalNodes = set()
        destination = defaultdict(set)
        origin = defaultdict(set)
        for i in range(len(graph)):
            if not graph[i]:
                terminalNodes.add(i)
                continue
            for j in graph[i]:
                destination[j].add(i)
                origin[i].add(j)

        safeNodes = set()
        todo = terminalNodes
        while todo:
            nextTodo = set()
            for node in todo:
                safeNodes.add(node)
                if node not in destination:
                    continue
                for originNode in destination[node]:
                    if originNode not in origin:
                        continue
                    origin[originNode].discard(node)
                    if not origin[originNode]:
                        del origin[originNode]
                        nextTodo.add(originNode)
                del destination[node]
            todo = nextTodo

        ans = []
        for i in range(len(graph)):
            if i in safeNodes:
                ans.append(i)
        return ans


print(Solution().eventualSafeNodes([[], [0, 2, 3, 4], [3], [4], []]))
print(Solution().eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
print(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
