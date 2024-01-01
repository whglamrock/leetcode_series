from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        elementCount = Counter(arr)
        return len(set(elementCount.values())) == len(elementCount)
