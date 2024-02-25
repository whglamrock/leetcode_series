from heapq import *
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        locations = set()
        for numOfPassenger, origin, destination in trips:
            locations.add(origin)
            locations.add(destination)
        locations = sorted(locations)

        i = 0
        currLoad = 0
        pq = []
        for location in locations:
            # first, pop out the passengers that have arrived at their destinations
            while pq and pq[0][0] <= location:
                destination, numOfPassenger = heappop(pq)
                currLoad -= numOfPassenger

            # add the new passengers after dropping off the arrived passengers
            while i < len(trips) and trips[i][1] <= location:
                if currLoad + trips[i][0] > capacity:
                    return False
                currLoad += trips[i][0]
                heappush(pq, [trips[i][2], trips[i][0]])
                i += 1

        return True


print(Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))
print(Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))
