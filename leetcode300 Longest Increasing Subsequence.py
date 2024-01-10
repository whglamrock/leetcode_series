from typing import List

# O(N * logN) solution. P.S., if running time of O(N * logN) is required, it's a hard question
# see explanation: https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # tail[i] is the smallest tail of all LIS of length i + 1
        tail = [0] * n
        size = 0

        # for each num, try to insert in the tail
        for num in nums:
            l, r = 0, size
            # need to find biggest tail[m] >= num
            while l < r:
                m = (l + r) // 2
                if tail[m] == num:
                    l = m
                    break
                elif tail[m] < num:
                    l = m + 1
                else:
                    r = m

            tail[l] = num
            if l == size:
                size += 1

        return size


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