from collections import defaultdict
from heapq import *
from typing import List

# O(N * log(N) + O(E)) solution, where N is number of courses, and E is the number of relationships (edges)
# The leetcode solution uses Kahn's algorithm to achieve O(N + E) time but it's not really necessary. Below solution
# is really the most practical solution to come up with in real interview without knowing a rarely known algorithm.
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        courseToPrerequisites, courseToDependents = defaultdict(set), defaultdict(set)
        for i, j in relations:
            courseToPrerequisites[j].add(i)
            courseToDependents[i].add(j)

        pq = []
        for course in range(1, n + 1):
            if course not in courseToPrerequisites:
                heappush(pq, [time[course - 1], course])

        currTime = 0
        while pq:
            finishTime, course = heappop(pq)
            currTime = max(currTime, finishTime)
            if course not in courseToDependents:
                continue
            for dependentCourse in courseToDependents[course]:
                if dependentCourse not in courseToPrerequisites:
                    continue
                courseToPrerequisites[dependentCourse].discard(course)
                if not courseToPrerequisites[dependentCourse]:
                    del courseToPrerequisites[dependentCourse]
                    heappush(pq, [finishTime + time[dependentCourse - 1], dependentCourse])
            del courseToDependents[course]

        return currTime
