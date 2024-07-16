from typing import List


# O(N * logN) solution. P.S., if running time of O(N * logN) is required, it's a hard question
# see explanation: https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)
                continue
            indexEqualOrBigger = self.findLeftMostIndexEqualOrBiggerThan(tails, num)
            # for case like [4, 10, 4, 3, 8, 9], we need to avoid tails become [4, 4]
            if indexEqualOrBigger == -1 or tails[indexEqualOrBigger] == num:
                continue
            tails[indexEqualOrBigger] = num

        return len(tails)

    def findLeftMostIndexEqualOrBiggerThan(self, nums: List[int], target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] >= target:
                    return m
                return -1
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return -1


print(Solution().lengthOfLIS([10, 9, 2, 5, 1, 7, 101, 18]))


'''
# a naive O(N * N) solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
'''