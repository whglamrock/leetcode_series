
# O(N * logN) solution. P.S., if running time of O(N * logN) is required, it's a hard question
# see explanation: https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        # tail[i] is the smallest tail for LIS of length i + 1
        tail = [0] * n
        size = 0

        for num in nums:
            # we only need to search in [0, size] because nums[size:] are all 0
            l, r = 0, size
            # look for insert position for num. i.e., find the last number < num
            while l < r:
                m = (l + r) / 2
                # then for sure m is not the position we want to insert num on
                if tail[m] < num:
                    l = m + 1
                # 1) nums[m] == num: it doesn't matter whether we insert num here
                # 2) nums[m] > num: it's possible we will insert here so keep m within our search range
                else:
                    r = m

            # when all existing tails are < num, l == size and tail[l] == 0
                # l won't ever go index out of range because size <= index of num
            # otherwise override tail[l]
            tail[l] = num
            if l == size:
                size += 1

        return size



print Solution().lengthOfLIS([10, 9, 2, 5, 1, 7, 101, 18])



'''
# a naive O(N^2) solution

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        tail = [1] * n
        
        for i in xrange(1, n):
            num = nums[i]
            for j in xrange(i):
                if nums[j] < nums[i]:
                    tail[i] = max(tail[j] + 1 , tail[i])
        
        return max(tail)
'''