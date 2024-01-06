from collections import defaultdict
from functools import lru_cache
from typing import List, Dict

# O(m * n) solution where n == len(quiet) and m == len(richer)
class Solution:
    def __init__(self):
        self.peopleToRicher = defaultdict(set)

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        self.peopleToRicher = defaultdict(set)
        for item in richer:
            rich, poor = item[0], item[1]
            self.peopleToRicher[poor].add(rich)

        peopleToQuietness = {}
        for i, quietness in enumerate(quiet):
            peopleToQuietness[i] = quietness

        ans = []
        for i in range(len(quiet)):
            richerPeople = self.dfsToFindAllRicher(i)
            leastQuietRicherPeople = self.findLeastQuietFromRicher(richerPeople, peopleToQuietness)
            ans.append(leastQuietRicherPeople)

        return ans

    def findLeastQuietFromRicher(self, richerPeople: set, peopleToQuietness: Dict[int, int]) -> int:
        minQuietness = 2147483647
        leastQuietPeople = None
        for people in richerPeople:
            queitness = peopleToQuietness[people]
            if leastQuietPeople is None or queitness <= minQuietness:
                minQuietness = queitness
                leastQuietPeople = people
        return leastQuietPeople

    @lru_cache(None)
    def dfsToFindAllRicher(self, start: int) -> set:
        richerPeople = set()
        todo = {start}
        while todo:
            nextTodo = set()
            for people in todo:
                if people in richerPeople:
                    continue
                richerPeople.add(people)
                for rich in self.peopleToRicher[people]:
                    if rich not in richerPeople:
                        nextTodo.add(rich)
            todo = nextTodo

        return richerPeople


print(Solution().loudAndRich(richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                             quiet=[3, 2, 5, 4, 6, 1, 7, 0]))
print(Solution().loudAndRich(richer=[], quiet=[0]))
