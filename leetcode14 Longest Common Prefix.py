from collections import defaultdict
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        indexToChars = defaultdict(set)
        minLen = min(len(word) for word in strs)
        for word in strs:
            for i in range(minLen):
                indexToChars[i].add(word[i])
                if len(indexToChars[i]) > 1:
                    minLen = min(minLen, i)
                    break

        return strs[0][:minLen]
