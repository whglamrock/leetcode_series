from collections import defaultdict
from typing import Dict, List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(dict)
        for fromCity, toCity, dist in edges:
            graph[fromCity][toCity] = dist
            graph[toCity][fromCity] = dist

        cityToNumOfNeighborCities = {}
        for i in range(n):
            neighborCities = self.bfs(graph, i, distanceThreshold)
            cityToNumOfNeighborCities[i] = len(neighborCities)

        minNumOfNeighborCities = min(cityToNumOfNeighborCities.values())
        ans = -1
        for i in range(n):
            if cityToNumOfNeighborCities[i] == minNumOfNeighborCities:
                ans = i

        return ans

    def bfs(self, graph: Dict[int, Dict[int, int]], startCity: int, distanceThreshold: int) -> set:
        todo = {(startCity, 0)}
        neighborCities = set()
        # we need this instead of a visited set to avoid missing some neighbor cities that require extra hops but shorter distance
        cityToMinDist = {}
        while todo:
            nextTodo = set()
            for city, currDist in todo:
                neighborCities.add(city)
                cityToMinDist[city] = currDist

                if city not in graph or currDist >= distanceThreshold:
                    continue

                for nextCity in graph[city]:
                    nextDist = currDist + graph[city][nextCity]
                    if nextDist > distanceThreshold or (
                            nextCity in cityToMinDist and cityToMinDist[nextCity] <= nextDist):
                        continue
                    nextTodo.add((nextCity, nextDist))
                    cityToMinDist[nextCity] = nextDist

            todo = nextTodo

        neighborCities.discard(startCity)
        return neighborCities
