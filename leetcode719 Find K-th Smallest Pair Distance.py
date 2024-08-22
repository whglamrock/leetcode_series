from typing import List


# It's natural to think of binary search, but it's most important to realize you can use sliding window
# to achieve O(n) time when counting pair diffs smaller than certain threshold.
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxDiff = nums[-1] - nums[0]
        minDiff = 2147483647
        for i in range(1, len(nums)):
            minDiff = min(minDiff, nums[i] - nums[i - 1])

        l, r = minDiff, maxDiff
        while l < r:
            m = (l + r) // 2
            numOfPairsWithSmallerDiff = self.countPairsDiffSmallerEqualThan(nums, m)
            if numOfPairsWithSmallerDiff < k:
                l = m + 1
            # keep in mind when numOfPairsWithSmallerDiff == k we shouldn't directly return
            # because there may be 0 pair of nums whose pair diff is numOfPairsWithSmallerDiff
            else:
                r = m

        # exit condition of the above while loop is l == r
        return l

    # need to realize we can achieve O(n) for counting pair diff smaller than a threshold with sliding window
    def countPairsDiffSmallerEqualThan(self, nums: List[int], diff: int) -> int:
        count = 0
        l = 0
        for r, num in enumerate(nums):
            while l < r and num - nums[l] > diff:
                l += 1
            count += r - l

        return count
