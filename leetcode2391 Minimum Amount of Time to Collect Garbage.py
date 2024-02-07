from collections import Counter
from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        totalTime = 0
        maxMetalIndex, maxPaperIndex, maxGarbageIndex = 0, 0, 0
        for i, trash in enumerate(garbage):
            charCount = Counter(trash)
            if 'M' in charCount:
                totalTime += charCount['M']
                maxMetalIndex = max(maxMetalIndex, i)
            if 'P' in trash:
                totalTime += charCount['P']
                maxPaperIndex = max(maxPaperIndex, i)
            if 'G' in trash:
                totalTime += charCount['G']
                maxGarbageIndex = max(maxGarbageIndex, i)

        if maxMetalIndex > 0:
            totalTime += sum(travel[:maxMetalIndex])
        if maxPaperIndex > 0:
            totalTime += sum(travel[:maxPaperIndex])
        if maxGarbageIndex > 0:
            totalTime += sum(travel[:maxGarbageIndex])

        return totalTime
