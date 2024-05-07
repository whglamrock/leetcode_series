from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = sum(aliceSizes) - sum(bobSizes)
        aliceSizes, bobSizes = set(aliceSizes), set(bobSizes)
        for aliceSize in aliceSizes:
            if aliceSize - diff // 2 in bobSizes:
                return [aliceSize, aliceSize - diff // 2]

        return [-1, -1]
