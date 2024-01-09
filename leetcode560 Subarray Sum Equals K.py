from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        prefixSum = 0
        prefixSumToCount = defaultdict(int)
        ans = 0

        for num in nums:
            prefixSum += num
            if prefixSum == k:
                ans += 1
            if prefixSum - k in prefixSumToCount:
                ans += prefixSumToCount[prefixSum - k]
            prefixSumToCount[prefixSum] += 1

        return ans


print(Solution().subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
