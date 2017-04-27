
'''
This idea came from: https://leetcode.com/discuss/36966/solution-explained
The idea is Quicksort, but takes only O(n) time complexity
'''

# P.S. Selection sort: on average O(N^2) running time
# O(n) solution. It is proved that if we randomly choose the pivot (or pre-shuffle the nums array),
#   the number of times the final while loop executes will be constant
# If we don't shuffle the nums array, we can randomly choose the pivot.

import random

class Solution(object):
    def findKthLargest(self, nums, k):

        if not nums or len(nums) < k:
            return

        def exchange(array, i, j):

            array[i], array[j] = array[j], array[i]

        # notice how the shuffle is written: all elements exchange with left ones (including self)
        # in this way, we can make sure that each number has the same probability of being at each position
        #   e.g., the probability of the first number being at positon 0 is: 1/2 * 2/3 * 3/4 *...* (n-1)/n
        #   = 1/n
        def shuffle(array):

            for i in xrange(1, len(array)):
                j = random.randint(0, i)    # 0 <= j <= i, different from randrange()
                exchange(array, i, j)

        def partition(array, lo, hi):

            i, j = lo, hi
            # the condition has to be i < j, because of test cases like [99, 99],
            #   when the j won't even move and while loop becomes infinite
            while i < j:
                # after the first while loop, if i < hi, then array[i] > array[lo]
                while i < hi and array[i] <= array[lo]:
                    i += 1
                # after the second while loop, if j > lo, then array[j] <= array[lo]
                while j > lo and array[j] > array[lo]:
                    j -= 1
                # based on the two exit conditions, when i > j happens, then we have
                #   the partition array we want
                if i > j: break
                exchange(array, i, j)
            # we exchange array[lo] with array[j] instead of array[i] because we want
            #   strictly ensure that after exchange, all elements on the left of array[lo]
            #   are <= array[lo], on the right are > array[lo]
            exchange(array, lo, j)  # remember: array[j + 1] > array[lo]
            return j

        shuffle(nums)
        k = len(nums) - k   # we wanna find the len(nums) - k smallest
        lo, hi = 0, len(nums) - 1

        # we always make sure lo <= k <= hi; the exit condition is lo == hi
        while lo < hi:
            j = partition(nums, lo, hi)
            if j < k:
                lo = j + 1
            elif j > k:
                hi = j - 1
            else:
                return nums[k]    # or break

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


# what' interesting is that the simplest solution actually runs super fast:

class Solution(object):
    def findKthLargest(self, nums, k):

        if not nums or len(nums) < k:
            return

        nums.sort()
        nums.reverse()
        return nums[k - 1]
'''
