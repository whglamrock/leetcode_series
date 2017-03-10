'''
This idea came from: https://leetcode.com/discuss/36966/solution-explained
The idea is Quicksort, but takes only O(n) time complexity
'''

# P.S. Selection sort: on average O(N^2) running time

# O(n) solution
# If we don't shuffle the nums array, we can randomly choose the pivot.

import random
class Solution(object):
    def findKthLargest(self, nums, k):

        def exchange(a, i, j):

            a[i], a[j] = a[j], a[i]

        # notice how the shuffle is written: all elements exchange with left ones
        def shuffle(array):

            for index in xrange(1, len(array)):
                # the maximum of r will still be len(array) - 1
                r = random.randrange(index + 1)
                exchange(array, r, index)

        # To ensure all elements on the left of j are <= array[lo],
            #   on the right are > array[lo]
        def partition(array, lo, hi):

            i, j = lo, hi
            # the condition can't be i <= j (e.g., try test case nums = [99, 99], k = 1).
            while i < j:
                # We can switch the order of two following while loops because
                #   they don't overlap.
                # At last we can guarantee array[j] <= array[lo] and array[j + 1:]
                #   are all > array[lo].
                while j > lo and array[j] > array[lo]:
                    j -= 1
                # At last there could be (array[i] > array[lo] and i > j),
                #   where we cannot exchange(array, i, j) here.
                # And it also explains why we can't exchange(array, lo, i) at last.
                while i < hi and array[i] <= array[lo]:
                    i += 1
                if i > j: break
                exchange(array, i, j)
            # Due to the above settings, we cannot exchange(array, lo, i) here,
            #   and we need to make sure that all array[j + 1:] are strictly > array[lo] not >=.
            exchange(array, lo, j)
            return j

        shuffle(nums)
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1

        # logarithmically reduce the search range, but the number of
        # times the while loop operates will still be linear
        while lo < hi:
            j = partition(nums, lo, hi)
            # lo = j + 1 not j
            if j < k:
                lo = j + 1
            # hi = j - 1 not j
            elif j > k:
                hi = j - 1
            else:
                break

        return nums[k]



nums = [1, 1, 1, 2, 2, 3, 4, 6, 6, 7, 9]
k = 5
Sol = Solution()
print Sol.findKthLargest(nums, k)



'''
# O(nlogn) solution:
from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):

        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)

        return heappop(heap)
'''
