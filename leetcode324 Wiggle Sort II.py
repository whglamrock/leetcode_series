
import random

# O(N) time & O(1) space. The O(n) time solution has to derive from the median which you can use as a pivot
    # to partition the nums.

# To deal with the condition where we have a lot of same medians, we need to avoid using biggest comparing/paring
    # with smallest numbers
# P.S.: it's very IMPORTANT! to put smallest numbers at far right & biggest numbers at far left, instead of
    # smallest numbers at far left & biggest numbers at far right
    # taking [4,4,5,5,5,5,6,6] as example, the results of two approaches will be respectively:
    # [4,5,4,5,5,6,5,6] / [5,6,5,6,4,5,4,5]

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        # make num of smaller nums >= num of bigger nums
        med = self.findKthLargest(nums, n / 2)

        # step 1: make sure even slots have smaller numbers
        i = 0
        j = 1
        while j < n:
            while nums[j] < med and i < n:
                self.exchange(nums, i, j)
                i += 2
            j += 2

        # step 2: make sure odd slots have bigger numbers:
        i = 0
        j = 1
        while i < n:
            while nums[i] > med and j < n:
                self.exchange(nums, i, j)
                j += 2
            i += 2

        # step 3: make sure the biggest number stay on the far left
        i = 1
        j = n / 2 * 2 - 1
        while i < j:
            while nums[i] == med and j > i:
                self.exchange(nums, i, j)
                j -= 2
            i += 2

        # step 4: make sure the smallest number stay on the far right
        i = 0
        j = (n - 1) / 2 * 2
        while i < j:
            while nums[j] == med and i < j:
                self.exchange(nums, i, j)
                i += 2
            j -= 2

    def findKthLargest(self, nums, k):
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
        return nums[k]

    def partition(self, nums, l, r):
        i, j = l, r
        while i < j:
            while i <= r and nums[i] <= nums[l]:
                i += 1
            while j > l and nums[j] > nums[l]:
                j -= 1
            if i >= j:
                break
            self.exchange(nums, i, j)
        self.exchange(nums, j, l)
        return j

    def exchange(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp



nums = [13, 6, 5, 5, 4, 2]
Solution().wiggleSort(nums)
print nums

nums = [4,5,4,5,5,6,5,6]
Solution().wiggleSort(nums)
print nums
