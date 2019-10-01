
# Typical union find solution. remember the find() and union() methods

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 0:
            return False
        if not edges:
            return n <= 1

        # the path compression will make sure if two nodes are in the same union, the find() will output the same parent
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # when we union 2 parts(each part contains a bunch of nodes) of the tree, the following line won't
                # update all parents of x set to find(y);
            # i.e., it will only compress the path in x set first then do the union
            parent[find(x)] = find(y)

        parent = range(n)
        for i, j in edges:
            x = find(i)
            y = find(j)
            # circle exists
            if x == y:
                return False
            union(i, j)
            # print parent

        return len(edges) == n - 1

