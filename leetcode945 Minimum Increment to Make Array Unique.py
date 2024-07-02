from collections import Counter, deque
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        duplicates = deque()
        for num in sorted(numCount.keys()):
            if numCount[num] > 1:
                for i in range(numCount[num] - 1):
                    duplicates.append(num)

        if not duplicates:
            return 0

        replacementNum = duplicates[0] + 1
        replacementSet = set()
        ans = 0
        while duplicates:
            dupe = duplicates.popleft()
            replacementNum = max(replacementNum, dupe + 1)
            while replacementNum in numCount or replacementNum in replacementSet:
                replacementNum += 1

            replacementSet.add(replacementNum)
            ans += replacementNum - dupe

        return ans
