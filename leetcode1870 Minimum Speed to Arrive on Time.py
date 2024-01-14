from math import ceil
from typing import List

# pay attention to edge cases (refer to the written test cases at the bottom).
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        minSpeed = max(sum(dist) // hour, 1)
        if hour <= len(dist) - 1:
            return -1
        maxSpeed = max(max(dist), ceil(dist[-1] / (hour - len(dist) + 1)))

        l, r = minSpeed, maxSpeed
        while l <= r:
            if l == r:
                return int(l)
            m = (l + r) // 2
            if self.canFinishWithSpeed(dist, hour, m):
                r = m
            else:
                l = m + 1

        return -1

    def canFinishWithSpeed(self, dist: List[int], hour: float, speed: int) -> bool:
        time = 0
        for i in range(len(dist) - 1):
            distance = dist[i]
            time += ceil(distance / speed)
        time += dist[-1] / speed
        return time <= hour


print(Solution().minSpeedOnTime([2, 1, 5, 4, 4, 3, 2, 9, 2, 10], 75.12))
print(Solution().minSpeedOnTime([1, 1, 100000], 2.01))
print(Solution().minSpeedOnTime([1, 3, 2], 6))
print(Solution().minSpeedOnTime([1, 3, 2], 1.9))
print(Solution().minSpeedOnTime([1, 3, 2], 2.7))
