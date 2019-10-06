
from collections import defaultdict
from heapq import *

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        if not times:
            return -1

        q = [(0, K)]
        heapify(q)
        nodeToNeighborToTime = defaultdict(dict)
        nodeToTime = {}

        for u, v, t in times:
            nodeToNeighborToTime[u][v] = t

        while q:
            lastTime, node = heappop(q)
            if node not in nodeToTime:
                nodeToTime[node] = lastTime
                for child in nodeToNeighborToTime[node]:
                    heappush(q, (nodeToNeighborToTime[node][child] + lastTime, child))

        return max(nodeToTime.values()) if len(nodeToTime) == N else -1



print Solution().networkDelayTime([[2, 1, 1], [2, 3, 3], [1, 3, 1], [1, 4, 5], [3, 4, 1], [3, 5, 2], [4, 5, 1]], 5, 2)
