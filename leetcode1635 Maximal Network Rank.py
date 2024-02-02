from collections import defaultdict
from typing import List

# Why we cannot achieve O(n): https://leetcode.com/problems/maximal-network-rank/solutions/889404/edge-count-attempt-to-o-n/
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cityToConnectedCities = defaultdict(set)
        for i, j in roads:
            cityToConnectedCities[i].add(j)
            cityToConnectedCities[j].add(i)

        maxRank = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                rank = len(cityToConnectedCities[i]) + len(cityToConnectedCities[j])
                if j in cityToConnectedCities[i]:
                    rank -= 1
                maxRank = max(maxRank, rank)

        return maxRank
