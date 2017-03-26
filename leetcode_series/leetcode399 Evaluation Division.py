
# DFS solution.

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(set)
        valuegraph = {}
        for i, equation in enumerate(equations):
            a, b = equation
            graph[a].add(b)
            graph[b].add(a)
            valuegraph[(a, b)] = values[i]
            valuegraph[(b, a)] = float(1) / values[i]

        # last is the last hop in the path; visited stores the current partial path;
        # cur is accumulated mutiplier
        def dfs(graph, last, end, visited, cur):
            if end in graph[last]:
                return cur * valuegraph[(last, end)]
            ans = None
            for next in graph[last]:
                if next not in visited:
                    ans = dfs(graph, next, end, visited | {next}, cur * valuegraph[(last, next)])
                    if ans: return ans

        ans = []
        for query in queries:
            s, e = query
            div = dfs(graph, s, e, {s}, 1)
            if not div:
                ans.append(-1.0)
            else:
                ans.append(div)

        return ans