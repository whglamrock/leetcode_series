
# Intro to UnionFind find: https://www.youtube.com/watch?v=ID00PMy0-vE&t=761s
# A naive solution takes O(K * log(M * N)) time complexity, which satisfies the interview standard. But in real
    # interview it would be nice to mention that with proper "union by rank & path compression"
    # each union operation can take amortized O(log(M * N))

class Solution(object):
    def numIslands2(self, m, n, positions):

        ans = []
        island = UnionFind()
        for position in positions:
            i, j = position
            island.add((i, j))
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newpo = (i + dir[0], j + dir[1])
                if newpo in island.parent:
                    island.union((i, j), newpo)
            ans.append(island.count)

        return ans



# the classic way of defining a UnionFind object

class UnionFind(object):
    def __init__(self):

        self.parent = {}
        # how many nodes are under a specific findParent
        self.nodeToNumOfChildren = {}
        self.count = 0

    def add(self, p):

        self.parent[p] = p
        self.count += 1
        self.nodeToNumOfChildren[p] = 1

    def findParent(self, i):

        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]    # path compression
            i = self.parent[i]
        return i

    def union(self, p, q):  # in the problem, p and q are presented as tuples.

        p = self.findParent(p)
        q = self.findParent(q)
        if p == q:
            return
        if self.nodeToNumOfChildren[p] < self.nodeToNumOfChildren[q]:
            p, q = q, p
        self.parent[q] = p
        self.count -= 1
        # self.nodeToNumOfChildren[q] doesn't matter anymore, because it's "the rank of non-findParent" node
        self.nodeToNumOfChildren[p] += self.nodeToNumOfChildren[q]
        # we don't delete the self.nodeToNumOfChildren[p] here, because we need all
        # the intermediate self.parent[x]s to find the ultimate findParent, even
        # though we did the path compression.

