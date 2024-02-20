from typing import List

# 1) Sort the envelopes by width ascending and height descending. The reason why we sort by height descending is because
# 2) we wanna avoid inaccurate extension of russian doll length.
# Consider the following example (if sort envelopes by height ascending):
# envelopes = [[1, 1], [2, 4], [3, 3], [3, 4]], and the current smallestHeightsAtEachLength = [1, 4] after scanning the
# first 2 envelopes. [3, 3] will update smallestHeightsAtEachLength to [1, 3]; then [3, 4] will incorrectly extend the
# smallestHeightsAtEachLength by 1, to [1, 3, 4].
# 3) So we need to sort envelopes descending. This way, when we use "smallestHeightsAtEachLength[-1] < height" to extend
# the smallestHeightsAtEachLength we know for sure the existing heights in smallestHeightsAtEachLength all have smaller
# corresponding widths.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # smallestHeights[i] means the smallest height of russian doll of length (i + 1)
        smallestHeightsAtEachLength = []

        for i, envelope in enumerate(envelopes):
            height = envelope[1]
            if not smallestHeightsAtEachLength or smallestHeightsAtEachLength[-1] < height:
                smallestHeightsAtEachLength.append(height)
            else:
                indexToReplace = self.findMinIndexBigger(smallestHeightsAtEachLength, height)
                if indexToReplace == -1:
                    continue
                smallestHeightsAtEachLength[indexToReplace] = height

        return len(smallestHeightsAtEachLength)

    def findMinIndexBigger(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] >= target:
                    return m
                else:
                    return -1
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return -1
