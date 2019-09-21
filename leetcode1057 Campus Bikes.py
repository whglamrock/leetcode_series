
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        if not workers or not bikes:
            return []

        queue = []
        # n <= m
        m, n = len(bikes), len(workers)

        for i in xrange(n):  # i is the worker index
            for j in xrange(m):  # j is bike index
                distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                queue.append([distance, i, j])

        queue.sort()
        ans = [-1] * n
        usedBikes = set()

        for distance, i, j in queue:
            if ans[i] != -1 or j in usedBikes:
                continue
            ans[i] = j
            usedBikes.add(j)

        return ans



workers = [[0, 0], [1, 1], [2, 0]]
bikes = [[1, 0], [2, 2], [2, 1]]
print Solution().assignBikes(workers, bikes)




