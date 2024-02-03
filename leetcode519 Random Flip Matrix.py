from random import randint
from typing import List

# Idea is fisher yates shuffle algorithm. See: https://leetcode.com/problems/random-flip-matrix/solutions/154053/java-ac-solution-call-least-times-of-random-nextint-function/
# The O(M * N) space solution should be acceptable in real interview
class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.size = m * n
        self.indexToUsedIndex = {}

    def flip(self) -> List[int]:
        i = randint(0, self.size - 1)
        self.size -= 1
        actualIndex = i if i not in self.indexToUsedIndex else self.indexToUsedIndex[i]
        lastActualIndex = self.size if self.size not in self.indexToUsedIndex else self.indexToUsedIndex[self.size]
        self.indexToUsedIndex[i] = lastActualIndex
        return divmod(actualIndex, self.n)

    def reset(self) -> None:
        self.indexToUsedIndex = {}
        self.size = self.m * self.n


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
