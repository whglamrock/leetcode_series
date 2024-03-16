from random import shuffle
from typing import List

# partition the array so that nums[:k + 1] <= some pivot, and nums[k + 1:] > the pivot.
# it's mathematically proven that the while loop only runs constant amount of time.
# P.S.: the stupid leetcode is giving TLE for below solution in a really stupid test case. But it's definitely
# acceptable in real interview.
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
            while i < j and nums[i] <= nums[l]:
                i += 1
            # when j == i, we won't need any more swap but we need j further -=1 once more
            # so that nums[:j + 1] strictly <= nums[l], nums[j + 1:] strictly > nums[l]
            while j >= i and nums[j] > nums[l]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]
        return j


print(Solution().findKthLargest(nums=[1, 1, 1, 2, 2, 3, 4, 6, 6, 7, 9], k=5))


'''
from heapq import *

# O(n * log(k)) heapq solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heappush(pq, num)
            if len(pq) > k:
                # pop out the smallest so the largest ones remain in heap
                heappop(pq)
        
        return pq[0]
'''
