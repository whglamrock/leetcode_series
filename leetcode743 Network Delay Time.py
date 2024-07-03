from collections import defaultdict
from heapq import *
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        srcToDstToTime = defaultdict(dict)
        for src, dst, time in times:
            srcToDstToTime[src][dst] = time

        pq = [[0, k]]
        nodeToMinTime = {}
        while pq:
            currTime, node = heappop(pq)
            # Below if condition is important: think of case like [[1, 2, 1], [2, 3, 2], [1, 3, 4]].
            # if you print the pq, pq at some point will be [[3, 3], [4, 3]] so we can't just blindly
            # reset the nodeToMinTime here.
            if node in nodeToMinTime and nodeToMinTime[node] < currTime:
                continue
            nodeToMinTime[node] = currTime

            if node not in srcToDstToTime:
                continue
            for nextNode in srcToDstToTime[node]:
                nextTime = currTime + srcToDstToTime[node][nextNode]
                # pre-check to speed up the BFS. Pay attention here we need to use "<=" not "<" to avoid TLE
                if nextNode in nodeToMinTime and nodeToMinTime[nextNode] <= nextTime:
                    continue
                nodeToMinTime[nextNode] = nextTime
                heappush(pq, [nextTime, nextNode])

        return max(nodeToMinTime.values()) if len(nodeToMinTime) == n else -1
