from random import shuffle
from typing import List

# O(N) time & O(1) space.
# 1) It's natural to think of using the median of the array, but we have to use
# quick sort idea to partition the array (from lc215 kth largest element), which takes O(n) time.
# 2) then move the numbers around, pay attention to deal with numbers == median. It's kind of tricky
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        median = self.findKthLargest(nums, n // 2)

        # step 1: make sure even slots have smaller numbers
        i = 0
        j = 1
        while j < n:
            while i < n and nums[j] < median:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
            j += 2

        # step 2 make sure odd slots have bigger numbers
        i = 0
        j = 1
        while i < n:
            while j < n and nums[i] > median:
                nums[i], nums[j] = nums[j], nums[i]
                j += 2
            i += 2

        # step 3 move all medians in the odd indexes to the far right
        i = 1
        j = n - 1 if n % 2 == 0 else n - 2
        while i < j:
            while nums[i] == median and i < j:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 2
            i += 2

        # step 4: move all medians in the even indexes to the far left
        i = 0
        j = n - 1 if n % 2 != 0 else n - 2
        while i < j:
            while nums[j] == median and i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
            j -= 2

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        shuffle(nums)
        l, r = 0, len(nums) - 1
        # it's important to realize that nums[:l] < nums[l] < nums[r] <= nums[r + 1:] after partition
        while l < r:
            j = self.partitionArray(nums, l, r)
            if j == k:
                return nums[k]
            if j < k:
                l = j + 1
            else:
                r = j - 1
        return nums[k]

    def partitionArray(self, nums: List[int], l: int, r: int) -> int:
        i, j = l, r
        while i < j:
            while i < j and nums[i] <= nums[l]:
                i += 1
            # pay attention to the "j >= i" here:
            # because we need to return j and make sure all nums[j + 1:] strictly > nums[j]
            while j >= i and nums[j] > nums[l]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]
        return j


nums = [13, 6, 5, 5, 4, 2]
Solution().wiggleSort(nums)
print(nums)

nums = [4, 5, 4, 5, 5, 6, 5, 6]
Solution().wiggleSort(nums)
print(nums)
