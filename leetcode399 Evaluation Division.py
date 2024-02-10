from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        strToStrToValue = defaultdict(dict)
        for i in range(len(equations)):
            strToStrToValue[equations[i][0]][equations[i][1]] = values[i]
            strToStrToValue[equations[i][1]][equations[i][0]] = 1 / values[i]

        # bfs
        ans = []
        for start, end in queries:
            if start not in strToStrToValue:
                ans.append(-1.0)
                continue

            todo = {(start, 1.0)}
            visited = set()
            foundAnswer = False
            while todo:
                if foundAnswer:
                    break
                nextTodo = set()
                for string, value in todo:
                    visited.add(string)
                    if string == end:
                        ans.append(value)
                        foundAnswer = True
                        break
                    if string not in strToStrToValue:
                        continue
                    for nextString in strToStrToValue[string]:
                        if nextString not in visited:
                            nextTodo.add((nextString, value * strToStrToValue[string][nextString]))
                todo = nextTodo

            if not foundAnswer:
                ans.append(-1.0)

        return ans


equations = [["a", "b"], ["e", "f"], ["b", "e"]]
values = [3.4, 1.4, 2.3]
queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
print(Solution().calcEquation(equations, values, queries))
