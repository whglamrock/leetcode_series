from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bedLen = len(flowerbed)
        for i in range(bedLen):
            if flowerbed[i] == 1 or (i > 0 and flowerbed[i - 1] == 1) or (i + 1 < bedLen and flowerbed[i + 1] == 1):
                continue
            flowerbed[i] = 1
            n -= 1

        return n <= 0


print(Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
