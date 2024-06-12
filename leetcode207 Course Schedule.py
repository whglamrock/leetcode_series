from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToDependents = defaultdict(set)
        courseToPrereqs = defaultdict(set)

        for i, j in prerequisites:
            courseToDependents[j].add(i)
            courseToPrereqs[i].add(j)

        todo = set()
        for course in range(numCourses):
            # this course can be taken rn
            if course not in courseToPrereqs:
                todo.add(course)

        visited = set()
        while todo:
            nextTodo = set()
            for course in todo:
                visited.add(course)
                if course in courseToDependents:
                    dependents = courseToDependents[course]
                    for dependent in dependents:
                        courseToPrereqs[dependent].discard(course)
                        if not courseToPrereqs[dependent]:
                            del courseToPrereqs[dependent]
                            nextTodo.add(dependent)
                    del courseToDependents[course]
            todo = nextTodo

        return len(visited) == numCourses


print(Solution().canFinish(2, [[1,0],[0,1]]))
print(Solution().canFinish(4, [[1,0],[2,1],[3,1],[3,0],[3,2]]))
