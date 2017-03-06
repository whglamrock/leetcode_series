# O(nlogn) solution (if running time of O(nlog) is required, it's a hard question).

# idea came from: https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation
# see his explanation: "We can easily prove that tails is a increasing array"; "tails is an array storing the
# smallest tail of all increasing subsequences with length i + 1 in tails[i]"

class Solution(object):
    def lengthOfLIS(self, nums):

        if (not nums) or len(nums) == 0:
            return 0

        n = len(nums)
        tail = [0] * n  # it could 0, or whatever number/char. try [100] * n, it will also pass.
        size = 0
        for num in nums:
            # no need to check the index beyond the size, because those are
            # zeroes (or i.e., unchanged. we can initialize the tail other numbers)
            l, r = 0, size
            # find the first position where tail[i] >= num, then update this tail[i]
            while l < r:
                m = l + (r - l) / 2
                if tail[m] < num:
                    l = m + 1
                else:
                    r = m
            tail[l] = num
            # the following can be interpreted as: if the length of longest sequence
            # increased, the size will be increased; otherwise it won't be changed.
            size = max(size, l + 1)
            #print tail

        return size



Sol = Solution()
nums = [10, 9, 2, 5, 1, 7, 101, 18]
print Sol.lengthOfLIS(nums)



# this algorithm can find the length of longest subsequence but the tail is not the
# actual subsequence.
'''
# my original O(n^2) solution
class Solution(object):
    def lengthOfLIS(self, nums):

        if (not nums) or len(nums) == 0:
            return 0

        n = len(nums)
        dp = [1] * n
        for i in xrange(1, n):
            for j in xrange(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

        #print dp
        return max(dp)
'''