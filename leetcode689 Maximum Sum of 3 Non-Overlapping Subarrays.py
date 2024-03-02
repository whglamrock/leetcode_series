from typing import List

# 1) It shouldn't be too hard to think of using prefixSum + 3 rounds of dp array to get the sum of 3 k length subarrays;
# But the question asks for the starting indexes and lexicographically smallest index triplets: this means we need to
# keep track of which starting indexes we used to get the max n-K sum (n = 1/2/3)
# 2) In dp array, dp[i] means in the xth round what the max x-k sum value is with the last subarray ends at nums[i],
# where x = 1/2/3.
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        prefixSums = []
        for num in nums:
            if not prefixSums:
                prefixSums.append(num)
            else:
                prefixSums.append(num + prefixSums[-1])

        n = len(nums)
        indexToStartIndexOfMax1stKSum = {}
        dp1 = [-1] * n
        dp1[k - 1] = prefixSums[k - 1]
        indexToStartIndexOfMax1stKSum[k - 1] = 0
        for i in range(k, n - 2 * k):
            # if dp1[i - 1] == dp1[i] we need to use the starting index of dp1[i - 1]
            if dp1[i - 1] >= prefixSums[i] - prefixSums[i - k]:
                indexToStartIndexOfMax1stKSum[i] = indexToStartIndexOfMax1stKSum[i - 1]
                dp1[i] = dp1[i - 1]
            else:
                indexToStartIndexOfMax1stKSum[i] = i - k + 1
                dp1[i] = prefixSums[i] - prefixSums[i - k]

        dp2 = [-1] * n
        indexToStartIndexesOfMaxTwoKSum = {}
        for i in range(k * 2 - 1, n - k):
            if dp2[i - 1] >= dp1[i - k] + (prefixSums[i] - prefixSums[i - k]):
                indexToStartIndexesOfMaxTwoKSum[i] = indexToStartIndexesOfMaxTwoKSum[i - 1]
                dp2[i] = dp2[i - 1]
            else:
                indexToStartIndexesOfMaxTwoKSum[i] = [indexToStartIndexOfMax1stKSum[i - k], i - k + 1]
                dp2[i] = dp1[i - k] + (prefixSums[i] - prefixSums[i - k])

        dp3 = [-1] * n
        indexToStartIndexesOfMaxThreeKSum = {}
        for i in range(k * 3 - 1, n):
            if dp3[i - 1] >= dp2[i - k] + (prefixSums[i] - prefixSums[i - k]):
                indexToStartIndexesOfMaxThreeKSum[i] = indexToStartIndexesOfMaxThreeKSum[i - 1]
                dp3[i] = dp3[i - 1]
            else:
                indexToStartIndexesOfMaxThreeKSum[i] = indexToStartIndexesOfMaxTwoKSum[i - k] + [i - k + 1]
                dp3[i] = dp2[i - k] + (prefixSums[i] - prefixSums[i - k])

        return indexToStartIndexesOfMaxThreeKSum[n - 1]
