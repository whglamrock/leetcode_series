# O(N * logN) solution where N = len(edges).

# For explanation, see: https://leetcode.com/problems/redundant-connection-ii/discuss/108045/C%2B%2BJava-Union-Find
# -with-explanation-O(n) One important thing not hard to notice: if a node has 2 parents, one of the 2 edges has to
# be removed. Then solution will basically be divided into 2 conditions: such node exists or not. Either ways the
# circle exists because we have an extra edge. The tricky part is actually when there is a node with 2 parents,
# in which case we can't directly perform union find (we don't know which of the 2 parents we should put in the
# parent array). So we need to "remove" an edge to unblock union find/circle lookup, then we know whether we made the
# right move

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []

        n = len(edges)
        candidate1, candidate2 = None, None
        parent = [0] * (n + 1)

        for k in range(n):
            i, j = edges[k]
            if parent[j] == 0:
                parent[j] = i
            else:
                # cannot directly return [i, j] here because we don't know which one of candidate1/2 is redundant
                candidate1 = [i, j]
                candidate2 = [parent[j], j]
                # "remove" this edge; then use union find to see if the graph becomes a valid tree
                edges[k][1] = 0

        def find(x):
            # path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = range(n + 1)
        for i, j in edges:
            # if this happens then we did find a node with 2 parents and this is the "removed" edge
            if j == 0:
                continue
            x, y = find(i), find(j)
            # circle exists
            if x == y:
                # if candidate1/2 != None then we removed a wrong edge; if candidate1/2 == None then there was no
                # node with 2 parents, so we just need to remove an edge in circle
                return candidate2 if candidate2 else [i, j]
            union(i, j)

        return candidate1


print(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
print(Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))
