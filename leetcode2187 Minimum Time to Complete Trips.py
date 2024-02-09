from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, max(time) * totalTrips
        while l <= r:
            m = (l + r) // 2
            if l == r:
                return l
            if self.canCompleteTripsInTime(time, totalTrips, m):
                r = m
            else:
                l = m + 1

        return l

    def canCompleteTripsInTime(self, time: List[int], totalTrips: int, targetTime: int) -> bool:
        tripsCompleted = 0
        for timeOfBus in time:
            tripsCompleted += targetTime // timeOfBus
        return tripsCompleted >= totalTrips
