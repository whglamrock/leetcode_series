from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            medium = (l + r) // 2
            if l == r:
                if self.canMakeMBouquets(bloomDay, m, k, medium):
                    return medium
                return -1

            if self.canMakeMBouquets(bloomDay, m, k, medium):
                r = medium
            else:
                l = medium + 1

        return -1

    def canMakeMBouquets(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        currFlowers = 0
        count = 0
        for dayToBloom in bloomDay:
            if dayToBloom <= day:
                currFlowers += 1
            else:
                currFlowers = 0

            if currFlowers == k:
                count += 1
                currFlowers = 0

        return count >= m
