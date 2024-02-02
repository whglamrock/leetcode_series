from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseToPrerequisites, courseToDependents = defaultdict(set), defaultdict(set)
        for i, j in prerequisites:
            courseToPrerequisites[i].add(j)
            courseToDependents[j].add(i)

        todo = set()
        for i in range(numCourses):
            if i not in courseToPrerequisites:
                todo.add(i)

        ans = []
        visited = set()
        while todo:
            nextTodo = set()
            for course in todo:
                ans.append(course)
                visited.add(course)
                if course not in courseToDependents:
                    continue
                for dependentCourse in courseToDependents[course]:
                    if dependentCourse not in courseToPrerequisites:
                        continue
                    courseToPrerequisites[dependentCourse].discard(course)
                    if not courseToPrerequisites[dependentCourse]:
                        del courseToPrerequisites[dependentCourse]
                        nextTodo.add(dependentCourse)
                del courseToDependents[course]
            todo = nextTodo

        return ans if len(ans) == numCourses else []


print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution().findOrder(5, [[1, 0], [2, 0], [3, 1], [3, 2], [3, 4], [4, 2], [1, 2]]))
print(Solution().findOrder(5, [[1, 0], [2, 0], [3, 1], [3, 2], [3, 4], [4, 2], [1, 2], [2, 4]]))
