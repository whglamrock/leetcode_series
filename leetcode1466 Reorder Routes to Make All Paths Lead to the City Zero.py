from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        originToDestinations, destinationToOrigins = defaultdict(set), defaultdict(set)
        for i, j in connections:
            originToDestinations[i].add(j)
            destinationToOrigins[j].add(i)

        numOfReorder = 0
        prev = set()
        curr = {0}
        while curr:
            next = set()
            for city in curr:
                for nextCity in originToDestinations[city]:
                    if nextCity not in prev:
                        numOfReorder += 1
                        next.add(nextCity)
                for nextCity in destinationToOrigins[city]:
                    if nextCity not in prev:
                        next.add(nextCity)
            prev = curr
            curr = next

        return numOfReorder


print(Solution().minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(Solution().minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))
