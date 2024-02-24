from collections import deque
from typing import List

class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        words = set(words)
        matchedIndexes = deque()
        matchedLeft, matchedRight = None, None
        for r in range(len(s) - 1, -1, -1):
            if matchedLeft is not None and r < matchedLeft - 1:
                matchedIndexes.appendleft([matchedLeft, matchedRight])
                matchedLeft, matchedRight = None, None
            if matchedLeft is not None:
                for l in range(matchedLeft):
                    if s[l:r + 1] in words:
                        matchedLeft = l
                        break
            else:
                for l in range(r + 1):
                    if s[l:r + 1] in words:
                        matchedLeft, matchedRight = l, r
                        break

        if matchedLeft is not None:
            matchedIndexes.appendleft([matchedLeft, matchedRight])

        ans = []
        j = 0  # scan through matchedIndexes
        i = 0  # s index
        while i < len(s) and j < len(matchedIndexes):
            if i == matchedIndexes[j][0]:
                ans.append('<b>')
                ans.append(s[matchedIndexes[j][0]:matchedIndexes[j][1] + 1])
                ans.append('</b>')
                i = matchedIndexes[j][1] + 1
                j += 1
            else:
                ans.append(s[i])
                i += 1

        if i < len(s):
            ans.append(s[i:])

        return ''.join(ans)
