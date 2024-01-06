from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numOfGoodPairs = 0
        numCounter = defaultdict(int)

        for num in nums:
            numOfGoodPairs += numCounter[num]
            numCounter[num] += 1

        return numOfGoodPairs
