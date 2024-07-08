from collections import defaultdict
from typing import List


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.wordToIndexes = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.wordToIndexes[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        indexes1, indexes2 = self.wordToIndexes[word1], self.wordToIndexes[word2]
        if len(indexes1) > len(indexes2):
            indexes1, indexes2 = indexes2, indexes1

        shortestDist = 2147483647
        for target in indexes1:
            closestIndex = self.findClosest(indexes2, target)
            shortestDist = min(shortestDist, abs(closestIndex - target))

        return shortestDist

    def findClosest(self, nums: List[int], target: int) -> int:
        closestSmaller, closestBigger = -1, -1

        # go smaller
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if nums[m] <= target:
                    closestSmaller = nums[m]
                break
            if nums[m] <= target:
                l = m
            else:
                r = m - 1

        # go bigger
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] >= target:
                    closestBigger = nums[m]
                break
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        if closestSmaller == -1:
            return closestBigger
        if closestBigger == -1:
            return closestSmaller
        if target - closestSmaller <= closestBigger - target:
            return closestSmaller
        else:
            return closestBigger


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
