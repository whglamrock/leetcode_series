from functools import lru_cache
from typing import List, Tuple

class Solution:
    def __init__(self):
        self.cols = 0
        self.sentence = []

    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        self.sentence = sentence
        self.cols = cols

        ans = 0
        wordIdx = 0
        for _ in range(rows):
            nextIndex, numOfTimes = self.dp(wordIdx)
            ans += numOfTimes
            wordIdx = nextIndex

        return ans

    @lru_cache(None)
    def dp(self, i: int) -> Tuple[int, int]:
        currLen = 0
        numOfTimes = 0
        # remember this trick
        while currLen + len(self.sentence[i]) <= self.cols:
            currLen += len(self.sentence[i]) + 1
            i += 1
            if i == len(self.sentence):
                numOfTimes += 1
                i = 0

        # i the next index we can jump to, and numOfTimes is how many times we can fit the entire sentence in one row
        return i, numOfTimes
