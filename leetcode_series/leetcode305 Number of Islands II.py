
# Intro to Union find: https://www.youtube.com/watch?v=ID00PMy0-vE&t=761s
# m, n are useless.

class Solution(object):
    def numIslands2(self, m, n, positions):

        ans = []
        island = Union()
        for position in positions:
            i, j = position
            island.add((i, j))
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newpo = (i + dir[0], j + dir[1])
                if newpo in island.id:
                    island.unite((i, j), newpo)
            ans.append(island.count)

        return ans


# the classic way of defining a Unionfind object

class Union(object):
    def __init__(self):

        self.id = {}    # a pointer that points to its parent
        self.sz = {}    # how many nodes are under a specific root
        self.count = 0

    def add(self, p):

        self.id[p] = p
        self.count += 1
        self.sz[p] = 1

    def root(self, i):

        while self.id[i] != i:
            self.id[i] = self.id[self.id[i]]    # path compression
            i = self.id[i]
        return i

    def unite(self, p, q):  # in the problem, p and q are presented as tuples.

        p = self.root(p)
        q = self.root(q)
        if p == q:
            return
        if self.sz[p] < self.sz[q]:
            p, q = q, p
        self.id[q] = p
        self.count -= 1
        # self.sz[q] doesn't matter anymore, because it's "the rank of non-root" node
        self.sz[p] += self.sz[q]
        # we don't delete the self.sz[p] here, because we need all
        # the intermediate self.id[x]s to find the untimate root, even
        # though we did the path comppression.

