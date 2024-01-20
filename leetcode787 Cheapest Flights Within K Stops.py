from collections import defaultdict
from heapq import *
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make k the number of flights you can take at most
        k += 1
        srcToDestToPrice = defaultdict(dict)
        for origin, destination, price in flights:
            srcToDestToPrice[origin][destination] = price

        pq = [[0, src, 0]]
        nodeToMinFlights = {}

        while pq:
            price, node, numOfFlights = heappop(pq)
            if node == dst:
                return price

            # already used up all available number of flights
            if numOfFlights >= k:
                continue

            # means we have visited this node with fewer flights AND CHEAPER PRICE because
            # the pq always pops out the next stop with the currently cheapest price
            if node in nodeToMinFlights and nodeToMinFlights[node] < numOfFlights:
                continue
            nodeToMinFlights[node] = numOfFlights

            if node not in srcToDestToPrice:
                continue
            for nextNode in srcToDestToPrice[node]:
                nextPrice = srcToDestToPrice[node][nextNode]
                heappush(pq, [price + nextPrice, nextNode, numOfFlights + 1])

        return -1

