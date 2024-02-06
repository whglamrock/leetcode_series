from collections import Counter
from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        numCount = Counter(arr)
        currCount = 0
        deficit = 0
        maxPossible = 1
        for i in range(1, n + 1):
            if i in numCount:
                if deficit >= numCount[i]:
                    # pay off the debt first
                    deficit -= numCount[i]
                    # but we used all numCount[i] and are left with 0 number of i, so we need to borrow one i
                    currCount += 1
                    deficit += 1
                else:
                    currCount += numCount[i] - deficit
                    deficit = 0
            else:
                currCount += 1
                deficit += 1
            maxPossible = i
            if currCount >= n:
                break

        return maxPossible


print(Solution().maximumElementAfterDecrementingAndRearranging([1, 2, 2, 4, 6]))
