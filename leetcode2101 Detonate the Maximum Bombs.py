from collections import defaultdict
from typing import List, Dict

# O(N ^ 2) solution with using visited set for bfs
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bombToConnectedBombs = defaultdict(set)
        for i, bomb1 in enumerate(bombs):
            for j, bomb2 in enumerate(bombs):
                if i == j:
                    continue
                if self.canFurtherDetonate(bomb1, bomb2):
                    bombToConnectedBombs[i].add(j)

        maxNumOfDetonation = 0
        for i in range(len(bombs)):
            maxNumOfDetonation = max(maxNumOfDetonation, self.bfs(i, bombToConnectedBombs))
        return maxNumOfDetonation

    def bfs(self, i: int, bombToConnectedBombs: Dict[int, set]) -> int:
        todo = {i}
        visited = set()
        numOfDetonated = 0
        while todo:
            nextTodo = set()
            for bomb in todo:
                visited.add(bomb)
                numOfDetonated += 1
                if bomb not in bombToConnectedBombs:
                    continue
                for nextBomb in bombToConnectedBombs[bomb]:
                    if nextBomb not in visited:
                        nextTodo.add(nextBomb)
                        visited.add(nextBomb)
            todo = nextTodo

        return numOfDetonated

    def canFurtherDetonate(self, bomb1: List[int], bomb2: List[int]) -> bool:
        return (bomb2[0] - bomb1[0]) ** 2 + (bomb2[1] - bomb1[1]) ** 2 <= bomb1[2] ** 2
