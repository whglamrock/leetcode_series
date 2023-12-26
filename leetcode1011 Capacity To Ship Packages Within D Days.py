from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        minCap = r
        while l <= r:
            capacity = (l + r) // 2
            if self.isCapacityEnough(weights, days, capacity):
                r = capacity
                minCap = min(minCap, capacity)
                if l == r:
                    break
            else:
                l = capacity + 1

        return minCap

    def isCapacityEnough(self, weights: List[int], days: int, capacity: int) -> bool:
        curr = 0
        daysPassed = 0
        for weight in weights:
            if curr + weight > capacity:
                if daysPassed >= days:
                    return False
                curr = weight
                daysPassed += 1
            else:
                curr += weight

        daysPassed += 1
        return daysPassed <= days


print(Solution().shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
print(Solution().shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
