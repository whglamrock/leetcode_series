
# O(n) time, O(1) space solution
# keep a minimum slicing window, the sum of which always >= s

class Solution(object):
    def minSubArrayLen(self, s, nums):

        if not nums or sum(nums) < s:
            return 0

        winsum = 0
        i = 0
        minlen = len(nums)

        for j, num in enumerate(nums):
            winsum += num
            while winsum >= s:
                minlen = min(minlen, j + 1 - i)
                winsum -= nums[i]
                i += 1

        return minlen



s = 7
nums = [2, 3, 1, 2, 4, 3]
Sol = Solution()
print Sol.minSubArrayLen(s, nums)



'''
# the leetcode also asks for a O(nlogn) solution...
# 0(nlogn) time, O(n) space solution
# idea from: https://discuss.leetcode.com/topic/13749/two-ac-solutions-in-java-with-time-complexity-of-n-and-nlogn-with-explanation/2

class Solution(object):
    def minSubArrayLen(self, s, nums):

        if not nums or sum(nums) < s:
            return 0

        n = len(nums)
        sums = [0] * (n + 1)
        for i in xrange(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        minlen = n
        for i in xrange(n):
            # the left/right bound of contiguous array is i/end
            end = self.binarySearch(sums, i, n, sums[i] + s)
            # then within all left bounds in sums[i + 1:], we can't find a valid right bound
            if sums[end] < s + sums[i]: break
            minlen = min(minlen, end - i)

        return minlen

    # to find the leftmost(i.e., smallest) sums[i] that >= target
    def binarySearch(self, sums, l, r, target):

        # exit condition is l == r
        while l < r:
            mid = l + (r - l) / 2
            if sums[mid] == target:
                return mid
            elif sums[mid] < target:    # sums[mid] can't be the candidate
                l = mid + 1
            else:   # sums[mid] is still the candidate
                r = mid

        return l    # or return r
'''
