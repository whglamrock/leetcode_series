from collections import defaultdict
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        nodeToParents = defaultdict(set)
        for i, j in edges:
            nodeToParents[j].add(i)

        ans = []
        for i in range(n):
            todo = {i}
            visited = set()
            while todo:
                nextTodo = set()
                for node in todo:
                    visited.add(node)
                    if node not in nodeToParents:
                        continue
                    for parent in nodeToParents[node]:
                        if parent not in visited:
                            nextTodo.add(parent)

                todo = nextTodo

            visited.discard(i)
            ans.append(sorted(visited))

        return ans
