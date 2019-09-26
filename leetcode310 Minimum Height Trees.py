
# O(N) running time/space solution.
# See idea explanation: https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts

from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        leaves = [i for i in xrange(n) if len(graph[i]) == 1]

        # the number of MHT roots is either 1 or 2, no matter how many longest paths exist
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                for j in graph[i]:
                    graph[j].discard(i)
                    if len(graph[j]) == 1:
                        newLeaves.append(j)
                del graph[i]
            leaves = newLeaves

        return leaves