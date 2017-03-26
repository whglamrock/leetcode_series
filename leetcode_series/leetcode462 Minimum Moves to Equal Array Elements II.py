
# choose the median as the final destination.
# For reason see https://discuss.leetcode.com/topic/69236/o-n-solution-with-detailed-explanation
# Use quickselect can reach O(N)

import random

class Solution(object):
    def minMoves2(self, nums):

        n = len(nums)
        if n % 2 == 0:
            median = (self.findKthLargest(nums, n / 2) + self.findKthLargest(nums, n / 2 + 1)) / 2
        else:
            median = self.findKthLargest(nums, n / 2 + 1)

        ans = 0
        for num in nums:
            ans += abs(num - median)

        return ans

    def findKthLargest(self, nums, k):

        def exchange(a, i, j):
            a[i], a[j] = a[j], a[i]

        def shuffle(array):
            for index in xrange(1, len(array)):
                r = random.randrange(index + 1)
                exchange(array, r, index)

        def partition(array, lo, hi):
            i, j = lo, hi
            while i < j:
                while j > lo and array[j] > array[lo]:
                    j -= 1
                while i < hi and array[i] <= array[lo]:
                    i += 1
                if i > j: break
                exchange(array, i, j)
            exchange(array, lo, j)
            return j

        shuffle(nums)
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            j = partition(nums, lo, hi)
            if j < k:
                lo = j + 1
            elif j > k:
                hi = j - 1
            else:
                break

        return nums[k]



Sol = Solution()
nums = [1,2,4,3,7,6,5]
print Sol.minMoves2(nums)


