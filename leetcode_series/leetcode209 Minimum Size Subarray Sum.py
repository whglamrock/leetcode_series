
# O(n) time, O(1) space solution
# keep a minimum slicing window, the sum of which always >= s

class Solution(object):
    def minSubArrayLen(self, s, nums):

        if not nums or sum(nums) < s:
            return 0

        cursum = 0
        l = 0
        minsize = len(nums)

        for i, num in enumerate(nums):
            cursum += num
            while cursum >= s:
                minsize = min(minsize, i - l + 1)
                cursum -= nums[l]
                l += 1

        return minsize



s = 7
nums = [2, 3, 1, 2, 4, 3]
Sol = Solution()
print Sol.minSubArrayLen(s, nums)



'''
# the leetcode also asks for a 0(nlogn) solution...
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

        minsize = n
        for i in xrange(n + 1):
            target = sums[i] + s
            # the left/right bound of contiguous array is i/end
            end = self.binarysearch(i, n, sums, target)
            # then within all left bounds in sums[i + 1:], we can't find a valid right bound
            if sums[end] - sums[i] < s: break
            minsize = min(minsize, end - i)

        return minsize

    # to find the smallest/leftmost sums[x] in sums[lo: hi + 1] that sums[x] - sums[lo] >= s
    # we assume that we definitely can find such a sums[x]
    def binarysearch(self, lo, hi, sums, target):

        while lo < hi:
            mid = lo + (hi - lo) / 2
            # this mid is candidate
            if sums[mid] > target:
                hi = mid
            # this mid is invalid, then the left bound should be mid + 1
            elif sums[mid] < target:
                lo = mid + 1
            else:
                # we already found the leftmost one, because every element in sums is unique
                return mid

        return lo
'''
