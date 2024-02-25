from collections import defaultdict
from typing import List

# remember: when we bfs, do it from a single unvisited node. Starting from all non hated people can get us wrong result.
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        peopleToEnemy = defaultdict(set)
        for i, j in dislikes:
            peopleToEnemy[i].add(j)
            peopleToEnemy[j].add(i)

        # group 1 or 2
        peopleToGroup = {}
        for people in range(1, n + 1):
            if people in peopleToGroup:
                continue

            # if the graph is disconnected, for each disconnected part
            # we don't really care which initial group we assign
            todo = [[people, 1]]
            peopleToGroup[people] = 1
            while todo:
                nextTodo = []
                for currPpl, group in todo:
                    for enemy in peopleToEnemy[currPpl]:
                        if enemy not in peopleToGroup:
                            peopleToGroup[enemy] = 3 - group
                            nextTodo.append([enemy, 3 - group])
                        elif peopleToGroup[enemy] == peopleToGroup[currPpl]:
                            return False
                todo = nextTodo

        return True
