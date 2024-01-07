from random import shuffle
from typing import List

# partition the array so that nums[:k + 1] <= some pivot, and nums[k + 1:] > the pivot.
# it's mathematically proven that the while loop only runs constant amount of time.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # find kth smallest
        k = len(nums) - k
        # help make time complexity close to O(n) based on mathematical research
        shuffle(nums)
        l, r = 0, len(nums) - 1
        # when l == r there is no need to further partition the array
        while l < r:
            j = self.partition(nums, l, r)
            if j == k:
                return nums[k]
            elif j < k:
                l = j + 1
            else:
                r = j - 1

        return nums[k]

    # quick sort
    def partition(self, nums: List[int], l: int, r: int) -> int:
        i, j = l, r

        while i < j:
            while i < r and nums[i] <= nums[l]:
                i += 1
            while j > l and nums[j] > nums[l]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]
        return j


print(Solution().findKthLargest(nums = [1, 1, 1, 2, 2, 3, 4, 6, 6, 7, 9], k = 5))



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
