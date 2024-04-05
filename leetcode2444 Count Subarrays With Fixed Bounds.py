from typing import List

# Intuition:
# 1) We keep a window where all elements in it are within [minK, maxK].
# 2) We record the lastIndex of minK and maxK. If any element is out of boundary it means the left bound has to be reset
# to current index + 1 (next index)
# 3) If the element is within the bound, we keep expanding the window. If the window is valid, the current element can be
# used as the right bound of the subarray. And the left bound of subarray can be anywhere between
# [l, min(lastMinKIndex, lastMaxKIndex)], inclusive.
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastMinKIndex, lastMaxKIndex = None, None
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            if not minK <= num <= maxK:
                lastMinKIndex, lastMaxKIndex = None, None
                l = r + 1
                continue

            if num == minK:
                lastMinKIndex = r
            if num == maxK:
                lastMaxKIndex = r

            if lastMinKIndex is not None and lastMaxKIndex is not None:
                ans += min(lastMinKIndex, lastMaxKIndex) - l + 1

        return ans
