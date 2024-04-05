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
