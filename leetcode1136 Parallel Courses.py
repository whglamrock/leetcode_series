from collections import defaultdict
from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        courseToPrerequisites = defaultdict(set)
        courseToDependents = defaultdict(set)
        for i, j in relations:
            courseToPrerequisites[j].add(i)
            courseToDependents[i].add(j)

        todo = set()
        for i in range(1, n + 1):
            if i not in courseToPrerequisites:
                todo.add(i)

        numOfSemesters = 0
        visited = set()
        while todo:
            nextTodo = set()
            for course in todo:
                visited.add(course)
                if course not in courseToDependents:
                    continue
                for dependentCourse in courseToDependents[course]:
                    courseToPrerequisites[dependentCourse].discard(course)
                    if not courseToPrerequisites[dependentCourse]:
                        nextTodo.add(dependentCourse)
                        del courseToPrerequisites[dependentCourse]
                del courseToDependents[course]
            todo = nextTodo
            numOfSemesters += 1

        return numOfSemesters if len(visited) == n else -1
