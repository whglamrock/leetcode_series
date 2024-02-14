from collections import defaultdict
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodeToChildren = defaultdict(set)
        for i, directManager in enumerate(manager):
            if directManager == -1:
                continue
            nodeToChildren[directManager].add(i)

        # bfs
        maxMinutes = 0
        todo = [[headID, 0]]
        while todo:
            nextTodo = []
            for node, currTime in todo:
                maxMinutes = max(maxMinutes, currTime)
                if node not in nodeToChildren:
                    continue
                for child in nodeToChildren[node]:
                    nextTodo.append([child, currTime + informTime[node]])
            todo = nextTodo

        return maxMinutes
