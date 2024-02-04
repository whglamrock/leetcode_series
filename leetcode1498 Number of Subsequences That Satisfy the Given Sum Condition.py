from typing import List

# The hardest part is to figure out that the order of the subsequence doesn't matter
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        mod = 10 ** 9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += 2 ** (r - l)
                l += 1

        return ans % mod
