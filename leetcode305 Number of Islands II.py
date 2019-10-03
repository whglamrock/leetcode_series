
# remember how the find() & union() helper methods are used in 2D condition.
# Time complexity O(k * log(m * n)) where k == len(positions). It's mathematically proved that with path compression
    # union() and find() both take O(log(m * n))

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not positions:
            return []

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            parent[find(node1)] = find(node2)

        parent = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        numOfIslands = 0
        ans = []

        for i, j in positions:
            if (i, j) in parent:  # leetcode does give this stupid test case
                ans.append(numOfIslands)
                continue

            # find all the connected islands(if exists)
            islandSet = set()
            for x, y in directions:
                if (i + x, j + y) in parent:
                    islandSet.add(find((i + x, j + y)))

            # modify the numOfIslands and append it to ans
            numOfIslands -= len(islandSet)
            numOfIslands += 1
            ans.append(numOfIslands)

            # union the connected islands
            islands = list(islandSet)
            for k in xrange(len(islands) - 1):
                union(islands[k], islands[k + 1])

            # make sure parent[(i, j)] is also up to date
            if islands:
                # not directly islands[0] because it could have changed with the union() method
                parent[(i, j)] = find(islands[0])
            else:
                parent[(i, j)] = (i, j)

        return ans



print Solution().numIslands2(4, 4, [[0, 1], [0, 2], [1, 1], [1, 3], [2, 2], [3, 2], [1, 2]])
print Solution().numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])