from collections import defaultdict
from heapq import *
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        srcToDstToProb = defaultdict(dict)
        for i in range(len(edges)):
            src, dst = edges[i]
            srcToDstToProb[src][dst] = succProb[i]
            srcToDstToProb[dst][src] = succProb[i]

        pq = [[-1, start_node]]
        nodeToMaxProb = {}
        while pq:
            prob, node = heappop(pq)
            prob = -prob

            if node == end_node:
                return prob
            if node in nodeToMaxProb and nodeToMaxProb[node] > prob:
                continue
            nodeToMaxProb[node] = prob

            for nextNode in srcToDstToProb[node]:
                nextProb = prob * srcToDstToProb[node][nextNode]
                # pre-check and pre-add the nextNode to the visited map, to speed up the BFS
                if nextNode in nodeToMaxProb and nodeToMaxProb[nextNode] >= nextProb:
                    continue
                nodeToMaxProb[nextNode] = nextProb
                heappush(pq, [-nextProb, nextNode])

        return 0
