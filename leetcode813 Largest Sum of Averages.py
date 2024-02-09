from functools import lru_cache
from typing import List

# Time complexity is O(K * N ^ 2) because for each k partition, we can get the maxScoreSum from k - 1 partition scenario
# Proof:
# 1) when k = 1, you need O(N) to get the score for each nums[i:]
# 2) when k = 2, for each nums[i:], you scan through j in nums[i + 1:]. In this case nums[i:] is divided into
# nums[i:j] and nums[j:], then you can get the maxScore of 2 partition for nums[i:]. This takes O(N ^ 2) time
# 3) same idea for all k values. Thus, the total time is O(K * N ^ 2).
class Solution:
    def __init__(self):
        self.prefixSum = []

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        self.prefixSum = []
        for num in nums:
            if not self.prefixSum:
                self.prefixSum.append(num)
            else:
                self.prefixSum.append(self.prefixSum[-1] + num)

        return self.dfs(0, k)

    @lru_cache(None)
    def dfs(self, i: int, k: int) -> float:
        prefixSumToMinus = self.prefixSum[i - 1] if i > 0 else 0
        maxScoreSum = (self.prefixSum[-1] - prefixSumToMinus) / (len(self.prefixSum) - i)
        if k == 1:
            return maxScoreSum

        for j in range(i, len(self.prefixSum) - 1):
            currScore = (self.prefixSum[j] - prefixSumToMinus) / (j - i + 1)
            maxScoreSum = max(maxScoreSum, currScore + self.dfs(j + 1, k - 1))

        return maxScoreSum
