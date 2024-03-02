from collections import defaultdict
from random import randint
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.numToIndexes = defaultdict(list)
        for i, num in enumerate(nums):
            self.numToIndexes[num].append(i)

    def pick(self, target: int) -> int:
        indexes = self.numToIndexes[target]
        return indexes[randint(0, len(indexes) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
