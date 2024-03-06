from typing import List

# if there is overlapping, we choose the one with smaller end
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr = None
        ans = 0
        for start, end in intervals:
            if curr is None or start >= curr:
                curr = end
                continue

            # overlapping, we will have to remove one of them
            curr = min(end, curr)
            ans += 1

        return ans
