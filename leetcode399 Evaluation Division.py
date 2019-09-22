
from collections import defaultdict

# "union find" alike graph solution. Basically build every possible connections

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not queries:
            return []
        if not equations:
            return [-1.0] * len(queries)

        # taking a / b = 2.0, b / c = 3.0 as example, graph is something like
            # {a: {a: 1, b: 2, c: 6}, b: {a: 0.5, b: 1, c: 3}, c: {a: 0.167, b: 0.333, c: 1}}
        graph = defaultdict(dict)

        for i in xrange(len(equations)):
            dividend, divisor = equations[i][0], equations[i][1]
            value = values[i]

            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

            graph[dividend][dividend] = 1.0
            graph[divisor][divisor] = 1.0

            # need a copy of the keys otherwise python dict won't allow dict size change in the for loop
            dividend_neighbors = graph[dividend].keys()
            divisor_neighbors = graph[divisor].keys()

            for x in dividend_neighbors:
                for y in divisor_neighbors:
                    graph[x][y] = graph[x][dividend] * graph[dividend][divisor] * graph[divisor][y]
                    graph[y][x] = graph[y][divisor] * graph[divisor][dividend] * graph[dividend][x]

        # print graph
        ans = [-1.0] * len(queries)
        for i in xrange(len(queries)):
            dividend, divisor = queries[i]
            if dividend in graph and divisor in graph[dividend]:
                ans[i] = graph[dividend][divisor]

        return ans



equations = [["a", "b"], ["e", "f"], ["b", "e"]]
values = [3.4, 1.4, 2.3]
queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
print Solution().calcEquation(equations, values, queries)