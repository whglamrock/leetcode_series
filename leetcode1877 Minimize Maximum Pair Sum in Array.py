from typing import List

# proof that pairing min with max is always optimal: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/solutions/1238655/java-c-python-min-max/
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[-1]
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - i - 1])
        return ans
