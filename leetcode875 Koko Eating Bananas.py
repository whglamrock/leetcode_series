from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        sumOfPiles = sum(piles)
        minSpeedNeededToFinishInH = sumOfPiles // h + 1 if sumOfPiles % h != 0 else sumOfPiles // h
        l, r = min(maxPile, minSpeedNeededToFinishInH), max(maxPile, minSpeedNeededToFinishInH)

        minSpeed = max(l, r)
        while l < r:
            speed = (l + r) // 2
            if self.canFinishWithSpeed(piles, h, speed):
                r = speed
                minSpeed = min(minSpeed, speed)
            else:
                l = speed + 1

        if l == r:
            minSpeed = l

        return minSpeed

    def canFinishWithSpeed(self, piles: List[int], h: int, speed: int) -> bool:
        hoursNeeded = 0
        for pile in piles:
            if pile % speed == 0:
                hoursNeeded += pile // speed
            else:
                hoursNeeded += pile // speed + 1
        return hoursNeeded <= h


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
print(Solution().minEatingSpeed(piles=[1000000000], h=2))
