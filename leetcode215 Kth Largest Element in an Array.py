
import random

# This idea came from: https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60294/Solution-explained
# The idea is Quicksort, but takes only O(n) time complexity because it's mathematically proved the while loop
    # will only run constant number of times

# in real interview, run edge cases like [1, 2], [2, 1], [99, 99, 1], [1, 99, 99]
# and a normal test case like [3,2,1,5,6,4]

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # make it become finding the k smallest num
        k = len(nums) - k
        random.shuffle(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            j = self.partition(nums, l, r)
            if j == k:
                return nums[k]
            elif j < k:
                l = j + 1
            else:
                r = j - 1

        # can also return nums[l] because at this point l == r == k
        return nums[k]

    # the quick sort idea: partition the array. find/make an index j that
    # all nums[:j] <= nums[j] and all nums[j + 1:] > nums[j]. Note that
    # nums[:j]/nums[j + 1:] can contain 0 numbers
    def partition(self, nums, l, r):
        i, j = l, r
        # we assume we are gonna pick nums[l] as the pivot so we compare with nums[l]
        while i < j:
            # make sure after exchange all nums[i] <= the pivot.
            # note that the condition for while loop can also be i <= r because when we exchange i, j it has to be
                # i < j so using i <= r won't cause index out of range
            while i < r and nums[i] <= nums[l]:
                i += 1
            # make sure after exchange all nums[j] > the pivot
            while j > l and nums[j] > nums[l]:
                j -= 1
            # for case like [99, 99], j can just stay put and i moves all the way to r
            if i >= j:
                break
            self.exchange(nums, i, j)

        self.exchange(nums, j, l)
        return j

    def exchange(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp



print Solution().findKthLargest(nums = [1, 1, 1, 2, 2, 3, 4, 6, 6, 7, 9], k = 5)



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
