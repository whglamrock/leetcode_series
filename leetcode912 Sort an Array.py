from typing import List

# remember how to do merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return nums

        m = len(nums) // 2
        left, right = self.mergeSort(nums[:m]), self.mergeSort(nums[m:])
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return nums
