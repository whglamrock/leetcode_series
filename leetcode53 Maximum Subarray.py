from typing import List

class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prefixSums = []
        for num in nums:
            if not prefixSums:
                prefixSums.append(num)
            else:
                prefixSums.append(num + prefixSums[-1])

        ans = -2147483648
        minPrefixSum = 0
        for prefixSum in prefixSums:
            ans = max(ans, prefixSum - minPrefixSum)
            minPrefixSum = min(minPrefixSum, prefixSum)

        return ans


print(Solution().maxSubArray([-2, -1, -1, -1, 7, 4, -3, -4, -5, 5]))
