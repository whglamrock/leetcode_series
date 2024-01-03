from collections import defaultdict
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        busToStops = defaultdict(set)
        stopToBuses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                busToStops[i].add(stop)
                stopToBuses[stop].add(i)

        if source not in stopToBuses:
            return -1
        visitedBuses = set()
        visitedStops = {source}
        todo = {source}

        numOfBuses = 0
        while todo:
            if target in todo:
                return numOfBuses

            nextTodo = set()
            for stop in todo:
                visitedStops.add(stop)
                for bus in stopToBuses[stop]:
                    if bus in visitedBuses:
                        continue
                    visitedBuses.add(bus)
                    for nextStop in busToStops[bus]:
                        if nextStop not in visitedStops:
                            nextTodo.add(nextStop)
            todo = nextTodo
            numOfBuses += 1

        return -1


print(Solution().numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6))
print(Solution().numBusesToDestination(routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15, target=12))
