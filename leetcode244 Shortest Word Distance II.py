from collections import defaultdict
from typing import List


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.wordToIndexes = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.wordToIndexes[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # always make word2 has more indexes
        if len(self.wordToIndexes[word1]) > len(self.wordToIndexes[word2]):
            word1, word2 = word2, word1

        indexesOfWord2 = self.wordToIndexes[word2]
        minDistance = 2147483647
        for index1 in self.wordToIndexes[word1]:
            closestSmaller = self.findClosestSmaller(indexesOfWord2, index1)
            closestBigger = self.findClosestBigger(indexesOfWord2, index1)
            if closestSmaller != -1:
                minDistance = min(minDistance, index1 - closestSmaller)
            if closestBigger != -1:
                minDistance = min(minDistance, closestBigger - index1)

        return minDistance

    def findClosestSmaller(self, nums: List[int], target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if nums[m] < target:
                    return nums[m]
                return -1
            if nums[m] < target:
                l = m
            else:
                r = m - 1

        return -1

    def findClosestBigger(self, nums: List[int], target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] > target:
                    return nums[m]
                return -1
            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return -1


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
