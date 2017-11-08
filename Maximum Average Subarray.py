
# Question from: https://www.lintcode.com/zh-cn/problem/maximum-average-subarray/

class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):

        l, r = 2147483647, -2147483648
        n = len(nums)
        for num in nums:
            l, r = min(l, num), max(r, num)

        diff = [0 for _ in xrange(n + 1)]
        diff[0] = 0

        while r - l > 10 ** -6:

            # the mid is the candidate of ideal average
            mid = (l + r) / 2.0
            min_pre = 0
            check = False

            for i in xrange(1, n + 1):
                # the diff[i] is the accumulated difference:
                #   (sum of m elements - m * mid), which is invalid when i < k;
                diff[i] = diff[i - 1] + nums[i - 1] - mid
                if i >= k and diff[i] - min_pre >= 0:
                    check = True
                    break
                if i >= k:
                    # min_pre always <= 0, and it has to be k elements
                    #   before diff[i]
                    min_pre = min(min_pre, diff[i - k + 1])

            # notice the exit condition and we need to calculate average
            #   we cannot set new boundary +1 or -1, or we could miss
            #   the answer
            if check:
                l = mid
            else:
                r = mid

        return l    # we can return r too, cuz we need to return a double type