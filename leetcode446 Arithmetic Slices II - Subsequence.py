from collections import defaultdict
from copy import deepcopy
from typing import List

# O(N ^ 2) solution
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        indexToNumCountInLeft = {}
        numCount = defaultdict(int)
        for i, num in enumerate(nums):
            indexToNumCountInLeft[i] = deepcopy(numCount)
            numCount[num] += 1

        n = len(nums)
        indexToDiffToCount = {}
        dp = [0] * n
        for i in range(2, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = 0
                # 3 number sequence
                if nums[j] - diff in indexToNumCountInLeft[j]:
                    count += indexToNumCountInLeft[j][nums[j] - diff]
                # more than 3 number sequence
                if j in indexToDiffToCount and diff in indexToDiffToCount[j]:
                    count += indexToDiffToCount[j][diff]

                if i not in indexToDiffToCount:
                    indexToDiffToCount[i] = defaultdict(int)
                indexToDiffToCount[i][diff] += count
                dp[i] += count

        return sum(dp)
