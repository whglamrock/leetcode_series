
from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # trees[i] contains all nodes connected to i; the value can also be list because we only have N - 1 edges
        self.trees = defaultdict(set)
        # count[i] counts the num of nodes in the subtree[i], note that we assume 0 as root
        self.count = [1] * N
        # the answer we needa return
        self.res = [0] * N
        self.N = N

        for i, j in edges:
            self.trees[i].add(j)
            self.trees[j].add(i)

        self.dfs1(0, -1)
        self.dfs2(0, -1)
        return self.res

    # in the first dfs, we can update both the self.count and self.res
    # after this round of dfs, only self.res[0] will be same as the final answer
        # and all the rest of the self.res[i] will be the sum of distance to its sub-nodes
    def dfs1(self, root, prev):
        for i in self.trees[root]:
            if i != prev:
                self.dfs1(i, root)
                self.count[root] += self.count[i]
                # the count[i] is the extra distance sum caused by from root to i
                self.res[root] += self.res[i] + self.count[i]

    # only update the self.res
    def dfs2(self, root, prev):
        for i in self.trees[root]:
            if i != prev:
                # res[root] - count[i] is the sum of distance from i to all its subtrees + the sum of distance from
                    # root to root's non-i subtrees
                # the raw form of the following line is res[i] += (res[root] - count[i] - res[i]) + (N - count[i])
                self.res[i] = (self.res[root] - self.count[i]) + (self.N - self.count[i])
                self.dfs2(i, root)



N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print Solution().sumOfDistancesInTree(N, edges)



