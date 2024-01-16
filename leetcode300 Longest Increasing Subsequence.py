from typing import List

# O(N * logN) solution. P.S., if running time of O(N * logN) is required, it's a hard question
# see explanation: https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # tails stores the smallest tail of any IS with certain length
        tails = []
        # records the length of current LIS
        size = 0

        for i in range(n):
            # can increase the LIS
            if not tails or nums[i] > tails[-1]:
                tails.append(nums[i])
                size += 1
            else:
                # there is no place for nums[i]
                if nums[i] == tails[-1]:
                    continue
                indexOfBiggerNumber = self.findIndexBiggerThan(tails, nums[i])
                if indexOfBiggerNumber != -1:
                    tails[indexOfBiggerNumber] = nums[i]

        return size

    # find the smallest index bigger than target
    def findIndexBiggerThan(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                if nums[l] > target:
                    return l
                else:
                    return -1
            m = (l + r) // 2
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