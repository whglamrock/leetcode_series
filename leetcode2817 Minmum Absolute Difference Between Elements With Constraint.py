from heapq import *
from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        numsWithIndex = sorted([[nums[i], i] for i in range(len(nums))])
        leftPq, rightPq = [], []

        minDiff = 2147483647
        for i in range(len(nums)):
            num, index = numsWithIndex[i]
            # push in the current number first because x can be 0
            heappush(leftPq, [index, num])
            heappush(rightPq, [-index, num])
            while leftPq and index - leftPq[0][0] >= x:
                minDiff = min(minDiff, num - heappop(leftPq)[1])
            while rightPq and -rightPq[0][0] - index >= x:
                minDiff = min(minDiff, num - heappop(rightPq)[1])

        return minDiff
