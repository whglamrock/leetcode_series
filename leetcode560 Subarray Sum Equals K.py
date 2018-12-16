
from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):

        preSum = 0
        preSumCount = defaultdict(int)
        ans = 0
        for num in nums:
            preSum += num
            if preSum == k:
                ans += 1
            if preSum - k in preSumCount:
                ans += preSumCount[preSum - k]
            preSumCount[preSum] += 1

        return ans



Sol = Solution()
print Sol.subarraySum([0,0,0,0,0,0,0,0,0,0], 0)
