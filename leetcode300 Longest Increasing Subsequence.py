
# O(nlogn) solution. P.S., if running time of O(nlog) is required, it's a hard question
# see explanation: https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation

class Solution(object):
    def lengthOfLIS(self, nums):

        if not nums:
            return 0

        n = len(nums)
        tail = [0] * n
        size = 0

        for num in nums:
            # we only search in [0, size) because we wanna potentially grow length
            l, r = 0, size

            # we are actually looking for inserting position for num;
                # i.e., look for tail[l - 1] < num and override tail[l]
            while l < r:
                m = l + (r - l) / 2
                if tail[m] < num:
                    l = m + 1
                else:
                    r = m

            # insert the num
            tail[l] = num
            # all existing tails are all < num so we can grow the size by 1
            if size == l:
                size += 1

        return size



print Solution().lengthOfLIS([10, 9, 2, 5, 1, 7, 101, 18])